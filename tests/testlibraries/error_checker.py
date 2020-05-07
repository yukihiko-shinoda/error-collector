"""This module implements error checker."""


class ErrorChecker:
    @staticmethod
    def assert_error(error, error_message, error_class_to, error_class_from):
        assert type(error) is error_class_to
        assert type(error.__cause__) is error_class_from
        assert str(error) is error_message
