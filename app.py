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
@app.route('/hello/<cinema_id>')
def cinema(cinema_id):
    with open('theatres.json') as f:
        theatres = json.load(f)
        name = theatres[cinema_id]
    # return 'cinema %d' % cinema_id
    return 'cinema ' + name

# extended theatre above
@app.route('/hell')
def hell():
    with open('theatres.json') as f:
        theatres = json.load(f)
        theatre_to_id = {}
    for theatre_id, name in theatres.items():
        theatre_to_id[name] = theatre_id
    with open('db.json') as f:
        movies = json.load(f)
    schedule = {}
    for movie in movies:
        theatre = movie['theatre']
        if theatre not in schedule:
            schedule[theatre] = {
                "movies": [],
                "id": theatre_to_id[theatre]
            }
        schedule[theatre]['movies'].append(
            {
                'name': movie['name'],
                'time': movie['time']
            }
        )
    return render_template("hell.html", schedule=schedule)


@app.route('/cinema/<cinema_id>')
def cinemas(cinema_id):
    with open('db.json') as f:
        movies = json.load(f)
    with open('theatres.json') as f:
        theatres = json.load(f)
        theatre = theatres[cinema_id]
        result = []
        # for movie in movies:
        #     if movie['theatre'] == theatre:
        #         result.append(movie)
        result = [movie for movie in movies if movie['theatre'] == theatre]
    return render_template('cinema.html', theatre=theatre, movies=result)
