from flask import Flask, render_template, request
import json
app = Flask(__name__)


@app.route('/')
def movies():
    with open("db.json") as f:
        movies = json.load(f)
    return render_template('index.html', movies=movies)


@app.route('/theatres')
def movie():
    with open('db.json') as f:
        movies = json.load(f)
    theatres = {}
    for movie in movies:
        theatre = movie['theatre']
        if theatre not in theatres:
            theatres[theatre] = []
        theatres[theatre].append(
            {
                'name': movie['name'],
                'time': movie['time']

            }
        )
    print(theatres)
    return render_template('theatres.html', theatres=theatres)


# @app.route('/cinema/<int:cinema_id>')
@app.route('/cinema/<cinema_id>')
def cinema(cinema_id):
    with open('theatres.json') as f:
        theatres = json.load(f)
        name = theatres[cinema_id]
    # return 'cinema %d' % cinema_id
    return 'cinema ' + name
