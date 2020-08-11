# Error Collector

[![Test](https://github.com/yukihiko-shinoda/error-collector/workflows/Test/badge.svg)](https://github.com/yukihiko-shinoda/error-collector/actions?query=workflow%3ATest)
[![Test Coverage](https://api.codeclimate.com/v1/badges/f954efad2003fe046369/test_coverage)](https://codeclimate.com/github/yukihiko-shinoda/error-collector/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/f954efad2003fe046369/maintainability)](https://codeclimate.com/github/yukihiko-shinoda/error-collector/maintainability)
[![Code Climate technical debt](https://img.shields.io/codeclimate/tech-debt/yukihiko-shinoda/error-collector)](https://codeclimate.com/github/yukihiko-shinoda/error-collector)
[![Updates](https://pyup.io/repos/github/yukihiko-shinoda/error-collector/shield.svg)](https://pyup.io/repos/github/yukihiko-shinoda/error-collector/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/errorcollector)](https://pypi.org/project/errorcollector/)
[![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fyukihiko-shinoda%2Ferror-collector)](http://twitter.com/share?text=Error%20Collector&url=https://pypi.org/project/errorcollector/&hashtags=python)

Collects raised error during with statement.

## Features

In some cases we don't want to raise an error immediately.
For example, case when return error HTTP response to client
after validating whole HTTP POST data.

This package helps to collect error.

## Installation

```console
pip install errorcollector
```

## Usage

### MultipleErrorCollector

Let's say, there are data model which has single property.
Before process this data model, we want to validate property.

Ex:

```python
from yourproduct.exceptions import ConvertError


class PostDataModel:
    def __init__(self, property_a_string: str, property_b_string: str):
        self._property_a_string = property_a_string
        self._property_b_string = property_b_string
        self.list_error = None

    def validate(self) -> bool:
        self.stock_convert_error(
            lambda: self.property_a_int,
            f"Property string A couldn't be converted to integer. Property string = {self._property_a_string}"
        )
        self.stock_convert_error(
            lambda: self.property_b_int,
            f"Property string B couldn't be converted to integer. Property string = {self._property_b_string}"
        )
        return bool(self.list_error)

    def stock_convert_error(self, method: Callable[[], Any], message: str) -> None:
        with MultipleErrorCollector(ConvertError, message, self.list_error):
            return method()

    @property
    def property_a_int() -> int:
        """May raise ValueError"""
        return int(self._property_a_string)

    @property
    def property_b_int() -> int:
        """May raise ValueError"""
        return int(self._property_b_string)
```

When we call method `validate()`, even if `ValueError` occurs,
the exception is not raised and execution does not stop.

When `method()` in method `stock_convert_error()` raises `ValueError`,
`ConvertError` which is set raised `ValueError` into `__cause__` is set
into property `self.list_error`.

We can check details of error after validate.

### SingleErrorCollector

This is single version of Error Collector.
This may be useful in case when need to handle
multiple cases and singular cases in an integrated method by polymorphism.

Ex:

```python
from yourproduct.exceptions import ConvertError


class PostDataModel:
    def __init__(self, property_string: str):
        self._property_string = property_string
        self.convert_error = None

    def validate(self) -> bool:
        self.stock_convert_error(
            lambda: self.property_int,
            f"Property string couldn't be converted to integer. Property string = {self._property_string}"
        )
        return self.convert_error is not None

    def stock_convert_error(self, method: Callable[[], Any], message: str) -> None:
        error_collector = SingleErrorCollector(ConvertError, message)
        with error_collector:
            method()
        self.convert_error = error_collector.error

    @property
    def property_int() -> int:
        """May raise ValueError"""
        return int(self._property_string)
```
