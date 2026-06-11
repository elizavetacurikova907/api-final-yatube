# api_final
## Описание проекта:
Бэкенд соцсети, в которой можно публиковать посты с фотографиями или без, оставлять к ним комментарии, а также подписываться на других пользователей. Доступно подключение любого фронтенда с помощью API.
## Как запустить проект:

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
