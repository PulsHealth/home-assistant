"""The independent repository remains installable by HACS."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_package_metadata():
    manifest = json.loads((ROOT / "custom_components/pulshealth/manifest.json").read_text())
    hacs = json.loads((ROOT / "hacs.json").read_text())
    assert manifest["domain"] == "pulshealth"
    assert manifest["documentation"] == "https://github.com/PulsHealth/home-assistant"
    assert manifest["issue_tracker"] == manifest["documentation"] + "/issues"
    assert manifest["version"]
    assert hacs["homeassistant"] == "2026.10.0"
    assert (ROOT / "LICENSE").is_file()
    assert (ROOT / "custom_components/pulshealth/brand/icon.png").is_file()
