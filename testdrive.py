'''
   Implementation test drive
'''
import os
import shutil
import sys
import logging
from initdaemon import Daemon
from public import ReadPublicinfo
from runtest import RunTest
from preparetest import TestParpare
from logging_config import *


class TestDrive(Daemon, ReadPublicinfo, TestParpare):
    logger = logging.getLogger('client')
    homepath = os.getcwd()

    def __init__(self, setupxml, testxml):
        ReadPublicinfo.__init__(self, setupxml, testxml)
        Daemon.__init__(self)
        self.setupxml = setupxml
        self.testxml = testxml

    def testselect(self):
        self.logger.info('default test start')
        self._runtest()

    def mktestdir(self, pertesttype, pertest):
        dirtypes = ['result', 'debug']
        dirlist = {}
        localpath = os.path.join(self.homepath, 'resulttmp/')
        for pertype in dirtypes:
            dirpath = self.mkdirectory(localpath, '/',
                                       pertesttype, pertest,
                                       pertype)
            dirlist[pertype] = dirpath
            self.logger.info(dirlist)
        return dirlist

    def _runtest(self):
        testlist = self.dotestlist
        finalresultpath = os.path.join(self.homepath, 'finalresult')
        finalresultdir = self.mkdirectory(finalresultpath, '/')
        print finalresultdir
        self.logger.info("This time test list is %s" % testlist)
        for pertesttype in testlist:
            for pertest in testlist[pertesttype]:
                pathlist = self.mktestdir(pertesttype, pertest)
                Logging_Config.setlogger(pertest, '%s/setup.out' % pathlist['debug'])
                stdout_logger = logging.getLogger(pertest)
                setup = StreamToLogger(stdout_logger, logging.INFO)
                sys.stdout = setup
                job = __import__('%s' % pertest)
                runjob = job.DoTest(self.setupxml, self.testxml, self.homepath, finalresultdir )
                runjob._setup()
                Logging_Config.setlogger(pertest, '%s/result.out' % pathlist['result'])
                stdout_logger = logging.getLogger(pertest)
                test = StreamToLogger(stdout_logger, logging.INFO)
                sys.stdout = test
                runjob._runtest()

    def _run(self):
        self.logger.info('test start')
        self.testselect()


# testcase
# case1
# test = TestDrive('Testsetup_sample.xml', 'Test_parameter.xml')
# test._run()
# test='Perf_cpu'
# job = __import__('%s' % test)
