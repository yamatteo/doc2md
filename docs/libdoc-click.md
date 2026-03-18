---
title: "Click Documentation"
package_name: "click"
version: ">=8.0"
source: "https://click.palletsprojects.com/"
last_updated: "2026-03-18 17:30:00"
description: "Click is a Python package for creating beautiful command line interfaces in a composable way."
---

# Click

Click is a Python package for creating beautiful command line interfaces in a composable way.

## Version Information
- **Installed Version**: `>=8.0`
- **Documentation Source**: https://click.palletsprojects.com/
- **Last Updated**: 2026-03-18 17:30:00

## Key Features
- Arbitrary nesting of commands
- Automatic help page generation
- Supports lazy loading of subcommands
- Simple and intuitive API
- Extensive customization options
- Type hints support
- Testing utilities included

## Installation
```bash
pip install click>=8.0
```

## Basic Usage
```python
import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f'Hello {name}!')

if __name__ == '__main__':
    hello()
```

## Additional Resources
- [Official Documentation](https://click.palletsprojects.com/)
- [PyPI Package](https://pypi.org/project/click/)
- [GitHub Repository](https://github.com/pallets/click)

---

*This documentation was automatically generated using Tavily Remote MCP and the dependency-documenter skill.*
