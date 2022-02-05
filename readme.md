# Сервис просмотра контента

Для запуска сервиса выполнить
```
pip install -r requirements.txt
python main.py
```

Сервер доступен по адресу
```
http://localhost:8000/
```

Демонстрационные изображения (папка static), а также CSV файл находятся в репозитории, но их можно сгенерировать заново, выполнив:
```
python data_gen.py
```
Примечание: ```data_gen.py``` может быть выполнен только в ОС Windows, поэтому рекомендуется клонировать репозиторий целиком

Сервер принимает запросы в виде:
```
http://localhost:8000/?category=n1&category=n2
http://localhost:8000/?category=n4
http://localhost:8000/?category=n4&category=n2&category=n7
```

Список доступных категорий: ```n0, n1, n2, n3, n4, n5, n6, n7, n8, n9```
