# ft_package

A sample test package for demonstrating package creation in Python.

## Installation

To install `ft_package`, run the following command:

```bash
    pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```
or
```bash
    pip install ./dist/ft_package-0.0.1.tar.gz
```

## Usage
Here's how you can use ft_package:

```
from ft_package import count_in_list

# Count occurrences of an element in a list
print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.