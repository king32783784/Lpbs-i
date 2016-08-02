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
        RunTest._depend('gcc', 'make') 
        srcdir = RunTest._pretesttool(self.setupxml, self.testxml, 'Perf_thread', self.homepath)
        os.chdir(srcdir)

    def _runtest(self):
        basearg = self.baseparameter('Perf_thread', self.testxml)
        print basearg
        runtimes = basearg['runtimes']
        args_itmp = basearg['games'].split(',')
        args_games = ''
        for arg in args_itmp:
            args_games = args_games + ' %s ' % arg
        print args_games
        RunTest._dotest('RunTest.sh', args_games, runtimes)
# testcase
#a = Perf_cpu('Testsetup_sample.xml', 'Test_parameter.xml')
#a._setup()
#a._runtest()
