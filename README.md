# Experience-JustWork

## Тестовое задание django

### Запуск проекта
```console
$ docker‐compose up runserver
```
Доступен по адресу: http://0.0.0.0 8000

### Запуск тестирования

```console
$ docker‐compose up autotests
```

### Примеры запросов API

Список всех страниц

```console
$ curl -X GET \
  http://0.0.0.0:8000/api/v1/pages/ \
  -H 'Cache-Control: no-cache'
```

Список страниц с параметрами пагинации

```console
$ curl -X GET \
  'http://0.0.0.0:8000/api/v1/pages/?limit=2&offset=1' \
  -H 'Cache-Control: no-cache' 
```

Детальная информация о странице

```console
$ curl -X GET \
  http://0.0.0.0:8000/api/v1/page/test/ \
  -H 'Cache-Control: no-cache'
```