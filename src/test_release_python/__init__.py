"""Test Release Python - A sample project for agent-release testing."""

__version__ = "0.1.0"


def hello():
    """Print a greeting message with version."""
    print(f"Hello from test-release-python v{__version__}")
    return f"Hello from test-release-python v{__version__}"


def add(a, b):
    """Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    return a + b


def multiply(a, b):
    """Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of a and b
    """
    return a * b
