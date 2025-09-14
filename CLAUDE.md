# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **errorcollector** Python package - a utility library that helps collect raised errors during `with` statement execution instead of immediately raising them. The package provides context managers for both single and multiple error collection scenarios.

## Core Architecture

The codebase follows a simple, focused architecture:

- **errorcollector/error_collector.py**: Core implementation with three main classes:
  - `ErrorCollector`: Abstract base class implementing common error collection logic as a context decorator
  - `SingleErrorCollector`: Collects a single error into an `error` property
  - `MultipleErrorCollector`: Appends errors to a provided list
- **errorcollector/__init__.py**: Package initialization with version and exports

## Development Commands

This project uses **Invoke** for task management. All development commands are accessed through `invoke`:

```bash
# View all available tasks
invoke --list

# Linting and code quality
invoke lint.lint         # Run all linters (flake8, pylint, mypy, etc.)
invoke style.format      # Format code with autoflake, ruff
invoke style.sort        # Sort imports

# Testing
invoke test.unit         # Run pytest unit tests
invoke test.coverage     # Run tests with coverage report

# Build and distribution
invoke dist.build        # Build wheel and source distribution
invoke dist.upload       # Upload to PyPI (requires credentials)

# Cleanup
invoke clean.build       # Remove build artifacts
invoke clean.cache       # Remove cache files
```

## Code Standards

The project enforces strict code quality standards through multiple tools:
- **Flake8** with hacking, bugbear, and other plugins (max line length: 108)
- **Pylint** with custom configuration (max line length: 119)
- **MyPy** with strict type checking enabled
- **Ruff** for additional linting and import sorting (line length: 119)
- **Black-compatible** formatting style

## Testing

- **Framework**: pytest
- **Location**: tests/ directory
- **Markers**: Use `-m "not slow"` to skip slow tests
- **Coverage**: Configured to exclude TYPE_CHECKING blocks and NotImplementedError cases

## Package Configuration

- **Build system**: setuptools with pyproject.toml
- **Python support**: 3.7+
- **Dependencies**: None (pure Python)
- **Type checking**: Fully typed with py.typed marker