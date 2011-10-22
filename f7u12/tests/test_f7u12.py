import os
import unittest
from nose.plugins import PluginTester
from nose.tools import assert_equals

from f7u12 import F7U12


class F7U12Test(PluginTester):

    activate = '--with-f7u12'
    plugins = [F7U12()]
    suitepath = os.path.join(os.path.dirname(__file__), 'examples')

    def makeSuite(self):
        pass


class TestWhenEncounterinManyErrors(F7U12Test, unittest.TestCase):

    def _first_line(self, output):
        return str(output).split('\n')[0]

    def test_emits_F_for_first_seven_failures(self):
        assert_equals(7, self._first_line(self.output).count('F'))

    def test_emits_U_after_seven_failures(self):
        output = self._first_line(self.output)
        last_f = output.rfind('F')
        assert output[last_f+1:].count('U')
        assert not output[:last_f].count('U')
