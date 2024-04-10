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

check:
	poetry run pytest

test-coverage:
	poetry run coverage run -m pytest

gendiff:
	poetry run gendiff