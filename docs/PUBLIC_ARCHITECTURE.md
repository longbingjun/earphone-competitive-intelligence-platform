# Public engineering architecture

This repository demonstrates the engineering structure behind a competitive-intelligence data product without publishing the original company repository, its history, deployment runbooks, or production data.

```text
Public source adapter
        |
        v
Evidence-preserving extraction
  rules + optional text model
        |
        v
Normalization and validation
product / component / supplier / evidence
        |
        +--> PostgreSQL-compatible relational layer
        +--> S3-compatible object-storage layer
        |
        v
API + scheduled worker + static web export
```

## Repository boundaries

- `core/`: parsing, extraction, normalization and analytical transformations.
- `server/`: API, persistence abstractions, background jobs and schema migrations.
- `web/`: Astro/React data-product interface.
- `scripts/`: repeatable ETL, evaluation and release-validation commands.
- `tests/`: unit and integration tests using local or synthetic fixtures.
- `data/`: empty public manifests only; no historical or production content.

## Deliberately excluded

- GitLab history, merge-request references and employee identities.
- Internal hostnames, IP addresses, ports, database paths and backup locations.
- Production deployment and rollback runbooks.
- API keys, cookies and organization-specific environment-variable names.
- Crawled article text, video metadata, source images and model caches.
- Human-review worksheets and company-specific taxonomy decisions.

The interactive, sanitized portfolio is maintained separately in `headphone-component-intelligence`.
