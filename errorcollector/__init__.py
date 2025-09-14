"""Collects raised error during with statement."""

from errorcollector.error_collector import *  # noqa: F403

__version__ = "1.0.1"

__all__ = []
__all__ += error_collector.__all__  # type:ignore[name-defined] # noqa: F405 pylint: disable=undefined-variable
