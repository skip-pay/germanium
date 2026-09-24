"""
Provides unittest and Django test case assert functions
"""

import unittest
from contextlib import contextmanager

from germanium import config


class _AssertionsTestCase(unittest.TestCase):
    def runTest(self):
        pass


# assert* methods of unittest.TestCase under pep8 names, bound to one shared instance so maxDiff applies to all of them
_test_case = _AssertionsTestCase()

assert_equal = _test_case.assertEqual
assert_true = _test_case.assertTrue
assert_false = _test_case.assertFalse
assert_in = _test_case.assertIn
assert_not_in = _test_case.assertNotIn
assert_raises = _test_case.assertRaises
assert_not_equal = _test_case.assertNotEqual
assert_is = _test_case.assertIs
assert_is_instance = _test_case.assertIsInstance
assert_greater = _test_case.assertGreater
assert_less = _test_case.assertLess
assert_almost_equal = _test_case.assertAlmostEqual
assert_not_almost_equal = _test_case.assertNotAlmostEqual
assert_greater_equal = _test_case.assertGreaterEqual
assert_less_equal = _test_case.assertLessEqual
assert_not_is_instance = _test_case.assertNotIsInstance
assert_list_equal = _test_case.assertListEqual
assert_tuple_equal = _test_case.assertTupleEqual
assert_set_equal = _test_case.assertSetEqual
assert_dict_equal = _test_case.assertDictEqual
assert_sequence_equal = _test_case.assertSequenceEqual
assert_multi_line_equal = _test_case.assertMultiLineEqual
assert_is_none = _test_case.assertIsNone
assert_is_not_none = _test_case.assertIsNotNone
assert_logs = _test_case.assertLogs
assert_regex = _test_case.assertRegex
assert_not_regex = _test_case.assertNotRegex


if config.TURN_OFF_MAX_DIFF:
    assert_equal.__self__.maxDiff = None


def fail(msg=None):
    raise AssertionError(msg)


@contextmanager
def assert_not_raises(exc_type, func=None, *args, **kwargs):
    try:
        if func:
            func(*args, **kwargs)
        yield None
    except exc_type:
        raise fail("{} raised".format(exc_type.__name__))


def assert_length_equal(iterable, expected_length, msg=None):
    assert_equal(len(iterable), expected_length, msg)


class AllEqual:
    def __eq__(self, obj):
        return True


class NotNoneEqual:
    def __eq__(self, obj):
        return obj is not None


all_eq_obj = AllEqual()
not_none_eq_obj = NotNoneEqual()
