# CT Parsers


[![pypi](https://img.shields.io/pypi/v/ct-parsers.svg)](https://pypi.org/project/ct_parsers/)
[![python](https://img.shields.io/pypi/pyversions/ct-parsers.svg)](https://pypi.org/project/ct_parsers/)
[![Build Status](https://github.com/birdcar/ct-parsers/actions/workflows/dev.yml/badge.svg)](https://github.com/birdcar/ct_parsers/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/birdcar/ct-parsers/branch/main/graphs/badge.svg)](https://codecov.io/github/birdcar/ct_parsers)



A library and CLI for validating and converting CSVs for import into CoinTracker.


* GitHub: <https://github.com/birdcar/ct-parsers>
* PyPI: <https://pypi.org/project/ct-parsers/>
* Free software: MIT


## Features

* Validates that a CSV file conforms to CoinTrackers Generic CSV format
* Provides a CLI for testing locally

## Installation

```shell
# Clone repository
git clone https://github.com/birdcar/ct-parsers
# Change directory into repository
cd ct-parsers
# install with pip
pip install .
```

## Usage

```shell
# use ct-parse to parse a valid CoinTracker CSV file
ct-parse tests/fixtures/cointracker/kg.csv
# use ct-parse to parse invalid CoinTracker CSV files
for file in $(ls tests/fixtures/cointracker/kb*.csv); do ct-parse $file; done
```

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.
