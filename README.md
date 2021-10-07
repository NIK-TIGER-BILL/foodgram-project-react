# Проект Foodgram
![example workflow](https://github.com/NIK-TIGER-BILL/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg) (falling так как сервер в данный момент отключен)  
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)



Foodgram реализован для публикации рецептов. Авторизованные пользователи
могут подписываться на понравившихся авторов, добавлять рецепты в избранное,
в покупки, скачать список покупок ингредиентов для добавленных в покупки
рецептов.

## команды для запуска приложения
```
docker-compose up
docker-compose up -d --build
```
Можно использовать с флагами:  
-d (убрать сообщение от логов)  
--build (пересборка)  
## Может пригодится:
```
docker-compose exec backend python manage.py migrate --noinput # Проведение миграции
docker-compose exec backend python manage.py collectstatic --no-input  # Сбор статики
```
## .env
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=*** # пароль для подключения к БД(установите свой)
DB_HOST=db # название сервиса
DB_PORT=5432 # порт для подключения к БД
DJ_SECRET_KEY=*** # ключ django
```
## команда для создания суперпользователя
```
docker-compose exec backend python manage.py createsuperuser
```
Далее от вас потребуют вести имя суперпользователя, его почту, и пароль

## команды для загрузки ингридиентов из ingredients.json
Файл должен находится в директории backend/data в расширении json

```
docker-compose exec backend python manage.py load_ingredients  # загрузит из файла по умолчанию ingredients.json
docker-compose exec backend python manage.py load_ingredients ("Название файла")
```

## команда для заполнения базы начальными данными
```
docker-compose exec backend python manage.py loaddata data/init_data.json 
```
Данная команда загрузит начальные данные из фиксатуры

# Проект в интернете
Проект запущен и доступен по [адресу](http://62.84.113.196) (В данный момент сервер отключен)
