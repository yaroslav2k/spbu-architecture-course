# spbu-archtecture-course

Состав группы:
1) Николай Березиков (РПО)
2) Курбатов Ярослав (РПО)

# Установка и запуск

Требуется интерпретатор CPython 3.10.

1) Установка Poetry

В проекте используется [Poetry](https://python-poetry.org/) для управления зависимости.<br>

Linux, macOS, Windows (WSL):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Windows (Powershell):

```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

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
