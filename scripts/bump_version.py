# scripts/bump_version.py
from pathlib import Path

VERSION_FILE = Path("VERSION")
CHANGELOG_FILE = Path("CHANGELOG.md")


def bump_patch(version: str) -> str:
    major, minor, patch = map(int, version.strip().split("."))
    return f"{major}.{minor}.{patch + 1}"


def main() -> None:
    old_version = VERSION_FILE.read_text().strip()
    new_version = bump_patch(old_version)
    VERSION_FILE.write_text(new_version + "\n")
    changelog = CHANGELOG_FILE.read_text()
    entry = (
        f"\n## v{new_version}\n"
        "- Automated release preparation.\n"
        "- CI validation required before merge.\n"
    )
    CHANGELOG_FILE.write_text(changelog.rstrip() + "\n" + entry)
    print(f"Bumped version: {old_version} -> {new_version}")


if __name__ == "__main__":
    main()
