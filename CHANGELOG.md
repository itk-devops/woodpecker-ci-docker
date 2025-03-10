# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.2] - 2025-03-10

- Fix traefik labels for exposing agent endpoint 

## [1.1.1] - 2025-03-04

- Remove redundant env section from agent compose file
- Set default empty value for ext config endpoint

## [1.1.0] - 2025-02-25

- Split agent config in separate compose file to enable running agents only
- Expose gRPC over HTTPS to enable running agents on a different provider (zone)
- Add zone label to enable scoping to the provider they run on
- Enable setting docker image tag in env

## [1.0.0] - 2024-11-07

- Initial release