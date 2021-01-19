# final_project_n_lavanya 

![](https://github.com/nlavanya96/final_project_n_lavanya/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/nlavanya96/final_project_n_lavanya/branch/main/graph/badge.svg)](https://codecov.io/gh/nlavanya96/final_project_n_lavanya) ![Release](https://github.com/nlavanya96/final_project_n_lavanya/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/final_project_n_lavanya/badge/?version=latest)](https://final_project_n_lavanya.readthedocs.io/en/latest/?badge=latest)

API client package for users to call transportation APIs by Singapore's Land Transport Authority

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ final_project_n_lavanya
```

## Features

This packages enables users to call transportation APIs by Singapore's Land Transport Authority and obtain real-time information on transport and traffic situations. Various datasets can be built with the help of the functions in this package that can be used for a variety of purposes such as visualising transport conditions and analysing transportation trends. 24 functions are available in this package.

## Dependencies

[tool.poetry.dependencies] python = "^3.7" pandas = "^1.1.5" requests = "^2.25.1" pytest = "^6.2.1" datetime = "^4.0.1"

[tool.poetry.dev-dependencies] pytest = "^6.2.1" sphinx = "^3.3.1" sphinxcontrib-napoleon = "^0.7"

## Usage

The package consists of 24 functions that allow you to obtain datasets on different aspects such as bus arrivals, taxi availability, traffic incidents etc.

## Documentation

The official documentation is hosted on Read the Docs: https://final_project_n_lavanya.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/nlavanya96/final_project_n_lavanya/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
