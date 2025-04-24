# How to test mortgagepy

`mortgagepy` uses `pytest` and `pytest-cov` for testing.

It is recommended to use a virtual environment before running any tests. This
library uses `uv` to manage this and the following commands from the root of the
directory will run the tests.

```bash
# install uv, using any method, pip is one option
pip install uv

# create and activate a virtual environment
uv run pytest --cov-report=term --cov=mortgagepy
```
