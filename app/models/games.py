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
        return f"{player1.name} chose {player1.move} and is the winner!"
    if player1.move == "Scissors" and player2.move == "Paper":
        return f"{player1.name} chose {player1.move} and is the winner!"
    if player1.move == player2.move:
        return f"{player1.name} and {player2.name} made the same move. It's a draw!"
    else:
        return f"{player2.name} chose {player2.move} and is the winner!"
    
