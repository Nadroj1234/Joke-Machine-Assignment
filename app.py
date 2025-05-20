from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/joke_generator', methods=['GET', 'POST'])
def joke_generator():
    joke = None
    error = None
    mood = ''
    moods = ['funny', 'sad', 'angry', 'excited', 'happy']

    if request.method == 'POST':
        api_url = 'https://icanhazdadjoke.com/'
        headers = {'Accept': 'application/json'}
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            joke = response.json().get("joke")
            mood = request.form.get("mood").lower()
        else:
            error = f"Could not find mood '{mood}'. Try Another!"

    return render_template('joke_generator.html', mood=mood, error=error, moods=moods, joke=joke)


@app.route('/joke_search', methods=['GET', 'POST'])
def joke_search():
    error = None
    results = {}
    term = ''

    if request.method == 'POST':
        headers = {'Accept': 'application/json'}
        api_url = 'https://icanhazdadjoke.com/search'
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            print(response.json())
            results = response.json().get("results")
            term = request.form.get('term').lower()

            for joke in results:
                for i in joke:
                    i = results[i].get('joke')

        else:
            error = f"Could not find joke '{results}'. Try Another!"

    return render_template('joke_search.html', results=results, error=error, term=term, i=i)


if __name__ == '__main__':
    app.run(debug=True)
