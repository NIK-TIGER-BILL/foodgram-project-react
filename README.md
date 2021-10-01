# Foodgram-project-react

## команды для запуска приложения
```
docker-compose up
```
Можно использовать с флагом -d, чтобы убрать сообщение от логов
Может пригодится:
```
docker-compose exec backend python manage.py migrate --noinput # Проведение миграции
docker-compose exec backend python manage.py collectstatic --no-input  # Сбор статики
```
## команда для создания суперпользователя
```
docker-compose backend web python manage.py createsuperuser
```
Далее от вас потребуют вести имя суперпользователя, его почту, и пароль

## команды для загрузки ингридиентов из ingredients.json
```
docker-compose backend web python manage.py shell
```
И пишем там:
```
import json
from api.models import Ingredient

with open('data/ingredients.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for ingredient in data:
        Ingredient.objects.create(name=ingredient["name"],
                                  measurement_unit=ingredient[
                                      "measurement_unit"])
```

## команда для заполнения базы начальными данными(Еще не добавил)
```
docker-compose backend web python manage.py loaddata fixtures.json 
```
Данная команда загрузит начальные данные из фиксатуры

Публичный IP: 62.84.113.196
