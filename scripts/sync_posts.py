"""
sync_posts.py — Social posts sync script for taoxee.github.io

Manages _data/social_posts.yml: validates, imports, and pretty-prints
social post entries from LinkedIn and other platforms.
No external dependencies beyond the standard library.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class LinkedInPost:
    """Represents a single LinkedIn post entry."""

    id: str          # unique identifier; auto-generated as lp-{date}-{seq} if omitted
    date: str        # ISO 8601 date: YYYY-MM-DD
    content: str     # full post text
    url: str         # original LinkedIn post URL
    tags: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class ValidationError(ValueError):
    """Raised when a post entry fails validation."""


def validate_post(data: dict, *, source: str = "<input>") -> list[str]:
    """
    Validate a raw post dict.

    Returns a list of error message strings (empty list means valid).
    Warnings (non-fatal) are printed to stderr directly.
    """
    errors: list[str] = []

    # --- required fields ---
    for field_name in ("date", "content", "url"):
        value = data.get(field_name)
        if value is None:
            errors.append(
                f"[{source}] Missing required field '{field_name}'."
            )
        elif not isinstance(value, str) or not value.strip():
            errors.append(
                f"[{source}] Required field '{field_name}' must be a non-empty string."
            )

    # --- date format ---
    date_value = data.get("date", "")
    if isinstance(date_value, str) and date_value.strip():
        if not DATE_RE.match(date_value):
            errors.append(
                f"[{source}] Field 'date' has invalid format '{date_value}'. "
                "Expected YYYY-MM-DD."
            )
        else:
            # Also verify it's a real calendar date
            try:
                datetime.strptime(date_value, "%Y-%m-%d")
            except ValueError:
                errors.append(
                    f"[{source}] Field 'date' value '{date_value}' is not a valid "
                    "calendar date."
                )

    # --- URL prefix warning (non-fatal) ---
    url_value = data.get("url", "")
    if isinstance(url_value, str) and url_value.strip():
        if not url_value.startswith("https://"):
            print(
                f"Warning [{source}]: URL '{url_value}' does not start with 'https://'. "
                "The entry will still be written.",
                file=sys.stderr,
            )

    # --- tags (optional) ---
    tags = data.get("tags")
    if tags is not None:
        if not isinstance(tags, list):
            errors.append(
                f"[{source}] Field 'tags' must be a list, got {type(tags).__name__}."
            )
        else:
            for i, tag in enumerate(tags):
                if not isinstance(tag, str) or not tag.strip():
                    errors.append(
                        f"[{source}] Tag at index {i} must be a non-empty string."
                    )

    return errors


def report_errors(errors: list[str]) -> None:
    """Print validation errors to stderr."""
    for msg in errors:
        print(f"Error: {msg}", file=sys.stderr)


# ---------------------------------------------------------------------------
# ID generation
# ---------------------------------------------------------------------------

def generate_id(date: str, existing_ids: set[str]) -> str:
    """
    Auto-generate a unique post ID in the form lp-{date}-{seq:03d}.

    Increments seq until the generated ID is not in existing_ids.
    """
    seq = 1
    while True:
        candidate = f"lp-{date}-{seq:03d}"
        if candidate not in existing_ids:
            return candidate
        seq += 1


# ---------------------------------------------------------------------------
# Post construction
# ---------------------------------------------------------------------------

def build_post(data: dict, existing_ids: set[str], *, source: str = "<input>") -> Optional[LinkedInPost]:
    """
    Validate raw dict and construct a LinkedInPost.

    Returns None (and prints errors to stderr) if validation fails.
    Auto-generates `id` when not provided.
    """
    errors = validate_post(data, source=source)
    if errors:
        report_errors(errors)
        return None

    # Resolve id
    raw_id = data.get("id", "")
    if isinstance(raw_id, str) and raw_id.strip():
        post_id = raw_id.strip()
    else:
        post_id = generate_id(data["date"], existing_ids)

    tags = [str(t).strip() for t in (data.get("tags") or []) if str(t).strip()]

    return LinkedInPost(
        id=post_id,
        date=data["date"].strip(),
        content=data["content"].strip(),
        url=data["url"].strip(),
        tags=tags,
    )


# ---------------------------------------------------------------------------
# YAML I/O  (no external dependencies — minimal hand-rolled writer)
# ---------------------------------------------------------------------------

DATA_FILE = "_data/social_posts.yml"

_FILE_HEADER = (
    "# Social posts — ordered by date descending\n"
    "# Fields: id (required), date (required), content (required),"
    " url (required), platform (required), tags (optional)\n"
    "# Platforms: linkedin, medium, twitter, etc.\n"
)


def _escape_yaml_string(value: str) -> str:
    """Return a YAML-safe double-quoted string."""
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _serialize_post(post: dict) -> str:
    """Serialize a single post dict to a YAML block entry."""
    lines: list[str] = []

    # id
    lines.append(f'- id: {_escape_yaml_string(str(post.get("id", "")))}')

    # date
    lines.append(f'  date: {_escape_yaml_string(str(post.get("date", "")))}')

    # content — use literal block scalar (|) to preserve newlines
    content = str(post.get("content", ""))
    lines.append("  content: |")
    for content_line in content.splitlines():
        lines.append(f"    {content_line}")
    # Ensure the block ends with a trailing newline (YAML literal block requirement)
    if not content.endswith("\n"):
        lines.append("")  # blank line closes the block scalar cleanly

    # url
    lines.append(f'  url: {_escape_yaml_string(str(post.get("url", "")))}')

    # tags (optional)
    tags = post.get("tags") or []
    if tags:
        lines.append("  tags:")
        for tag in tags:
            lines.append(f"    - {_escape_yaml_string(str(tag))}")

    return "\n".join(lines)


def load_data_file(path: str = DATA_FILE) -> list[dict]:
    """
    Read the YAML data file and return a list of post dicts.

    Returns an empty list if the file does not exist.
    Uses a simple line-by-line parser sufficient for the known schema.
    """
    import os

    if not os.path.exists(path):
        return []

    with open(path, encoding="utf-8") as fh:
        raw = fh.read()

    return _parse_yaml_posts(raw)


def _parse_yaml_posts(raw: str) -> list[dict]:
    """
    Minimal parser for the linkedin_posts.yml schema.

    Handles:
      - id, date, url  as plain or double-quoted scalars
      - content        as a literal block scalar (|)
      - tags           as a sequence of plain or double-quoted scalars
    """
    posts: list[dict] = []
    current: dict | None = None
    in_content = False
    content_indent = 0
    content_lines: list[str] = []
    in_tags = False

    for raw_line in raw.splitlines():
        line = raw_line.rstrip()

        # Skip comment-only lines and blank lines outside a post
        if current is None:
            stripped = line.lstrip()
            if stripped.startswith("- id:"):
                current = {}
                in_content = False
                in_tags = False
                current["id"] = _parse_scalar(stripped[len("- id:"):].strip())
            continue

        # Inside a post entry
        stripped = line.lstrip()
        indent = len(line) - len(line.lstrip())

        # Detect new top-level list item (starts a new post)
        if stripped.startswith("- id:"):
            # Save previous post
            if in_content:
                current["content"] = "\n".join(content_lines).rstrip("\n")
                in_content = False
                content_lines = []
            posts.append(current)
            current = {}
            in_tags = False
            current["id"] = _parse_scalar(stripped[len("- id:"):].strip())
            continue

        # Literal block content lines
        if in_content:
            if indent >= content_indent:
                content_lines.append(line[content_indent:])
                continue
            else:
                # Block ended
                current["content"] = "\n".join(content_lines).rstrip("\n")
                in_content = False
                content_lines = []
                in_tags = False

        # Tag list items
        if in_tags:
            if stripped.startswith("- "):
                current.setdefault("tags", []).append(
                    _parse_scalar(stripped[2:].strip())
                )
                continue
            else:
                in_tags = False

        # Key: value lines
        if ":" in stripped:
            key, _, rest = stripped.partition(":")
            key = key.strip()
            rest = rest.strip()

            if key == "date":
                current["date"] = _parse_scalar(rest)
            elif key == "content":
                if rest == "|":
                    in_content = True
                    content_indent = indent + 2
                    content_lines = []
                else:
                    current["content"] = _parse_scalar(rest)
            elif key == "url":
                current["url"] = _parse_scalar(rest)
            elif key == "tags":
                current["tags"] = []
                in_tags = True

    # Flush last post
    if current is not None:
        if in_content:
            current["content"] = "\n".join(content_lines).rstrip("\n")
        posts.append(current)

    return posts


def _parse_scalar(value: str) -> str:
    """Strip surrounding double-quotes from a YAML scalar if present."""
    if value.startswith('"') and value.endswith('"') and len(value) >= 2:
        return value[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    return value


def pretty_print(posts: list[dict]) -> str:
    """
    Serialize *posts* to a YAML string with consistent formatting.

    - Sorts entries by date descending before writing.
    - Field ordering per entry: id, date, content, url, tags.
    - 2-space indentation for post fields; 4-space for content block lines and tag items.
    - Returns the full YAML string including the file header comment.
    """
    sorted_posts = sorted(posts, key=lambda p: str(p.get("date", "")), reverse=True)

    blocks = [_FILE_HEADER]
    for post in sorted_posts:
        blocks.append(_serialize_post(post))

    return "\n".join(blocks) + "\n"


def save_data_file(path: str, posts: list[dict]) -> None:
    """
    Write the list of post dicts to *path* as YAML.

    Creates the file (and any parent directories) if it does not exist.
    Uses pretty_print() for consistent indentation and field ordering.
    """
    import os

    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(pretty_print(posts))


# ---------------------------------------------------------------------------
# CLI — add subcommand
# ---------------------------------------------------------------------------

def cmd_add(args) -> None:  # noqa: ANN001
    """Implement the `add` subcommand."""
    import json

    if args.stdin:
        raw_json = sys.stdin.read()
        try:
            data = json.loads(raw_json)
        except json.JSONDecodeError as exc:
            print(f"Error: stdin is not valid JSON: {exc}", file=sys.stderr)
            sys.exit(1)
    else:
        data = {
            "content": args.content,
            "url": args.url,
            "date": args.date,
        }
        if args.tags:
            data["tags"] = [t.strip() for t in args.tags.split(",") if t.strip()]

    # Load existing posts to collect existing IDs
    posts = load_data_file(DATA_FILE)
    existing_ids: set[str] = {str(p.get("id", "")) for p in posts}

    post = build_post(data, existing_ids)
    if post is None:
        sys.exit(1)

    # Append and save
    new_entry: dict = {
        "id": post.id,
        "date": post.date,
        "content": post.content,
        "url": post.url,
    }
    if post.tags:
        new_entry["tags"] = post.tags

    posts.append(new_entry)
    save_data_file(DATA_FILE, posts)

    print(f"\u2713 Added post {post.id} dated {post.date}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="sync_posts — manage _data/linkedin_posts.yml"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- add ---
    add_parser = subparsers.add_parser("add", help="Add a new LinkedIn post entry")
    add_parser.add_argument("--content", help="Post text content")
    add_parser.add_argument("--url", help="Original LinkedIn post URL")
    add_parser.add_argument("--date", help="Post date (YYYY-MM-DD)")
    add_parser.add_argument(
        "--tags",
        help="Comma-separated list of tags (e.g. 'AI,Career')",
        default="",
    )
    add_parser.add_argument(
        "--stdin",
        action="store_true",
        help="Read post data as JSON from stdin instead of flags",
    )

    args = parser.parse_args()

    if args.command == "add":
        cmd_add(args)


if __name__ == "__main__":
    main()
