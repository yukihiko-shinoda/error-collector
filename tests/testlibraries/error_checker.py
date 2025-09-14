"""This module implements error checker."""

from __future__ import annotations


class ErrorChecker:
    """This class implements error checker."""

    @staticmethod
    def assert_error(
        error: Exception,
        error_message: str,
        error_class_to: type[Exception],
        error_class_from: type[Exception],
    ) -> None:
        """Checks error properties."""
        # Reason: Using type() is required to check perfectly same class. pylint: disable=unidiomatic-typecheck
        assert type(error) is error_class_to
        # Reason: Using type() is required to check perfectly same class. pylint: disable=unidiomatic-typecheck
        assert type(error.__cause__) is error_class_from
        assert str(error) is error_message
