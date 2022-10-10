# spbu-archtecture-course

Состав группы:
1) Николай Березиков (РПО)
2) Курбатов Ярослав (РПО)

# Установка и запуск

Требуется интерпретатор **CPython 3.10**.

В дальшейшем подразумевается, что python3 указывает на интерпретатор именно этой версии. (`python3 --version # => 3.10.*`)

Официальный мануал по установке poetry: https://python-poetry.org/docs/#installation

## Linux:

1) Установка Poetry

В проекте используется [Poetry](https://python-poetry.org/) для управления зависимости.<br>

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2) Установка зависимостей

Из папки pybash в корне репозитория:

```bash
poetry install
```

3) Запуск

Из папки pybash в корне репозитория:

```bash
poetry run python pybash/cli.py
```

## Windows (Сmd):

1) Установка зависимостей

Из корня репозитория:

```
pip install .\pybash\
```

2) Запуск

```
python .\pybash\pybash\cli.py
```

# grep

В качестве инструмента для парсинга опций командной строки рассматривались основные более-менее популярные варианты, в том числе [argparse](https://pypi.org/project/argparse/), [click](https://pypi.org/project/click/) и [docopt](https://pypi.org/project/docopt/), однако
в итоге был выбран `argparse` - стандарт de facto, предоставляющий простой и понятный интерфейс и достаточную для решения задачи функциональность.