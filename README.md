# manta-json

JSON validator and formatter — pretty-print, validate, and minify JSON from the command line.

Part of the [Manta](https://github.com/jrbobbyhansen-pixel) collection of zero-dependency Python CLI tools.

## Installation

```bash
pip install manta-json
```

Or run directly:

```bash
python -m manta_json --help
```

## Usage

```bash
# Validate JSON
echo '{"name": "Manta"}' | manta-json validate

# Pretty-print JSON
echo '{"name":"Manta","version":1}' | manta-json pretty

# Pretty-print with custom indent
echo '{"a":1}' | manta-json pretty --indent 4

# Minify JSON
echo '{
  "name": "Manta"
}' | manta-json minify
```

## Commands

| Command    | Description                          |
|------------|--------------------------------------|
| `validate` | Check if JSON is valid (exit code)   |
| `pretty`   | Pretty-print JSON with indentation   |
| `minify`   | Remove all unnecessary whitespace    |

## API

```python
from manta_json import validate, pretty_print, minify

validate('{"key": "value"}')  # => True
pretty_print('{"a":1}')       # => '{\n  "a": 1\n}'
minify('{\n  "a": 1\n}')    # => '{"a":1}'
```

## License

MIT — see [LICENSE](LICENSE).
