После скачивания проекта запустить  pip3 install -r requirements.txt. 

Так же нужно установить БД Postgresql. В терминале набрать следующее.
1)  sudo -u postgres psql
2)  CREATE DATABASE django_db;
3)  CREATE USER mike WITH PASSWORD 'password';
4)  ALTER ROLE mike SET client_encoding TO 'utf8';
5)  ALTER ROLE myprojectuser SET timezone TO 'UTC';
6)  GRANT ALL PRIVILEGES ON DATABASE django_db TO mike;
7)  \q


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Получение списка активных опросов
GET метод

active/polls/ - без параметров
Прохождение опроса

POST метод

take/poll/

Пример POST запроса находится в файле example.json

Получение пройденных опросов

GET метод

completed/polls/{uid}/

Параметры: uid: идентификатор пользователя

После запуска проект,дока по Api находится по адресу http://127.0.0.1:8000/swagger
