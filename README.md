# spbu-archtecture-course

Состав группы:
1) Николай Березиков (РПО)
2) Курбатов Ярослав (РПО)

# Установка и запуск

Требуется интерпретатор CPython 3.10.

## Linux, macOS:

1) Установка Poetry

В проекте используется [Poetry](https://python-poetry.org/) для управления зависимости.<br>

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2) Установка зависимостей

Из корня репозитория:

```bash
(cd pybash && poetry install)
```

3) Запуск

```bash
(cd pybash && poetry run python pybash/cli.py)
```

## Windows (Powershell):

1) Установка зависимостей

Из корня репозитория:

```bash
pip install .\pybash\
```

2) Запуск
```bash
python .\pybash\pybash\cli.py
```

