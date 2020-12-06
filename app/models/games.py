from app.models.game import *
from app.models.player import *


player1 = Player("Socrates", "Rock")
player2 = Player("Plato", "Paper")
player3 = Player("Aristotle", "Scissors")
game1 = Game({player1, player2})

# def choose_winner(player1, player2):
#     if player1.move == "Rock" and player2.move == "Scissors":
#         return player1
#     if player1.move == "Scissors" and player2.move == "Paper":
#         return player1
#     if player1.move == "Paper" and player2.move == "Rock":
#         return player1

def choose_winner(player1, player2):
    if player1.move == "Rock" and player2.move == "Scissors":
        return player1
    if player1.move == "Scissors" and player2.move == "Paper":
        return player1
    else:
        return player2
    
