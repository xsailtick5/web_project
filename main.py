from flask import Flask, url_for, request
from PIL import Image

app = Flask(__name__)


@app.route('/')
def title():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    lst = ['Человечество вырастает из детства.',
           'Человечеству мала одна планета.',
           'Мы сделаем обитаемыми безжизненные пока планеты.',
           'И начнем с Марса!',
           'Присоединяйся!']
    return '</br>'.join(lst)


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='photos/mars.png')}"
                     alt="здесь должна была быть картинка, но не нашлась">
                    <p>Это подпись под картинкой Марса</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <link rel="stylesheet"
                    href={url_for('static', filename='css/mystyle.css')}>
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='photos/mars.png')}"
                     alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-dark" id="123">Человечество вырастает из детства.</div>
                    <div class="alert alert-success">Человечеству мала одна планета.</div>
                    <div class="alert alert-secondary">Мы сделаем обитаемыми безжизненные пока планеты.</div>
                    <div class="alert alert-warning">И начнем с Марса!</div>
                    <div class="alert alert-danger">Присоединяйся!</div>
                  </body>
                </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" 
                        href={url_for('static', filename='css/formstyle.css')}>
                        <title>Отбор астронавтов</title>
                      </head>
                      <body>
                        <h1 align="center">Анкета претендента</h1>
                        <h2 align="center">на участие в миссии</h2>
                        <div>
                            <form class="login_form" method="post">
                                    <input type="second_name" class="form-control" id="second_name" placeholder="Введите Фамилию" name="second_name">
                                    <input type="name" class="form-control" id="name" placeholder="Введите Имя" name="name">
                                    <input type="email" class="form-control" id="email" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="educationSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="educationSelect" name="education">
                                          <option>Дошкольное</option>
                                          <option>Начальное общее</option>
                                          <option>Основное общее</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее образование — бакалавриат</option>
                                          <option>Высшее образование — специалитет, магистратура</option>
                                          <option>Высшее образование — подготовка кадров высшей квалификации</option>
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Какие у вас есть профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="engineer" value="engineer">
                                          <label class="form-check-label" for="engineer">
                                            Инженер
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="pilot" value="pilot">
                                          <label class="form-check-label" for="pilot">
                                            Пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="builder" value="builder">
                                          <label class="form-check-label" for="builder">
                                            Строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="biologist" value="biologist">
                                          <label class="form-check-label" for="biologist">
                                            Биолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="navigator" value="navigator">
                                          <label class="form-check-label" for="navigator">
                                            Штурман
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="climatologist" value="climatologist">
                                          <label class="form-check-label" for="climatologist">
                                            Климатолог
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male">
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
                                        <label for="motivation">Почему вы хотите приянть участие в миссии?</label>
                                        <textarea class="form-control" id="motivation" rows="3" name="motivation"></textarea>
                                    </div>
 
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="stay_on_mars" name="stay_on_mars">
                                        <label class="form-check-label" for="stay_on_mars">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                        </div>
                      </body>
                    </html>"""
    elif request.method == 'POST':
        print(request.form['second_name'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['profession'])
        print(request.form['sex'])
        print(request.form['motivation'])
        print(request.form['stay_on_mars'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                    <div class="alert alert-danger">Эта планета близка к Земле;</div>
                    <div class="alert alert-dark">На ней много необходимых ресурсов;</div>
                    <div class="alert alert-success">На ней есть вода и атмосфера;</div>
                    <div class="alert alert-secondary">На ней есть небольшое магнитное поле;</div>
                    <div class="alert alert-warning">Наконец, она просто красива!</div>
                  </body>
                </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h3>Претендента на участие в миссии {nickname}:</h3>
                    <div class="alert alert-success">Поздравляем! Ваш рейтинг после {level} этапа отбора</div>
                    <div class="alert alert-secondary">составляет {rating}!</div>
                    <div class="alert alert-warning">Желаем удачи!</div>
                  </body>
                </html>"""


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'POST':
        f = request.files['file']
        f.save('static/photos/download.png')
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" 
                        href={url_for('static', filename='css/formstyle.css')}>
                    <title>Отбор астронавтов</title>
                  </head>
                  <body>
                        <h1 align="center">Загрузка фотографии</h1>
                        <h2 align="center">для участия в миссии</h2>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <img src={url_for('static', filename='photos/download.png')} width=400>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                  </body>
                </html>"""


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='/css/style.css')}" />
                    <title>Отбор астронавтов</title>
                </head>
                <body>
                <h1>Пейзажи Марса</h1>
                <div class="container">
                  <br>
                  <div id="myCarousel" class="carousel slide" data-ride="carousel">
                    <ol class="carousel-indicators">
                      <li data-target="#myCarousel" data-slide-to="1" class="active"></li>
                      <li data-target="#myCarousel" data-slide-to="2"></li>
                      <li data-target="#myCarousel" data-slide-to="3"></li>
                    </ol>
                    <div class="carousel-inner" role="listbox">
                      <div class="item active">
                        <img src="{url_for('static', filename='photos/landscape1.jpg')}" alt="First slide">
                            <div class="carousel-caption d-none d-md-block">
                                <h5>Лавины на откосах на северном полюсе Марса.</h5>
                                <p>Материал, включающий в себя лед и пыль и, возможно, большие валуны, 
                                откалывается от нависшего утеса и каскадом сходит с более мягких скатов.
                                Это отложение составляет примерно 180 метров в диаметре и растягивается
                                на 190 метров от основания утеса. 
                                </p>
                            </div>
                      </div>
                      <div class="item">
                        <img src="{url_for('static', filename='photos/landscape2.jpg')}" alt="Second slide">
                            <div class="carousel-caption d-none d-md-block">
                                <h5>Кратер Виктория в Meridiani Planum.</h5>
                                <p>Кратер составляет примерно 800 метров в диаметре. 
                                Слоистые осадочные породы отложились вдоль внешней стены кратера,
                                а на дне кратера видны валуны, отколовшиеся от стены кратера. 
                                В пределах стен этого кратера взорвался марсоход НАСА.
                                </p>
                            </div>
                      </div>
                      <div class="item">
                        <img class="d-block w-100" src="{url_for('static', filename='photos/landscape3.jpg')}" alt="Third slide">
                        <div class="carousel-caption d-none d-md-block">
                            <h5>Скалистые плоскогорья региона Nilosyrtis Mensae.</h5>
                            <p>Филлосиликатные (глиняные) минералы были найдены в регионе 
                            с помощью спектрометров космических аппаратов «Mars Express» и
                            «MRO», они представляют огромный интерес для поиска доказательств
                            жизни на древнем Марсе. 
                            </p>
                        </div>
                      </div>
                    </div>
                    <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
                      <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                      <span class="sr-only">Previous</span>
                    </a>
                    <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
                      <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                      <span class="sr-only">Next</span>
                    </a>
                  </div>
                </div>
                </body>
                </html>
                '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
