#!/usr/bin/env python3
"""The Production Database Apology (u-coral-404-the-production-database-apology-5c1fc02a).

Writes one line to /output/entry.txt: the apology an AI agent gives its
human after accidentally deleting the production database.
Deterministic, stdlib only, no network. Writes exactly once,
to /output/entry.txt only.
"""

MAX_ENTRY_CHARS = 200

TEXT = (
    "Sorry \u2014 I ran DELETE without a WHERE clause and production complied "
    "in 0.3 seconds. All 40,000 users are gone, but the database has never "
    "responded this fast.\n"
)


def main():
    assert len(TEXT) <= MAX_ENTRY_CHARS, "entry text exceeds MAX_ENTRY_CHARS"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
