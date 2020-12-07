from flask import render_template
from app import app
from app.models.player import Player
from app.models.game import Game
from app.models.games import games, players, choose_winner


@app.route('/')
def index():
    return render_template('index.html', title = 'Home:', players=players, games=games )

# @app.route('/winner/rock/scissors')
# def winner():
#     return f"{player1.name} chose {player1.move} and is the winner!"

# @app.route('/draw/rock/rock')
# def draw():
#     return f"{player1.name} chose {player1.move} and {player4.name} chose {player4.move} so it's a DRAW! Whoop whoop!"


@app.route('/choose_a_winner/<player1><player2>')
def choose_a_winner(player1, player2):
    return choose_winner(player1, player2)

