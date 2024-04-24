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
	poetry run pytest --cov=gendiff --cov-report xml

gendiff:
	poetry run gendiff

check:
	poetry run flake8

test:
	poetry run pytest

plain:
	poetry run gendiff tests/fixtures/file1nested.json tests/fixtures/file2nested.json -f plain

stylish:
	poetry run gendiff tests/fixtures/file1nested.json tests/fixtures/file2nested.json

json:
	poetry run gendiff tests/fixtures/file1nested.json tests/fixtures/file2nested.json -f json