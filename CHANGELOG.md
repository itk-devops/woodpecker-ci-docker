# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2025-02-24

- Split agent config in separate compose file to enable running agents only
- Expose gRPC over HTTPS to enable running agents on a different provider (zone)
- Add zone label to enable scoping to the provider they run on
- Enable setting docker image tag in env

## [1.0.0] - 2024-11-07

- Initial release