"""JSON validator and formatter — pretty-print, validate, and minify."""

import argparse
import json
import sys
from typing import List, Optional


def load_json(data: str) -> object:
    """Parse JSON string, exiting on error."""
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        print(f"error: invalid JSON — {e}", file=sys.stderr)
        sys.exit(1)


def validate(data: str) -> bool:
    """Validate JSON string. Returns True if valid."""
    try:
        json.loads(data)
        return True
    except json.JSONDecodeError:
        return False


def pretty_print(data: str, indent: int = 2) -> str:
    """Pretty-print JSON string."""
    obj = load_json(data)
    return json.dumps(obj, indent=indent, sort_keys=True) + "\n"


def minify(data: str) -> str:
    """Minify JSON string (remove all whitespace)."""
    obj = load_json(data)
    return json.dumps(obj, separators=(",", ":")) + "\n"


def main(argv: Optional[List[str]] = None) -> None:
    parser = argparse.ArgumentParser(
        description="JSON validator and formatter — pretty-print, validate, and minify.",
        epilog="Example: echo '{"a":1}' | manta-json pretty",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate", help="Check if JSON is valid")
    p_pretty = sub.add_parser("pretty", help="Pretty-print JSON")
    p_pretty.add_argument("-i", "--indent", type=int, default=2, help="Indent size (default: 2)")
    sub.add_parser("minify", help="Minify JSON (remove whitespace)")

    args = parser.parse_args(argv)

    data = sys.stdin.read()

    if args.command == "validate":
        if validate(data):
            print("valid JSON")
            sys.exit(0)
        else:
            print("invalid JSON", file=sys.stderr)
            sys.exit(1)
    elif args.command == "pretty":
        indent = getattr(args, "indent", 2)
        sys.stdout.write(pretty_print(data, indent))
    elif args.command == "minify":
        sys.stdout.write(minify(data))


if __name__ == "__main__":
    main()
