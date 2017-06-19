# cxflow-scikit

Scientific extension for `cxflow` framework.

## Development Status

- [![Build Status](https://gitlab.com/Cognexa/cxflow-scikit/badges/master/build.svg)](https://gitlab.com/Cognexa/cxflow-scikit/builds/)
- [![Development Status](https://img.shields.io/badge/status-CX%20PoC-yellow.svg?style=flat)]()
- [![Master Developer](https://img.shields.io/badge/master-Petr%20Bělohlávek-lightgrey.svg?style=flat)]()

## Requirements
The main dependency is cxflow (see [Cognexa/cxflow](https://gitlab.com/Cognexa/cxflow)
for installation guide).
Other requirements are listed in `requirements.txt`.

## Installation
Installation to a [virtualenv](https://docs.python.org/3/library/venv.html) is suggested, however, completely optional. 

### Standard Installation
1. Install **cxflow-scikit** `$ pip install git+https://gitlab.com/Cognexa/cxflow-scikit.git`

### Development Installation
1. Clone the **cxflow-scikit** repository `$ git clone git@gitlab.com:Cognexa/cxflow-scikit.git`
2. Enter the directory `$ cd cxflow-scikit`
3. Install **cxflow-scikit**: `$ pip install -e .`

## Usage
When `cxflow-scikit` installed, the following classes are available:

### Hooks

- `cxflow_tf.ClassificationInfoHook`

## Testing
Unit tests might be run by `$ python setup.py test`.

## License
MIT License
