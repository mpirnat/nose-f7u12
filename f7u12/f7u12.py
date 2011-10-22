import logging
import os

from nose.plugins import Plugin

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

    def begin(self):
        self.failure_count = 0

    def handleFailure(self, test, err):
        self.failure_count += 1

        if self.failure_count < 8:
            self.stream.write('F')
        else:
            self.stream.write('U')
        return True

    def setOutputStream(self, stream):
        self.stream = stream
        return self.stream

