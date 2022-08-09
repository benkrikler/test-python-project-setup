# fibonacci

[![PyPI - Version](https://img.shields.io/pypi/v/fibonacci.svg)](https://pypi.org/project/fibonacci)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fibonacci.svg)](https://pypi.org/project/fibonacci)
[![CI](https://github.com/benkrikler/test-python-project-setup/actions/workflows/ci.yml/badge.svg)](https://github.com/benkrikler/test-python-project-setup/actions/workflows/ci.yml)

-----

**Table of Contents**

- [Overview](#overview)
- [Installation](#installation)
- [Developing](#developing)
- [License](#license)

## Overview
*TODO: Give a brief explanation here*

See the [design choices](docs/design.md) document for more details.

## Installation

```console
pip install fibonacci
```

## Developing

### Pre-commit tests
Static code tests and formatting checks can be run using [pre-commit](pre-commit.com). Install pre-commit, then initialise the hooks for this project with:
```
pre-commit install
```

When you next commit a change, pre-commit will run various formatting and static code checks, in some cases fixing any issues automatically (see e.g. `black` and `isort`).

To manually trigger these checks on all files, you can do something like:

```console
pre-commit run --all-files
```
See pre-commit's built-in help for more guidance.

### Unit testing
Run the built-in unit tests with `pytest`:

```
python -m pytest
```

## Contributing
*TODO: Flesh out this section*

## License

`fibonacci` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
