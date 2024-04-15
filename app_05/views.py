from django.shortcuts import render
import random
import logging

from django.http import HttpResponse
logger = logging.getLogger(__name__)

# Create your views here.

# Задание №5
# � Создайте новое приложение. Подключите его к проекту. В
# приложении должно быть три простых представления,
# возвращающих HTTP ответ:
# � Орёл или решка
# � Значение одной из шести граней игрального кубика
# � Случайное число от 0 до 100
# � Пропишите маршруты

def one(request):
    logger.info('page ONE started')
    answer = ['Орел', 'Решка']
    return HttpResponse(f'{answer[random.randint(0,1)]}')

def two(request):
    logger.info('page TWO started')
    return HttpResponse(f'{random.randint(1, 6)}')

def three(request):
    logger.info('page THREE started')
    return HttpResponse(f'{random.randint(1, 100)}')

def index(request):
    logger.info(' /5/index page started')
    html = """
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title> Пример простой страницы index.html</title>
        </head>
        <body>
            <h1>index.html</h1>
            <br>Пример простой страницы - для того, чтобы посмотреть код, нажмите ctrl + U
        </body>
    </html>
    """
    return HttpResponse(html)

def about(request):
    logger.info(' /5/about page started')
    html = """
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title> Пример простой страницы about.html</title>
        </head>
        <body>
            <h1>about.html</h1>
            <br>Пример простой страницы - для того, чтобы посмотреть код, нажмите ctrl + U
        </body>
    </html>
    """
    return HttpResponse(html)