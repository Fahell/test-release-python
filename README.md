# Test Release Python

Test project for validating agent-release global tool with Python projects.

## Installation

```bash
pip install -e ".[dev]"
```

## Usage

```python
from test_release_python import hello, add

hello()  # Prints: Hello from test-release-python v0.1.0
result = add(2, 3)  # Returns: 5
```

## Development

```bash
# Run linter
ruff check .

# Run tests
pytest

# Run tests with coverage
pytest --cov=test_release_python
```

## Release

This project uses `agent-release` for automated releases:

```bash
release 0.1.0
```

## License

MIT
