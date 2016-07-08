'''
    sysbench: System evaluation benchmark
    test: Perf_cpu Perf_mem Perf_mysql
'''
import os
from runtest import RunTest
from pretreatment_result import MkResult


data_cpu_aidinfo = {
    "search_path": "execution time \(avg\/stddev\):(.*?)\/0.00",
    "chart_title": ('CPU Execution time (sec)'),
    "subjects": ('10000', '20000', '30000'),
    "itemname" : "sysbench_cpu",
}


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
        RunTest._depend('gcc', 'make', 'automake', 'libtool')
        srcdir = RunTest._pretesttool(self.setupxml, self.testxml, 'Perf_cpu', self.homepath)
        
        os.chdir(srcdir)
        self._configure('--without-mysql')
        self._make('LIBTOOL=/usr/bin/libtool')

    def _runtest(self):
        basearg = self.baseparameter('Perf_cpu', self.testxml)
        print basearg
        runtimes = basearg['runtimes']
        cpu_max_prime=basearg['cpu_max_prime'].split(',')
        for max_prime in cpu_max_prime:
            cmd = "--test=%s --cpu-max-prime=%s run" % (basearg['test_type'], max_prime)
            RunTest._dotest('sysbench', cmd, runtimes)
        resulttmppath = os.path.join(self.homepath, 'resulttmp/performance/Perf_cpu/result/result.out')
        doprocessresult = MkResult(data_cpu_aidinfo, runtimes, resulttmppath, self.result)
        doprocessresult.mkresult()          
# testcase
#a = Perf_cpu('Testsetup_sample.xml', 'Test_parameter.xml')
#a._setup()
#a._runtest()
