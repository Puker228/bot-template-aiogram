# bot-template-aiogram

## Установка зависимостей 
```
pip3.11 install -r requirements.txt
```

## Запуск бота
```
python3.11 src/main.py
```

## Env переменные 
| Переменная | Значение   |
| ------- | ---------- |
| BOT_TOKEN | Токен Бота |
| ADMIN_IDS | id Админов |
| DB_HOST | хост       |
| DB_PASS | пароль     |
| DB_PORT | порт       |
| DB_USER | ник        |
| DB_NAME | имя бд     |

## Миграции

создать миграцию
```
alembic revision --autogenerate -m "initial"
```

```
alembic upgrade head
```
