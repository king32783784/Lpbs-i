import os
import time
from preparetest import TestParpare
from public import ReadPublicinfo
from testsetup import TestSetup
from parameter import ParameterAnalysis
from subprocess import call, PIPE, Popen


class RunTest(TestSetup, ParameterAnalysis):
    
    @staticmethod
    def _depend(*args):
        defectlist = TestParpare.baseddependency(*args)
        if len(defectlist) > 0:
            self.packageinstall(defectlist)

    @staticmethod
    def _pretesttool(setupxml, testxml, testitem, homepath):
        print setupxml
        setinfo = ReadPublicinfo(setupxml, testxml)
        url = setinfo.setupinfo['xml_dict']['testtoolurl'][0]
        testitemargs = ParameterAnalysis.baseparameter(testitem, testxml)
        tarname = testitemargs['tarbal']
        setup = TestSetup()
        tarfilepath = setup.testtooldownload(url, tarname, homepath)
        testbindir = setup.decompressfile(tarfilepath, testitem, homepath)
        return testbindir
                        

    def testresult(self):
        pass

 
    def stbmonitor(self):
        pass

    def exception(self):
        pass

    @staticmethod
    def _dotest(executable, cmd, runtimes):
        homedir = os.getcwd()
        for root, dirs, files in os.walk(homedir):
            if executable in files:
                executable = os.path.join(root, executable)
                break
        cmds = [executable, cmd]
        finalcmd = os.path.join(' ', ' '.join(cmds))
        print finalcmd
        for runonce in range(int(runtimes)):
            test = Popen(finalcmd, stdout=PIPE, shell=True)
            stdout = test.communicate()[0]
            print stdout

#RunTest._pretesttool('Testsetup_sample.xml', 'Test_parameter.xml', 'Perf_cpu')
