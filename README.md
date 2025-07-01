# Ecommerce Platform

[![Django](https://img.shields.io/badge/Django-5.0-092E20?logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.14.0-red)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-blue?logo=postgresql)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-3.8-2496ED?logo=docker)](https://www.docker.com/)

Онлайн-магазин с системой заказов, кэшбэка и управления товарами.

## 📌 Основные возможности

- **Управление пользователями**
  - Регистрация с подтверждением email
  - Аутентификация по токену
  - Ролевая модель (клиенты/менеджеры)

- **Товары и корзина**
  - Каталог с фильтрацией и поиском
  - Система скидок на товары
  - Корзина с временным хранением

- **Заказы и оплата**
  - Многоэтапное оформление заказа
  - Применение промокодов
  - Использование кэшбэка
  - История заказов

- **Промо-механики**
  - Скидки на товары (админ-панель)
  - Промокоды (суммируемые/обычные)
  - Кэшбэк-система (начисление/списание)

- **Уведомления**
  - Подтверждение заказа
  - Оповещения о доставке
  - Еженедельная рассылка скидок

## 🛠 Технологический стек

| Компонент       | Технология                |
|-----------------|--------------------------|
| Backend         | Django 5.0 + DRF 3.14    |
| База данных     | PostgreSQL 13            |
| Асинхронные задачи | Celery 5.3 + Redis 6    |
| Деплой          | Docker + Gunicorn        |
| Документация    | Swagger/OpenAPI          |

## 🚀 Быстрый старт

### Требования
- Docker 20.10+
- Docker Compose 1.29+

### Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Snowdenru/ecommerce-platform.git
   cd ecommerce-platform
   ```

2. Создайте `.env` файл (пример в `.env.example`):
   ```bash
   cp .env.example .env
   ```

3. Запустите сервисы:
   ```bash
   docker-compose up --build -d
   ```

4. Примените миграции:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. Создайте администратора:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

6. Запустите Celery workers (опционально):
   ```bash
   docker-compose exec celery celery -A ecommerce worker -l info
   docker-compose exec celery-beat celery -A ecommerce beat -l info
   ```

## 🌐 Доступ к сервисам

| Сервис          | URL                          |
|----------------|-----------------------------|
| Основное API    | `http://localhost:8000/api/` |
| Админ-панель    | `http://localhost:8000/admin/` |
| Swagger Docs    | `http://localhost:8000/swagger/` |
| Redoc           | `http://localhost:8000/redoc/` |

## 📚 Документация API

Полная документация доступна через Swagger UI:
- Интерактивная документация: `/swagger/`
- Redoc: `/redoc/`

Примеры запросов:

```bash
# Регистрация пользователя
curl -X POST http://localhost:8000/api/accounts/register/ \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "password123"}'

# Получение списка товаров
curl http://localhost:8000/api/products/

# Создание заказа
curl -X POST http://localhost:8000/api/orders/ \
  -H "Authorization: Token {your_token}" \
  -H "Content-Type: application/json" \
  -d '{"promo_code": "SUMMER20"}'
```

## 🧩 Структура проекта

```
ecommerce/
├── apps/
│   ├── accounts/       # Пользователи и аутентификация
│   ├── products/       # Каталог товаров
│   ├── cart/           # Корзина покупок
│   ├── orders/         # Система заказов
│   └── promotions/     # Скидки и промокоды
├── ecommerce/          # Основные настройки проекта
├── static/             # Статические файлы
├── templates/          # Шаблоны email-уведомлений
└── tests/              # Тесты
```

## 🧪 Тестирование

Для запуска тестов:
```bash
docker-compose exec web python manage.py test
```

Покрытие тестами:
- Модели: XX%
- API: XX%
- Бизнес-логика: XX%

## 🔧 Настройки окружения

Основные переменные в `.env`:

```ini
# Базовые
DEBUG=True
SECRET_KEY=your-secret-key

# База данных
POSTGRES_DB=ecommerce
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

# Email
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=user@example.com
EMAIL_HOST_PASSWORD=password

# Кэшбэк
CASHBACK_PERCENT=5
MIN_CASHBACK_AMOUNT=1000
```

## 📄 Лицензия

Этот проект является учебным и распространяется под лицензией MIT. См. файл LICENSE для получения дополнительной информации.

 ---

Ecommerce Platform © 2025

