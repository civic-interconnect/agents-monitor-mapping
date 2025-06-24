# agents-monitor-mapping

> Mapping Assistant Agent for Civic Interconnect

[![Version](https://img.shields.io/badge/version-v0.2.2-blue)](https://github.com/civic-interconnect/agents-monitor-mapping/releases)
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

## Local Development

See [REF_DEV.md](./REF_DEV.md). Then:

```shell
py main.py
```
