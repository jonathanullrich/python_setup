# Python Production Project Setup

This repo can be used as a reproducible setup for production python code.

Use Pylance in VSCode for autocomplete. Use mypy for type checking as part of the CI process

## Development setup

In VSCode install the python extension - it comes with Pylance for Intellisense.

## Dependency management

```bash
python -m venv .venv
source .venv/bin/activate 
pip install -r requirements.txt
pip install torch
pip freeze > requirements.txt
```

## Type checking

[mypy](https://github.com/python/mypy)

```bash
mypy .
```

## Linting and formatting

[Ruff](https://github.com/astral-sh/ruff)

```bash
ruff check
ruff format
```

## CI
[Pre-commit](https://github.com/pre-commit/pre-commit)

### Why not use Pyright

- installation requires node (https://microsoft.github.io/pyright/#/installation) - the community pip version seems like a bad compromise (https://pypi.org/project/pyright/)