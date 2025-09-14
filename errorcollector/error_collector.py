"""This module implements error collector."""

from __future__ import annotations

from abc import abstractmethod
from contextlib import ContextDecorator
from typing import TYPE_CHECKING
from typing import Generic
from typing import TypeVar

if TYPE_CHECKING:
    from types import TracebackType

__all__ = ["MultipleErrorCollector", "SingleErrorCollector"]

TypeVarError = TypeVar("TypeVarError", bound=Exception)


class ErrorCollector(ContextDecorator, Generic[TypeVarError]):
    """This class implements base methods of error collector."""

    def __init__(self, error_class: type[TypeVarError], message: str) -> None:
        self.error_class = error_class
        self.message = message

    def __enter__(self) -> ErrorCollector[TypeVarError]:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool:
        if exc_value is None:
            return False

        try:
            self.raise_as_error_class(exc_value)
        except self.error_class as error:
            self.collect(error)
        return True

    def raise_as_error_class(self, exc_value: BaseException) -> None:
        raise self.error_class(self.message) from exc_value

    @abstractmethod
    def collect(self, error: TypeVarError) -> None:
        """This method collects error into property."""


class SingleErrorCollector(ErrorCollector[TypeVarError]):
    """This class implements error collector for single error."""

    def __init__(self, error_class: type[TypeVarError], message: str) -> None:
        super().__init__(error_class, message)
        self.error: TypeVarError | None = None

    def collect(self, error: TypeVarError) -> None:
        self.error = error


class MultipleErrorCollector(ErrorCollector[TypeVarError]):
    """This class implements error collector for multiple error."""

    def __init__(self, error_class: type[TypeVarError], message: str, list_error: list[TypeVarError]) -> None:
        super().__init__(error_class, message)
        self.list_error = list_error

    def collect(self, error: TypeVarError) -> None:
        self.list_error.append(error)
