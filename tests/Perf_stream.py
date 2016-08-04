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
        srcdir = RunTest._pretesttool(self.setupxml, self.testxml, 'Perf_stream', self.homepath)
        os.chdir(srcdir)
        self._make(' ')

    def _runtest(self):
        basearg = self.baseparameter('Perf_stream', self.testxml)
        print basearg
        threads = basearg['thread'].split(',')
        runtimes = basearg['runtimes']
        for thread in threads:
            RunTest._dotest('stream_test', thread, runtimes)
