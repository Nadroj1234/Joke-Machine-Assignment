from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/joke_generator', methods=['GET', 'POST'])
def joke_generator():
    response = requests.get('https://icanhazdadjoke.com/ ')

    return render_template('joke_generator.html')


@app.route('/joke_search')
def joke_search():
    return render_template('joke_search.html')


if __name__ == '__main__':
    app.run(debug=True)
