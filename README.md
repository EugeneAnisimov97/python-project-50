### Hexlet tests and linter status:
[![Actions Status](https://github.com/EugeneAnisimov97/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/EugeneAnisimov97/python-project-50/actions)
![workflow_githubaction](https://github.com/EugeneAnisimov97/python-project-50/actions/workflows/pyci.yml/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/d93bf3deddd1242b6582/maintainability)](https://codeclimate.com/github/EugeneAnisimov97/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d93bf3deddd1242b6582/test_coverage)](https://codeclimate.com/github/EugeneAnisimov97/python-project-50/test_coverage)

__"Вычислитель отличий" (gendiff)__ - второй проект, разработанный в рамках обучения на курсе Хекслет. Это инструмент командной строки для поиска различий между двумя файлами.

used in the project:

[**pytest**](https://docs.pytest.org/en/8.2.x/)

[**json**](https://docs.python.org/3/library/json.html)

[**pyyml**](https://pypi.org/project/PyYAML/)

[**agreparse**](https://docs.python.org/3/library/argparse.html)

## Установка
Для установки и запуска проекта вам потребуется Python версии 3.10 и выше и инструмент для управления зависимостями Poetry.

1. Склонируйте репозиторий с проектом на ваше локальное устройство:
```
git clone git@github.com:EugeneAnisimov97/python-project-50.git
```
2. Перейдите в директорию проекта:
```
cd python-project-50
```
3. Установите необходимые зависимости с помощью Poetry:
```
poetry install
```

### Проект поддерживает следующие форматы файлов для поиска отличий:

- YAML
- JSON

## Как найти различия между двумя файлами

1. Поместите два файла, которые вы хотите сравнить, в папку tests/fixtures.
2. Выполните команду для поиска различий:
```
poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
```
3. Замените file1.json и file2.json на названия ваших файлов
***

### Форматы вывода отличий
Для выбора формата вывода различий, укажите флаг -f с названием форматтера. Возможные форматтеры:

- stylish (по умолчанию)
- plain
- json

### Примеры команд для разных форматов вывода:


1. Вывод в стиле stylish
```
poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
```

2. Вывод в формате plain
```
poetry run gendiff -f plain tests/fixtures/file1.json tests/fixtures/file2.json
```

3. Вывод в формате json
```
poetry run gendiff -f json tests/fixtures/file1.json tests/fixtures/file2.json
```

### Демонстрация работы программы:
[![asciicast](https://asciinema.org/a/ugsYDZs6O60dxiHunkqSvow8s.svg)](https://asciinema.org/a/ugsYDZs6O60dxiHunkqSvow8s)

[![asciicast](https://asciinema.org/a/45yB9Ewj4k0DCbvwqZ34lNphi.svg)](https://asciinema.org/a/45yB9Ewj4k0DCbvwqZ34lNphi)

[![asciicast](https://asciinema.org/a/iQXwpPbm17fQW85jfbM7ascMQ.svg)](https://asciinema.org/a/iQXwpPbm17fQW85jfbM7ascMQ)

[![asciicast](https://asciinema.org/a/EF3Trp0sK2C70R5p8xP8p9wJ2.svg)](https://asciinema.org/a/EF3Trp0sK2C70R5p8xP8p9wJ2)

***
## Контакты
- Автор: Eugene Anisimov
- [GitHub](https://github.com/EugeneAnisimov97)
- [Email](zero0061@mail.ru)
- [telegram](https://t.me/Eugene_Anisimov)