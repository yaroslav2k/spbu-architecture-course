# spbu-archtecture-course

Состав группы:
1) Николай Березиков (РПО)
2) Курбатов Ярослав (РПО)

# Установка и запуск

Требуется интерпретатор **CPython 3.10**.

В дальшейшем подразумевается, что python3 указывает на интерпретатор именно этой версии. (`python3 --version # => 3.10.*`)

Оффициальный мануал по установке poetry: https://python-poetry.org/docs/#installation

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

