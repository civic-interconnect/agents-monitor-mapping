# agents-monitor-mapping

> Mapping Assistant Agent for Civic Interconnect

[![Version](https://img.shields.io/badge/version-v0.2.0-blue)](https://github.com/civic-interconnect/agents-monitor-mapping/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/civic-interconnect/agents-monitor-mapping/actions/workflows/agent-runner.yml/badge.svg)](https://github.com/civic-interconnect/agents-monitor-mapping/actions)

This agent creates mapping tables between OCD Divisions and OpenStates jurisdictions.

## Current Status

- OCD Divisions fully pulled daily.
- OpenStates mapping scaffolding under construction.
- Early mapping files begin with `mapping/ocd-to-openstates.csv`.


## Local development

Requires Git Large File Support (LFS).

```powershell
git lfs install
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel --prefer-binary
py -m pip install --upgrade -r requirements-dev.txt --timeout 100 --no-cache-dir
pre-commit install
py main.py
```

## Deployment

This agent is scheduled to run automatically using GitHub Actions.

## Before Starting Changes

```shell
git pull
```

## After Tested Changes (New Version Release)

First: Update these files to the new version:

1. VERSION file
2. README.md (update version badge)

Then run the following:

```shell
pre-commit autoupdate --repo https://github.com/pre-commit/pre-commit-hooks
ruff check . --fix
git add .
git commit -m "Release: v0.2.0 w/civic-lib v0.9.0"
git push origin main
git tag v0.2.0
git push origin v0.2.0
```
