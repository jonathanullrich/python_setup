#!/bin/bash

# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Install pre-commit hooks
pre-commit install

# Update pre-commit hooks
pre-commit autoupdate