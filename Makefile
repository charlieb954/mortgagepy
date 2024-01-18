test:
	coverage run --source=mortgagepy -m pytest -v tests && coverage report -m

build:
	poetry build