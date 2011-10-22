import nose


class TestGeneratesLotsOfFailures(object):

    def test_generates_failures(self):

        def _make_a_test(i):
            # start with some wins
            if i < 7:
                assert True

            # but then it hits the fan...
            elif i < 30:
                assert False

            # then be a little random
            elif i % 3 == 0:
                assert False
            else:
                assert True

        for i in range(50):
            yield _make_a_test, i
