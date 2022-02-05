Запуск сервера:
main.py

Сервер доступен по адресу http://localhost:8000/

Сервер принимает запросы в виде:
http://localhost:8000/?category=n1&category=n2
http://localhost:8000/?category=n4
http://localhost:8000/?category=n4&category=n2&category=n7

Список доступных категорий: n0, n1, n2, n3, n4, n5, n6, n7, n8, n9

Сервер возвращает изображения, находящиеся в папке "static"

Папка static и соответствующий файл conf.csv находятся в репозитории, либо их можно сгенерировать вызвав data_gen.py
data_gen.py работает только в ОС Windows (так как используется модуль OS)

