from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def page1():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def page2():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def page3():
    return '''
    <p>Человечество вырастает из детства.</p>
    <p>Человечеству мала одна планета.</p>
    <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
    <p>И начнем с Марса!</p>
    <p>Присоединяйся!</p>
    '''


@app.route('/image_mars')
def page4():
    return f'''
        <!doctype html>
        <html lang="ru">
          <head>
            <meta charset="utf-8">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
            <title>Привет, Марс!</title>
          </head>
          <body>
            <h1>Жди нас, Марс!</h1>
            <img src="{url_for('static', filename='img/marse.png')}" alt="картинка марса чо">
            <p>вот она какая, красная планета!</p>
          </body>
        </html>
                '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
