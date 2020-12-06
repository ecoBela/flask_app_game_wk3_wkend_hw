from app import app
from app.models.games import *


@app.route('/')
def index():
    return "Welcome to Rock, Paper, Scissors!"

@app.route('/winner/rock/scissors')
def winner():
    return f"{player1.name} chose {player1.move} and is the winner!"

@app.route('/draw/rock/rock')
def draw():
    return f"{player1.name} and {player4.name} made the same move. It's a draw!"


