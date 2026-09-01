# tests/test_version.py
from scripts.bump_version import bump_patch


def test_patch_version_bump():
    assert bump_patch("0.1.0") == "0.1.1"


def test_patch_carry_is_numeric():
    assert bump_patch("2.7.9") == "2.7.10"
