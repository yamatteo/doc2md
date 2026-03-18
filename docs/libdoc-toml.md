---
title: "TOML Documentation"
package_name: "toml"
version: ">=0.10.2"
source: "https://github.com/uiri/toml"
last_updated: "2026-03-18 17:49:00"
description: "TOML is a Python library for parsing and creating TOML (Tom's Obvious Minimal Language) configuration files."
---

# TOML

TOML is a Python library for parsing and creating TOML (Tom's Obvious Minimal Language) configuration files. TOML is an enhanced INI format designed to be easy to read and write for humans while being unambiguous for machines.

## Version Information
- **Installed Version**: `>=0.10.2`
- **Documentation Source**: https://github.com/uiri/toml
- **Last Updated**: 2026-03-18 17:49:00

## Key Features
- 📝 Simple and readable configuration format
- 🔧 Easy parsing and generation of TOML files
- 🎯 Type-preserving data structures
- 📊 Supports arrays, tables, and nested structures
- 🌐 Unicode support
- ✅ Passes official TOML test suite
- 🚅 Fast and lightweight
- 🔄 Bidirectional conversion (parse and generate)

## Installation
```bash
pip install toml>=0.10.2
```

## Basic Usage
```python
import toml

# Parse TOML file
config = toml.load('config.toml')
print(config['database']['host'])

# Parse TOML string
toml_string = """
[database]
host = "localhost"
port = 5432
"""
config = toml.loads(toml_string)

# Generate TOML
data = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'tables': ['users', 'posts']
    }
}
toml_string = toml.dumps(data)
```

## Configuration File Example
```toml
# config.toml
title = "My Application"

[database]
host = "localhost"
port = 5432
username = "admin"
password = "secret"

[servers]
[servers.alpha]
ip = "10.0.0.1"
dc = "eqdc10"

[servers.beta]
ip = "10.0.0.2"
dc = "eqdc10"

[clients]
data = [["gamma", "delta"], [1, 2]]
hosts = ["alpha", "omega"]
```

## Python Integration
```python
import toml

# Load configuration
with open('config.toml', 'r') as f:
    config = toml.load(f)

# Access nested data
db_host = config['database']['host']
servers = config['servers']

# Modify configuration
config['database']['port'] = 3306
config['new_section'] = {'key': 'value'}

# Save configuration
with open('config_updated.toml', 'w') as f:
    toml.dump(config, f)
```

## Data Types Support
```python
import toml

# All supported TOML data types
config_data = {
    'string': 'Hello, World!',
    'integer': 42,
    'float': 3.14159,
    'boolean': True,
    'array': [1, 2, 3, 'four'],
    'datetime': toml.datetime.datetime(2023, 1, 1, 12, 0, 0),
    'table': {
        'nested_key': 'nested_value'
    },
    'array_of_tables': [
        {'name': 'item1', 'value': 100},
        {'name': 'item2', 'value': 200}
    ]
}
```

## Error Handling
```python
import toml

try:
    config = toml.load('config.toml')
except toml.TomlDecodeError as e:
    print(f"Error parsing TOML: {e}")
except FileNotFoundError:
    print("Configuration file not found")
```

## Additional Resources
- [Official TOML Specification](https://toml.io/en/)
- [PyPI Package](https://pypi.org/project/toml/)
- [GitHub Repository](https://github.com/uiri/toml)
- [Real Python TOML Tutorial](https://realpython.com/python-toml/)
- [TOML Test Suite](https://github.com/BurntSushi/toml-test)

---

*This documentation was automatically generated using Tavily Remote MCP and the dependency-documenter skill.*
