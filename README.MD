## Требования
Python >= 3.10

## Установка
Виртуальное окружение
```bash
python3.10 -m venv .venv
source .venv/bin/activate
```

Зависимости
```bash
python -m pip install -r requirements.txt
python -m pip install -e ./src
```

## Тесты
`python -m pytest tests/`

## Пояснения к реализации
- camelCase используется для аутентичности с названиями функций, указанных в тестовом задании
- Предполагается, что:
    - Идентификатор элемента (включая root) уникален
    - Элементы в массиве расположены так, что родитель не может распологаться после дочернего элемента
