# font-val

## Style / Linting / Unit Testing

### Python
[![Tested with Pytest](https://img.shields.io/badge/Tested%20with-Pytest-red?style=for-the-badge)](https://docs.pytest.org/)

Pytest files are found in the `tests` folder.

Run pytest from the root of the project.

You can test for coverage using:
```text
pytest --cov --cov-report=html
```

[![Code style: black](https://img.shields.io/badge/Code%20Style-Black-000000.svg?style=for-the-badge)](https://github.com/psf/black)


```text
isort --profile black .
black --line-length 120 .
flake8 --append-config=.github/linters/.flake8
```
