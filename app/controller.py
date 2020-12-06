from flask import render_template
from app import app
from app.models.player import Player
from app.models.games import *
from app.models.game import Game


@app.route('/')
def index():
    return render_template('index.html', title = 'Home:')


# @app.route('/winner/<play1>/<play2>')
# def winner(play1, play2):
#     return f"{player1.name} chose {player1.move} and is the winner!"

# @app.route('/draw/rock/rock')
# def draw():
#     return f"{player1.name} chose {player1.move} and {player4.name} chose {player4.move} so it's a DRAW! Whoop whoop!"

# @app.route('/game/<player1>/<player2>')
# def choose(player1, player2):
#     return f"The winner is {choose_winner(player1, player2)}"