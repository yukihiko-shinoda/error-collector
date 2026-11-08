# SPDX-FileCopyrightText: Copyright (c) 2020 Yukihiko Shinoda
# SPDX-License-Identifier: MIT
"""Collects raised error during with statement."""

from errorcollector.error_collector import *  # noqa: F403

__version__ = "1.1.0"

__all__ = []
__all__ += error_collector.__all__  # type:ignore[name-defined] # noqa: F405 pylint: disable=undefined-variable
