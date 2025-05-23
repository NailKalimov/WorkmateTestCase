# Генератор отчётов по зарплатам сотрудников из CSV-файлов.

Проект реализован на Python с использованием только стандартной библиотеки.  
Легко расширяется для новых типов отчётов.
Образцы входных данных находятся в папке ./source

## Функционал

- Чтение данных сотрудников из одного или нескольких CSV-файлов с разными названиями колонок для ставки (`hourly_rate`, `rate`, `salary`).
- Гибкая обработка структуры входных файлов (порядок и названия колонок не важны).
- Генерация отчёта по зарплатам с группировкой по отделам и итогами (см. пример ниже).
- Валидация аргументов командной строки.
- Расширяемая архитектура: новые типы отчётов добавляются через отдельные классы.
- Покрытие кода тестами на pytest.

## Пример отчёта
![image](https://github.com/user-attachments/assets/6a5415ab-e45f-4160-a489-0a611cff516b)

## Установка и запуск

1. **Клонировать репозиторий:**
   ```bash
   git clone <URL>
   cd <project_folder>
   ```

2. **Создать виртуальное окружение:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # или venv\\Scripts\\activate на Windows
   ```

3. **Установить зависимости для тестирования (pytest):**
   ```bash
   pip install -r requirements.txt
   ```

4. **Запустить скрипт с входными файлами:**
   ```bash
   python main.py source/data1.csv source/data2.csv source/data3.csv --report payout
   ```

## Тестирование

- Все основные модули покрыты тестами на pytest.
- Покрытие кода тестами: **94%** (см. отчёт `pytest --cov`).

### Запуск тестов и проверка покрытия

```bash
pytest
pytest --cov=.utils
```

## Как добавить новый тип отчёта

1. Создай новый класс отчёта в `report.py`, унаследованный от `Report`.
2. Зарегистрируй его в `ReportFactory` в `utils/report_factory.py`.
3. Запусти с новым типом отчёта:  
   ```bash
   python main.py ... --report <new_report_type>
   ```

