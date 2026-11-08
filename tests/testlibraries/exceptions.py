# SPDX-FileCopyrightText: Copyright (c) 2020 Yukihiko Shinoda
# SPDX-License-Identifier: MIT
"""This module implements exceptions for this package."""


class Error(Exception):
    """Base class for exceptions in this module.

    @see https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions
    """


class ErrorForTestFrom1Error(Error):
    """This error is used only for test."""


class ErrorForTestFrom2Error(Error):
    """This error is used only for test."""


class ErrorForTestToError(Error):
    """This error is used only for test."""
