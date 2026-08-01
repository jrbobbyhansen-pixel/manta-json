"""Tests for manta-json."""

from manta_json import validate, pretty_print, minify


def test_validate_valid():
    assert validate('{"a": 1, "b": 2}')


def test_validate_invalid():
    assert not validate('{invalid}')


def test_validate_empty_object():
    assert validate("{}")


def test_validate_array():
    assert validate("[1, 2, 3]")


def test_pretty_print():
    result = pretty_print('{"a":1,"b":2}')
    assert '"a": 1' in result
    assert '"b": 2' in result
    assert "\n" in result


def test_pretty_print_indent():
    result = pretty_print('{"a":1}', indent=4)
    assert "    " in result


def test_minify():
    result = minify('{\n  "a": 1,\n  "b": 2\n}')
    assert " " not in result
    assert "\n" not in result
    assert '{"a":1,"b":2}' in result


def test_minify_nested():
    result = minify('{"a": {"b": [1, 2]}}')
    assert " " not in result
    assert '{"a":{"b":[1,2]}}' in result
