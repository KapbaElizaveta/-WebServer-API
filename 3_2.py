from flask import Flask, url_for, request

app = Flask(__name__)


# @app.route('/carousel', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def carousel():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            # <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
                            # <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
                            # <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
                            <title>Чудеса света</title>
                          </head>
                          <body>
                            <h1 align="center">Чудеса света</h1>
                            <div align="center" id="carousel-example-generic" class="carousel slide" data-ride="carousel">
                              <ol class="carousel-indicators">
                                <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="1"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="2"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="3"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="4"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="5"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="6"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="7"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="8"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="9"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="10"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="11"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="12"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="13"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="14"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="15"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="16"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="17"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="18"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="19"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="20"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="21"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="22"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="23"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="24"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="25"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="26"></li>
                              </ol>
                              <div class="carousel-inner" role="listbox">
                                <div class="carousel-item active">
                                  <img src="/static/img/1.jpg" alt="First slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/2.jpg" alt="Second slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/3.jpg" alt="Third slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/4.jpg" alt="Third slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/5.jpg" alt="Fourth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/6.jpg" alt="Fifth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/7.jpg" alt="Sixth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/8.jpg" alt="Slide slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/9.jpg" alt="The ninth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/10.jpg" alt="The tenth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/11.jpg" alt="The eleventh slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/12.jpg" alt="The twelfth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/13.jpg" alt="The thirteenth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/14.jpg" alt="The fourteenth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/15.jpg" alt="The fifteenth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/16.jpg" alt="The sixteenth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/17.jpg" alt="The sixteenth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/18.jpg" alt="The sixteenth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/19.jpg" alt="The sixteenth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/20.jpg" alt="The sixteenth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/21.jpg" alt="The sixteenth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/22.jpg" alt="The sixteenth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/23.jpg" alt="The sixteenth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/24.jpg" alt="The sixteenth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/25.jpg" alt="The sixteenth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/26.jpg" alt="The sixteenth slide">
                                </div>
                              </div>
                              <a class="left carousel-control" href="#carousel" role="button" data-slide="prev">
                                <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                                <span class="sr-only">Previous</span>
                              </a>
                              <a class="right carousel-control" href="#carousel" role="button" data-slide="next">
                                <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                                <span class="sr-only">Next</span>
                              </a>
                            </div>
                        </div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
