# How to test mortgagepy

`mortgagepy` uses `pytest`, `pytest-cov` and `tox` for it's testing.

It is recommended to use a virtual environment before running any tests. This
library uses `uv` to manage this and the following commands from the root of the
directory will run the tests.

```bash
# install uv, using any method, pip is preferred for ease
pip install uv

# create and activate a virtual environment
uv venv
source .venv/bin/activate
uv sync

# run tox
tox

# or run pytest
pytest
```
