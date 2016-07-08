'''
    sysbench: System evaluation benchmark
    test: Perf_cpu Perf_mem Perf_mysql
'''
import os
from runtest import RunTest

class DoTest(RunTest):
    def __init__(self, setupxml, testxml, homepath, finalresult):
        self.setupxml = os.path.abspath(setupxml)
        self.testxml = os.path.abspath(testxml)
        self.homepath = homepath
    
    def _setup(self):
        '''
         Setup before starting test
        '''
        print self.setupxml
        RunTest._depend('gcc', 'make', 'automake', 'libtool')
        srcdir = RunTest._pretesttool(self.setupxml, self.testxml, 'Perf_mem', self.homepath)
        
        os.chdir(srcdir)
        self._configure('--without-mysql')
        self._make('LIBTOOL=/usr/bin/libtool')

    def _runtest(self):
        basearg = self.baseparameter('Perf_mem', self.testxml)
        print basearg
        num_threads = basearg['num_threads'].split(',')
        print num_threads
        for num_thread in num_threads:
            cmd = "--test=%s --num-threads=%s --memory-block-size=%s --memory-total-size=%s run" % (basearg['test_type'], num_thread, basearg['block_size'], basearg['total_size'])
            RunTest._dotest('sysbench', cmd, basearg['runtimes'])
             
# testcase
#a = Perf_cpu('Testsetup_sample.xml', 'Test_parameter.xml')
#a._setup()
#a._runtest()
