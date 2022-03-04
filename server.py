from flask import Flask, url_for, request

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
             <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
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


@app.route('/promotion_image')
def page5():
    return f'''
        <!doctype html>
        <html lang="ru">
          <head>
            <meta charset="utf-8">
             <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
            <title>Привет, Марс!</title>
          </head>
          <body>
            <h1>Жди нас, Марс!</h1>
            <img src="{url_for('static', filename='img/marse.png')}" alt="картинка марса чо">
            <div class="alert alert-primary" role="alert">Человечество вырастает из детства.</div>
            <div class="alert alert-secondary" role="alert">Человечеству мала одна планета.</div>
            <div class="alert alert-success" role="alert">Мы сделаем обитаемыми безжизненные пока планеты.</div>
            <div class="alert alert-danger" role="alert">И начнем с Марса!</div>
            <div class="alert alert-warning" role="alert">Присоединяйся!</div>
          </body>
        </html>
        '''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>анкета в космонавты</h1>
                            <div>
                                <form class="login_form" method="post">   
                                    <input class="form-control" id="shurename" aria-describedby="emailHelp" placeholder="Введите фамилию" name="shurename">
                                    <input class="form-control" id="name" aria-describedby="emailHelp" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>высшее</option>
                                          <option>среднее</option>
                                          <option>низшее</option>
                                          <option>окончил школу</option>
                                          <option>окончил садик</option>
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">какова ваша профессия?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="1" value="1" checked>
                                          <label class="form-check-label" for="male">
                                            Милиционер
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="2" value="2">
                                          <label class="form-check-label" for="female">
                                            Врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="3" value="3">
                                          <label class="form-check-label" for="female">
                                            Не-ет, моя главная профессия — ПО-О-О-ВАР! 
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="4" value="4">
                                          <label class="form-check-label" for="female">
                                            пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="5" value="5">
                                          <label class="form-check-label" for="female">
                                            строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="6" value="6">
                                          <label class="form-check-label" for="female">
                                            экзобиолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="7" value="7">
                                          <label class="form-check-label" for="female">
                                            врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="job" id="8" value="8">
                                          <label class="form-check-label" for="female">
                                            инженер по терраформированию
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">почему вы хотите стать космонавтом?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов остаться на марсе</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form)
        return "<h1>Форма отправлена</h1>"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
