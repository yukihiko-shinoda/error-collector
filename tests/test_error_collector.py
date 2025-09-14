"""Tests for error_collector.py."""

from errorcollector.error_collector import MultipleErrorCollector
from errorcollector.error_collector import SingleErrorCollector
from tests.testlibraries.error_checker import ErrorChecker
from tests.testlibraries.exceptions import ErrorForTestFrom1Error
from tests.testlibraries.exceptions import ErrorForTestFrom2Error
from tests.testlibraries.exceptions import ErrorForTestToError


class TestSingleErrorCollector:
    """Tests for Single Error Collector."""

    @staticmethod
    def test() -> None:
        """Should."""
        error_message = "test"
        error_collector = SingleErrorCollector(ErrorForTestToError, error_message)
        with error_collector:
            raise ErrorForTestFrom1Error
        error = error_collector.error
        assert error is not None
        ErrorChecker.assert_error(error, error_message, ErrorForTestToError, ErrorForTestFrom1Error)


class TestMultipleErrorCollector:
    """Tests for Multiple Error Collector."""

    @staticmethod
    def test() -> None:
        """Should."""
        error_message = "test"
        error_collector = MultipleErrorCollector(ErrorForTestToError, error_message, [])
        with error_collector:
            raise ErrorForTestFrom1Error
        with error_collector:
            raise ErrorForTestFrom2Error
        list_error = error_collector.list_error
        expected_error_count = 2
        assert len(list_error) == expected_error_count
        ErrorChecker.assert_error(list_error[0], error_message, ErrorForTestToError, ErrorForTestFrom1Error)
        ErrorChecker.assert_error(list_error[1], error_message, ErrorForTestToError, ErrorForTestFrom2Error)

    @staticmethod
    def test_no_error() -> None:
        """Should."""
        error_message = "test"
        error_collector = MultipleErrorCollector(ErrorForTestToError, error_message, [])
        with error_collector:
            pass
        list_error = error_collector.list_error
        assert len(list_error) == 0
