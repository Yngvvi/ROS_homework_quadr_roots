# Задание
Принимает на вход 3 числа с плавающей точкой - коэффициенты a,b,c квадратного уравнения. Ответом является строка, содержащая ответ (два корня, один корень или нет корней). Пример запроса: 1.0 8.0 3.0. Ответ: "x1 = -0.39, x2 = -7.61"

## Состав пакета
В состав пакета помимо сервера (<b>roots_server</b>) входит две версии клиента: <b>auto_roots_client</b>, генерирующий запросы с частотой 1 Гц (1 запрос в секунду), при этом значения коэффициентов a, b и c находятся в промежутке от -50 до 50, и <b>roots_client</b>, позволяющий делать запросы вручную, значения коэффициентов при этом вводятся через пробел после названия файла при его запуске.

Пример запуска клиента вручную:
>rosrun quadr_roots src/roots_client.py 1 8 3

## Тип сообщений - GetRoots
Сообщения <b>GetRoots</b>, которыми обмениваются клиент и сервис, содержат 3 поля запроса a, b, c (типа float32) и поле ответа - message (типа string).

## Дополнительная информация
Версия ROS - ROS Noetic

Язык программирования - python
