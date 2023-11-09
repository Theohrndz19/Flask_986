from flask import Flask
import random

app = Flask(__name__)

fact = ['9 dari 10 poeple playing Mobile Legends!',
         'Zlatan Ibrahimovic still the GOAT',
         'This world would be disaster by Nature!',
         'The best sold Windows is Windows XP']

@app.route('/')
def home():
    return "<h1>Blank Website</h1><a href='random_fact'>Click me!</a>"

@app.route("/random_fact")
def hello_world():
    return f"<h1>Hello entire world!</h1><p>{random.choice(fact)}</p>"

app.run(debug=True)