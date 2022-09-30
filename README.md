# simple news api
### API DOC
#### 1. `POST auth/register/ `
<p>Регистрация нового пользователя. </p> 

request
```JSON
{
  "username": "string",
  "password": "string",
  "password2": "string",
  "email": "user@example.com"
}
```
response
```JSON
{
  "username": "string",
  "email": "user@example.com"
}
```
#### 2. `POST auth/token/`
<p>Получение JWT токена для доступа к данным API. Во всех небезопасных методах (POST, PUT, DELETE) необходимо передавать полученный токен в headers. </p>

`Authorization: Bearer your_token`

request
```JSON
{
  "username": "string",
  "password": "string"
}
```
response
```JSON
{
  "refresh": "string",
  "access": "string"
}
```
#### 3. `POST auth/token/refresh/`
<p>Получение нового токена по refresh токену.</p>

request
```JSON
{
"refresh": "string"
}
```
response
```json
{
"refresh": "string",
"access": "string"
}
```

#### 4. `GET news/`
<p>Получение списка новостей, доступ для всех пользователей.</p>

response
```json
{
"count": 0,
"next": "http://example.com",
"previous": "http://example.com",
"results": [
{
"id": 0,
"author_name": "string",
"likes": 0,
"comments": 0,
"newscomment": [],
"title": "string",
"description": "string",
"created_at": "2019-08-24T14:15:22Z"
}
]
}
```

#### 5. `POST news/`
<p> Публикация новой новости, доступ для авторизированных пользователей.</p>

request
```json
{
"title": "string",
"description": "string"
}
```
response
```json
{
"id": 0,
"author_name": "string",
"likes": 0,
"comments": 0,
"newscomment": [
{}
],
"title": "string",
"description": "string",
"created_at": "2019-08-24T14:15:22Z"
}
```

#### 6. `GET news/{id}/`
<p>Получение детальной новости, доступ для всех пользователей.</p>

response
```json
{
"id": 0,
"author_name": "string",
"likes": 0,
"comments": 0,
"newscomment": [
{}
],
"title": "string",
"description": "string",
"created_at": "2019-08-24T14:15:22Z"
}
```

#### 7. `PUT news/{id}/`
<p>Обновление новости, доступ для автора новости или админа.</p>

request
```json
{
"title": "string",
"description": "string"
}
```
response
```json
{
"id": 0,
"author_name": "string",
"likes": 0,
"comments": 0,
"newscomment": [
{}
],
"title": "string",
"description": "string",
"created_at": "2019-08-24T14:15:22Z"
}
```

#### 8. `DELETE news/{id}/`
<p>Удаление новости, доступ для атвора или админа.</p>

#### 9. `GET comments/`
<p>Получение списка комментариев, доступ для всех.</p>

response
```json
[
{
"news": 0,
"news_title": "string",
"content": "string",
"user": "string"
}
]
```

#### 10. `POST comments/`
<p>Публикация коментария, доступ для авторизированных пользователей.</p>

request
```json
{
"news": 0,
"content": "string"
}
```
response
```json
{
"news": 0,
"news_title": "string",
"content": "string",
"user": "string"
}
```

#### 11. `GET comments/{id}/`
<p>Получение детального комментария, доступ для всех пользователей.</p>

response
```json
{
"news": 0,
"news_title": "string",
"content": "string",
"user": "string"
}
```

#### 12. `DELETE comments/{id}/`
<p>Удаление комментария, доступ для автора комментария, автора самой новости, админа.</p>

#### 13. `GET likes/`
<p>Получение списка лайков, доступно для всех пользователей.</p>

response
```json
[
{
"id": 0,
"user": "string",
"liked": true,
"news": 0
}
]
```

#### 14. `POST likes/`
<p>Публикация лайка, доступ для авторизированных пользователей.</p>

request
```json
{
"liked": true,
"news": 0
}
```
response
```json
{
"id": 0,
"user": "string",
"liked": true,
"news": 0
}
```

#### 15. `GET likes/{id}/`
<p>Получение лайка, доступ для всех пользователей.</p>

response
```json
{
"id": 0,
"user": "string",
"liked": true,
"news": 0
}
```

#### 16. `DELETE likes/{id}/`
<p>Удаление лайка, доступ для админа.</p>

## Run project instruction

1. `git clone https://github.com/lacusver/news_portal.git`
2. `pip install -r requirements.txt`
3. В корне проекта создайте файл .env и укажите:
    + SECRET_KEY -> секретный ключ для работы Django
    + DATABASE_NAME -> имя вашей бд
    + DATABASE_USER -> имя пользователя бд
    + DATABASE_PASS -> пароль от бд
4. Запустите сервер `python manage.py runserver`
