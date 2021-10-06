# Проект Foodgram
![example workflow](https://github.com/NIK-TIGER-BILL/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)  

Foodgram сделан для публикации рецептов. Авторизованные пользователи
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
##Может пригодится:
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
