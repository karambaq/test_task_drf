# Task

Тестовое задание – дополнительный способ для нас убедиться в вашей квалификации и понять, какого рода задачи вы выполняете эффективнее всего.
Расчётное время на выполнение тестового задания: 2-2,5 часа.

У текущего тестового задания нет чёткого технического задания – такие задачи у нас встречаются. Однако, ниже – все необходимые и достаточные вводные данные для успешного решения задачи.

Задача: реализовать API, позволяющее добавлять, изменять, просматривать и удалять данные в модели "Приложения".
"Приложения" – это модель, которая хранит в себе внешние источники, которые будут обращаться к API. Обязательные поля модели: ID, Название приложения, Ключ API. Поле "Ключ API" нельзя менять через API напрямую, должен быть метод, позволяющий создать новый ключ API.
После добавления приложения – должна быть возможность использовать "Ключ API" созданного приложения для осуществления запросов к метод /api/test, метод должен возвращать JSON, содержащий всю информацию о приложении.

Использовать следующие технологии: Django 2.2.7, Django REST framework.

Результат выполнения задачи:
- исходный код приложения в github
- инструкция по разворачиванию приложения (в docker или локально)
- инструкция по работе с запросами к API: как авторизоваться, как добавить, как удалить и т.д


# Installation
----
    ## Create venv and install requirements with

    `pip install -r requirements.txt`

1) Create postgresql database `test_task`
2) Change DBUSER in `settings.py`

**Run with**
`python manage.py runserver`

# Endpoints:

**List apps**
----
  Returns all existing apps

* **URL**

  /api/apps/

* **Method:**
  
  `GET` 
  

* **Sample Call:**

    `curl "http://127.0.0.1:8000/api/apps/"`

**Get app by id**
----
  Returns app with specified id

* **URL**

  /api/apps/:id

* **Method:**
  
  `GET` 
  

* **Sample Call:**

    `curl "http://127.0.0.1:8000/api/apps/17"`

* **Response:**
    ```
    {
        "id": 17,
        "name": "External 5",
        "api_key": "d5df4592311f354dafd57e31a30de6db7197d003b25b83"
    }
    ```


**Update app name by id**
----
  Updating existing app name by id

* **URL**

  /api/apps/:id/

* **Method:**
  
  `PUT` 
  

* **Sample Call:**


    ```
    curl --header "Content-Type: application/json" \
  --request PUT \
  --data '{"name": "new name"}' \
  http://127.0.0.1:8000/api/apps/17/
    ```

* **Response:**
    ```
    {
        "id":17,
        "name":"new name","api_key":"d5df4592311f354dafd57e31a30
de6db7197d003b25b83"}
    ```


**Update api key**
----
  Update api key

* **URL**

  /api/apps/:api_key/update/

* **Method:**
  
  `PUT` 
  

* **Sample Call:**


    ```
    curl --header "Content-Type: application/json" \
  --request PUT \
    http://127.0.0.1:8000/api/apps/49bbb956a32fe4e30dc9fc66b294a162a927d9dc642cc4/update/
    ```

* **Response:**
    ```
    {
        "message": "your api key is updated",
        "old_api_key": "8f2cec73d308c32c8b7b2388c0bb4445cf8eb76686fab3",
        "new_api_key": "49bbb956a32fe4e30dc9fc66b294a162a927d9dc642cc4"
    }
    ```

**Delete app by id**
----
  Deleting app by id

* **URL**

  /api/apps/:id/

* **Method:**
  
  `DELETE` 
  

* **Sample Call:**

    `curl "http://127.0.0.1:8000/api/apps/17"`

    ```
    curl --header "Content-Type: application/json" \
  --request DELETE \
    http://127.0.0.1:8000/api/apps/17/
    ```


**Get app info by api_key**
----
    Gives info about app

* **URL**

  /api/apps/:api_key/test/info

* **Method:**
  
  `GET` 
  

* **Sample Call:**


    ```
    curl --header "Content-Type: application/json" \
  --request GET \
    http://127.0.0.1:8000/api/apps/811079ee025ca0471b9d0eb1953d04bf2e270f48224333/test/info/
    ```

* **Response:**

    ```
    {
        "app": {
            "id": 18,
            "name": "External 21",
            "api_key": "811079ee025ca0471b9d0eb1953d04bf2e270f48224333"
        }
    }
    ```