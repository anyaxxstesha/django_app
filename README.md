# Для запуска:
1. Заполнить файл .env.example, изменить его название на .env
2. Ввести команду "docker compose up"

# Архитектура:

В проекте есть следующие модули:
* config - основные настройки проекта
* dogs - приложение с основными моделями и логикой

Модель Dog содержит следующие поля:
* name (строка символов)
* age (целое число)
* breed (внешний ключ к модели Breed)
* gender (строка символов)
* color (строка символов)
* favorite_food (строка символов)
* favorite_toy (строка символов)

Модель Breed содержит следующие поля:
* name (строка символов)
* size (строка символов) [должно принимать значения Tiny, Small, Medium, Large]
* friendliness (поле целого числа) [должно принимать значения от 1 до 5]
* trainability (поле целого числа) [должно принимать значения от 1 до 5]
* shedding_amount (поле целого числа) [должно принимать значения от 1 до 5]
* exercise_needs (поле целого числа) [должно принимать значения от 1 до 5]


# Эндпоинты:

---

request: 
```
POST /api/dogs/
```
```json
{
    "id": 7,
    "name": "Чувырла",
    "age": 4,
    "gender": "M",
    "color": "Серый",
    "favorite_food": "ст",
    "favorite_toy": "Банан",
    "breed": 2
}
```

response:
```json
{
    "id": 7,
    "name": "Чувырла",
    "age": 4,
    "gender": "M",
    "color": "Серый",
    "favorite_food": "ст",
    "favorite_toy": "Банан",
    "breed": 2
}
```
---

request: 
```
GET /api/dogs/7/
```

response:
```json
{
    "id": 7,
    "name": "Чувырла",
    "age": 4,
    "breed": 2,
    "gender": "M",
    "color": "Серый",
    "favorite_food": "ст",
    "favorite_toy": "Банан",
    "dogs_amount_same_breed": 1
}
```
---

request: 
```
GET /api/dogs/
```
```json
[
    {
        "id": 4,
        "name": "Rat",
        "age": 5,
        "breed": 1,
        "gender": "M",
        "color": "Серый",
        "favorite_food": "Стейк",
        "favorite_toy": "Банан",
        "avg_breed_age": 6.0
    },
    {
        "id": 5,
        "name": "Rat",
        "age": 6,
        "breed": 1,
        "gender": "M",
        "color": "Серый",
        "favorite_food": "Стейк",
        "favorite_toy": "Банан",
        "avg_breed_age": 6.0
    },
    {
        "id": 1,
        "name": "Лексуссс",
        "age": 5,
        "breed": 1,
        "gender": "M",
        "color": "Пурпур",
        "favorite_food": "Стейк",
        "favorite_toy": "Банан",
        "avg_breed_age": 6.0
    },
    {
        "id": 6,
        "name": "Бульдог",
        "age": 8,
        "breed": 1,
        "gender": "M",
        "color": "Серый",
        "favorite_food": "ст",
        "favorite_toy": "Банан",
        "avg_breed_age": 6.0
    },
    {
        "id": 7,
        "name": "Чувырла",
        "age": 4,
        "breed": 2,
        "gender": "M",
        "color": "Серый",
        "favorite_food": "ст",
        "favorite_toy": "Банан",
        "avg_breed_age": 4.0
    }
]
```
----------
request: 
```
PUT(PATCH) /api/dogs/7/
```
```json
{
    "id": 7,
    "name": "Чувырла",
    "age": 4,
    "gender": "M",
    "color": "Серый",
    "favorite_food": "ст",
    "favorite_toy": "Банан",
    "breed": 2
}
```
response:
```json
{
    "id": 7,
    "name": "Чувырла",
    "age": 5,
    "gender": "M",
    "color": "Серый",
    "favorite_food": "ст",
    "favorite_toy": "Банан",
    "breed": 2
}
```


---

request: 
```
DELETE /api/dogs/7/
```
```json
{
    "id": 7,
    "name": "Чувырла",
    "age": 4,
    "gender": "M",
    "color": "Серый",
    "favorite_food": "ст",
    "favorite_toy": "Банан",
    "breed": 2
}
```
response:
```json

```

---

request: 
```
POST /api/breeds/
```
```json
{
    "id": 3,
    "name": "Бульдог",
    "size": "XS",
    "friendliness": 4,
    "trainability": 4,
    "shedding_amount": 4,
    "exercise_needs": 4
}
```
response:
```json
{
    "id": 3,
    "name": "Бульдог",
    "size": "XS",
    "friendliness": 4,
    "trainability": 4,
    "shedding_amount": 4,
    "exercise_needs": 4
}
```

---

request: 
```
GET /api/breeds/3/
```
response:
```json
{
    "id": 3,
    "name": "Бульдог",
    "size": "XS",
    "friendliness": 4,
    "trainability": 4,
    "shedding_amount": 4,
    "exercise_needs": 4
}
```
----
request: 
```
GET /api/breeds/
```
response:
```json
[
    {
        "id": 1,
        "name": "Бульдог",
        "size": "L",
        "friendliness": 2,
        "trainability": 4,
        "shedding_amount": 1,
        "exercise_needs": 4,
        "dogs_amount": 4
    },
    {
        "id": 2,
        "name": "Чувырла",
        "size": "XS",
        "friendliness": 1,
        "trainability": 3,
        "shedding_amount": 5,
        "exercise_needs": 5,
        "dogs_amount": 0
    },
    {
        "id": 3,
        "name": "Бульдог",
        "size": "XS",
        "friendliness": 4,
        "trainability": 4,
        "shedding_amount": 4,
        "exercise_needs": 4,
        "dogs_amount": 0
    }
]
```
----

request: 
```
PUT(PATCH) /api/breeds/3/
```
```json
{
    "id": 3,
    "name": "Бульдог",
    "size": "XS",
    "friendliness": 5,
    "trainability": 4,
    "shedding_amount": 4,
    "exercise_needs": 4
}
```
response:
```json
{
    "id": 3,
    "name": "Бульдог",
    "size": "XS",
    "friendliness": 5,
    "trainability": 4,
    "shedding_amount": 4,
    "exercise_needs": 4
}
```

---

request: 
```
DELETE /api/breeds/3/
```
```json
{
    "id": 3,
    "name": "Бульдог",
    "size": "XS",
    "friendliness": 5,
    "trainability": 4,
    "shedding_amount": 4,
    "exercise_needs": 4
}
```
response:
```json

```