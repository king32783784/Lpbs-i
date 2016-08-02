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
        srcdir = RunTest._pretesttool(self.setupxml, self.testxml, 'Perf_io', self.homepath)
        srcdir = os.path.join(srcdir, 'src/current')      
        os.chdir(srcdir)
        self._make('linux')

    def _runtest(self):
        basearg = self.baseparameter('Perf_io', self.testxml)
        print basearg
        runtimes = basearg['runtimes']
        args_itmp = basearg['i'].split(',')
        args_i = ''
        for arg in args_itmp:
            args_i = args_i + ' -i ' + arg
        args_s = basearg['s']
        args_t = basearg['t']
        args_r = basearg['r']
        cmd = "-s %s %s -t %s -r %s" % (args_s, args_i, args_t, args_r)
        print cmd
        RunTest._dotest('iozone', cmd, runtimes)
#        resulttmppath = os.path.join(self.homepath, 'resulttmp/performance/Perf_cpu/result/result.out')
#        doprocessresult = MkResult(data_cpu_aidinfo, runtimes, resulttmppath, self.result)
#        doprocessresult.mkresult()          
# testcase
#a = Perf_cpu('Testsetup_sample.xml', 'Test_parameter.xml')
#a._setup()
#a._runtest()
