from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def get_joke():
    # Call the public joke API
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
#    
#    # Convert the response into JSON format
    joke_data = response.json()
#
#    # Extract setup and punchline
    setup = joke_data['setup']
    punchline = joke_data['punchline']
#
#    # Pass the joke to the HTML template
    return render_template('joke.html', setup=setup, punchline=punchline)

if __name__ == '__main__':
    app.run(debug=True)