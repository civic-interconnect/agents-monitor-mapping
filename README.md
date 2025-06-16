# agents-mapping-assistant

> Mapping Assistant Agent for Civic Interconnect 

[![Version](https://img.shields.io/badge/version-v0.1.0-blue)](https://github.com/civic-interconnect/agents-mapping-assistant/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/civic-interconnect/agents-mapping-assistant/actions/workflows/agent-runner.yml/badge.svg)](https://github.com/civic-interconnect/agents-mapping-assistant/actions)

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
py -m pip install --upgrade -r requirements.txt --timeout 100
py main.py
```

## Deployment

This agent is scheduled to run automatically using GitHub Actions.

## Before Starting Changes

```shell
git pull
```

## After Tested Changes (New Version Release)

```shell
git add .
git commit -m "Release: agents-mapping-assistant v0.1.0"
git push origin main
git tag v0.1.0
git push origin v0.1.0
```
