"""Tests for core functionality."""

import pytest

from test_release_python import __version__, add, hello, multiply


def test_version():
    """Test that version is defined."""
    assert __version__ == "0.1.0"
    assert isinstance(__version__, str)


def test_hello():
    """Test hello function returns greeting."""
    result = hello()
    assert "Hello from test-release-python" in result
    assert __version__ in result


def test_add():
    """Test add function with various inputs."""
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(100, 200) == 300


def test_multiply():
    """Test multiply function with various inputs."""
    assert multiply(2, 3) == 6
    assert multiply(0, 100) == 0
    assert multiply(-2, 5) == -10
    assert multiply(7, 7) == 49


def test_add_with_floats():
    """Test add function with float inputs."""
    assert add(1.5, 2.5) == 4.0
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_multiply_with_floats():
    """Test multiply function with float inputs."""
    assert multiply(2.0, 3.0) == 6.0
    assert multiply(0.5, 4) == 2.0
