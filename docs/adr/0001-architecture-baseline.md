# ADR-0001: Architecture Baseline

**Status:** Accepted  
**Date:** 2026-03-04  

## Context
We need a portfolio-grade system that demonstrates:
- strong separation of concerns
- testable, governable changes
- minimal surface area for mistakes

## Decision
We adopt a 3-layer architecture:

1) **core/** — source of truth  
- all routing logic
- all schemas + validation
- tests live here or reference here

2) **api/** — thin HTTP wrapper  
- request parsing
- calls core
- formats response

3) **ts-client/** — consumer-only  
- typed models
- examples
- never a decider

## Consequences
- API remains stable while core evolves safely
- governance and auditability are visible in public proof
- contributors have a clear rule-set