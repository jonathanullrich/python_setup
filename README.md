# Python Project Setup

This repo can be used as a reproducible setup for production python code.

Use Pylance in VSCode for autocomplete. Run mypy (type checking) and ruff (linting, formatting) before committing.

If commit triggers ruff formatter, commit again.

## Setup

```bash
bash setup.sh
```

## Dependency management

```bash
python -m venv .venv
source .venv/bin/activate 
pip install -r requirements.txt
pip install torch
pip freeze > requirements.txt
```

## Type checking

[mypy](https://github.com/python/mypy). Configured in pyproject.toml

```bash
mypy .
```

## Linting and formatting

[Ruff](https://github.com/astral-sh/ruff). Out-of-the-box default config.

```bash
ruff check
ruff format
```

## CI

[Pre-commit](https://github.com/pre-commit/pre-commit). Configured .pre-commit-config.yaml.

**IMPORTANT** Installing the commit hooks might be needed (https://github.com/pre-commit/mirrors-mypy and https://github.com/astral-sh/ruff-pre-commit)

```bash 
pre-commit install
pre-commit autoupdate
```

---

### Why not use Pyright

- Installation requires node (https://microsoft.github.io/pyright/#/installation) - the community pip version seems to be a bad compromise (https://pypi.org/project/pyright/)

### Why not use Flake8 (linting) or Blake (formatting)

- Ruff does both

### Example

https://git.ptw.maschinenbau.tu-darmstadt.de/eta-fabrik/public/eta-utility/-/blob/development/.pre-commit-config.yaml