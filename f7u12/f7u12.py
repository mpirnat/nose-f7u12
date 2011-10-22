import logging
import os

from nose.exc import SkipTest
from nose.plugins import Plugin
from unittest import TestResult, _TextTestResult

log = logging.getLogger('nose.plugins.f7u12')


class F7U12(Plugin):

    name = 'f7u12'
    enabled = True

    def options(self, parser, env=os.environ):
        super(F7U12, self).options(parser, env=env)

    def configure(self, options, config):
        super(F7U12, self).configure(options, config)
        self.config = config
        if not self.enabled:
            return

    def prepareTestResult(self, result):
        # This will break when unittest changes.
        # Current code is from 2.6

        our_result = F7U12Result(
                self.runner.stream,
                self.runner.descriptions,
                self.runner.verbosity,
                stopOnError=self.config.stopOnError)

        # Monkey patch unittest result with a custom result.
        # This is because Nose cannot completely replace the
        # unittest result.  Without this we can replace a few things.
        for fn in our_result.__class__.__dict__:
            setattr(result, fn, getattr(our_result, fn))

        # Reference some attributes so that summaries work:
        for a in ('failures', 'errors', 'testsRun', 'shouldStop'):
            setattr(our_result, a, getattr(result, a))

        # Tell other plugins that it's probably not safe to
        # do their own monkeypatching.
        self.result = result
        return result

    def prepareTestRunner(self, runner):
        self.runner = runner

    def begin(self):
        self.failure_count = 0

    def handleFailure(self, test, err):
        self.failure_count += 1

        if self.failure_count < 8:
            self.stream.write('F')
        else:
            self.stream.write('U')

        self.result.addFailure(test, err)

        if not self.result.wasSuccessful() and self.config.stopOnError:
            self.shouldStop = True
        return True

    def setOutputStream(self, stream):
        self.stream = stream


class F7U12Result(_TextTestResult):

    def __init__(self, stream, descriptions, verbosity, stopOnError=False):
        super(F7U12Result, self).__init__(stream, descriptions, verbosity)
        self.stopOnError = stopOnError

    def addFailure(self, test, err):
        TestResult.addFailure(self, test, err)
