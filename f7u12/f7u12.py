import logging
import os

from nose.plugins import Plugin

log = logging.getLogger('nose.plugins.f7u12')


class F7U12(Plugin):

    name = 'f7u12'

    def options(self, parser, env=os.environ):
        super(F7U12, self).options(parser, env=env)

    def configure(self, options, conf):
        super(F7U12, self).configure(options, conf)
        if not self.enabled:
            return
        
        self.config = config


    def finalize(self, result):
        log.info("Hello plugin world!")
