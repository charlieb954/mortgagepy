# Contributing to mortgagepy

`mortgagepy` uses `ruff` and `uv` for testing, linting and packaging. For
instructions on how to test the package, visit [TESTING.md](./TESTING.md)

## add/update a dependency

Dependencies are managed using `uv` to add a dependency run the following command:

```bash
uv add example-package # dependency
uv add example-package --dev # dev dependency
uv add example-package --group docs # doc dependency
```

## ruff

`ruff` is used for linting and formatting. All contributions should be formatted
and linted, this will then be checked using GitHub actions. To run the linting
manually you can use the following commands:

```bash
uvx ruff format
uvx ruff check
```
