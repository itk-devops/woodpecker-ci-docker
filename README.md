# Woodpecker CI Docker Compose Setup

ITK docker setup for Woodpecker CI

## Setup

This setup provides a collection of docker compose files to enable running Woodpecker server and agents either pooled
in same install or individually across different machines.

## Environment variables

At a minimum you should set the following or validate thhat the default works for you

```dotenv
COMPOSE_DOMAIN=woodpecker.local.itkdev.dk
COMPOSE_TAG=latest

WOODPECKER_DATABASE_DATASOURCE='db:db@tcp(mariadb:3306)/db?parseTime=true'

WOODPECKER_SERVER=woodpecker:9000
WOODPECKER_GITHUB_CLIENT=CHANGEME
WOODPECKER_GITHUB_SECRET=CHANGEME
WOODPECKER_AGENT_SECRET=CHANGEME
WOODPECKER_AGENT_LABELS=zone=CHANGEME

WOODPECKER_ADMIN=
WOODPECKER_ORGS=itk-dev

WOODPECKER_DEFAULT_CANCEL_PREVIOUS_PIPELINE_EVENTS=''
WOODPECKER_PROMETHEUS_AUTH_TOKEN=CHANGEME
WOODPECKER_METRICS_SERVER_ADDR=:8100
```
