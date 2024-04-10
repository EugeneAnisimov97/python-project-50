install:  
	poetry install 

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl --force-reinstall

lint:
	poetry run flake8

test-coverage:
	poetry run pytest --cov

gendiff:
	poetry run gendiff

check:
	poetry run pytest
	poetry run flake8