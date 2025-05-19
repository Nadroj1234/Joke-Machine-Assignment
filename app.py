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
        print(response.status_code)

        if response.status_code == 200:
            joke = response.json().get("joke")
            mood = request.form.get("mood").lower()
        else:
            error = f"Could not find mood '{mood}'. Try Another!"

    return render_template('joke_generator.html', mood=mood, error=error, moods=moods, joke=joke)


@app.route('/joke_search')
def joke_search():
    error = None
    joke = []
    if request.method == 'POST':
        joke = request.form.get('joke').lower()
        api_url = f'https://icanhaz/dadjoke.com/search '
        response = requests.get(api_url)

        if response.status_code == 200 and response.json().get('status') == 'success':
            joke = response.json()['message']
        else:
            error = f"Could not find breed '{joke}'. Try Another!"

    return render_template('joke_search.html', joke=joke, error=error)


if __name__ == '__main__':
    app.run(debug=True)
