# PulsHealth for Home Assistant

Read README.md before editing. This repository owns only the Home Assistant
client; API and OAuth server changes belong to PulsHealth/pulshealth.

Use a task branch and PR, signed-off commits, and the checks below. Preserve
the pulshealth domain, config entry compatibility, unique IDs and entity IDs.
Never log credentials, user identifiers or health payloads. Never use real
health data in tests. Missing data must remain unknown, not zero.

With Python 3.14: `pip install -r requirements-test.txt`, then
`ruff check custom_components tests`, `ruff format --check custom_components tests`
and `pytest -q`. CI is in .github/workflows/ci.yml.

Keep manifest version, release tag and HACS packaging consistent. Releases
are separate from merges. Server credentials and home-infrastructure details
must never enter this public repository.
