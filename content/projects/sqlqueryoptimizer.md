---
type: project
name: queryoptimax
tags: [sql, performance, ibm-db2, python, query-optimization]
github: https://github.com/UmukoroG/QueryOptiMax
summary: SQL performance optimizer for IBM DB2 that rewrites query patterns, cutting execution time ~50% on benchmarks
---

## What it is
QueryOptiMax is a SQL performance optimizer for IBM DB2 that analyzes
query plans and rewrites patterns to improve execution time.

## What I built
- Query plan analysis and pattern-rewriting logic that cut execution time
  on benchmark workloads by roughly 50%.
- A reproducible benchmarking harness in Python for comparing query
  variants across realistic data volumes.

## Stack
Python, IBM DB2, SQL.