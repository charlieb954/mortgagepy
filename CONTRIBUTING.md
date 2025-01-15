# Contributing to mortgagepy

`mortgagepy` uses `tox`, `ruff` and `uv` for testing, linting and packaging. For
instructions on how to test the package, visit [TESTING.md](./TESTING.md)

## add/update a dependency

Depedencies are managed using `uv` to add a dependency run the following command:

```bash
uv add example-package
```

To add an optional dependency, you will need to run the following:

```bash
uv add example-package --dev
```
