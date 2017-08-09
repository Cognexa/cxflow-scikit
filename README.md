# cxflow-scikit
[![CircleCI](https://circleci.com/gh/Cognexa/cxflow-scikit/tree/master.svg?style=shield)](https://circleci.com/gh/Cognexa/cxflow-scikit/tree/master)
[![Development Status](https://img.shields.io/badge/status-CX%20Regular-brightgreen.svg?style=flat)]()
[![Master Developer](https://img.shields.io/badge/master-Petr%20Bělohlávek-lightgrey.svg?style=flat)]()

Scientific extension for `cxflow` framework.

## Requirements
The main dependency is cxflow (see [Cognexa/cxflow](https://github.com/Cognexa/cxflow)
for installation guide).
Other requirements are listed in `requirements.txt`.

## Installation
Installation to a [virtualenv](https://docs.python.org/3/library/venv.html) is suggested, however, completely optional. 

### Standard Installation
1. Install **cxflow-scikit** `$ pip install git+https://github.com/Cognexa/cxflow-scikit.git`

### Development Installation
1. Clone the **cxflow-scikit** repository `$ git clone git@github.com:Cognexa/cxflow-scikit.git`
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
