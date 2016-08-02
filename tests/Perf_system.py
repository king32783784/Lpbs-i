'''
    sysbench: System evaluation benchmark
    test: Perf_cpu Perf_mem Perf_mysql
'''
import os
from runtest import RunTest
from pretreatment_result import MkResult

class DoTest(RunTest):
    def __init__(self, setupxml, testxml, homepath, finalresult):
        self.setupxml = os.path.abspath(setupxml)
        self.testxml = os.path.abspath(testxml)
        self.homepath = homepath
        self.result = finalresult
    
    def _setup(self):
        '''
         Setup before starting test
        '''
        print self.setupxml
        print self.testxml
        RunTest._depend('gcc', 'make')
        srcdir = RunTest._pretesttool(self.setupxml, self.testxml, 'Perf_system', self.homepath)
        os.chdir(srcdir)
        self._make('')

    def _runtest(self):
        basearg = self.baseparameter('Perf_system', self.testxml)
        print basearg
        runtimes = basearg['runtimes']
        args_itmp = basearg['c'].split(',')
        args_u = ''
        for arg in args_itmp:
            args_u = args_u + ' -c ' + arg
        args_u = ' -i 5' + args_u + ' context1'
        RunTest._dotest('Run', args_u , runtimes)
# testcase
#a = Perf_cpu('Testsetup_sample.xml', 'Test_parameter.xml')
#a._setup()
#a._runtest()
