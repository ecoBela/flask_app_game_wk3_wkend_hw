from app.models.game import *
from app.models.player import *


player1 = Player("Socrates", "Rock")
player2 = Player("Plato", "Paper")
player3 = Player("Aristotle", "Scissors")
player4 = Player("Captain Marvel", "Rock")
players = [player1, player2, player3, player4]

game1 = Game([player1, player2])
game2 = Game([player1, player3])
game3 = Game([player2, player3])
game4 = Game([player1, player4])
games = [game1, game2, game3, game4]

def add_new_game(game):
    games.append(game)


def choose_winner(player1, player2):
    if player1.move == "Rock" and player2.move == "Scissors":
        return f"{player1.name} chose {player1.move} and is the winner!"
    if player1.move == "Scissors" and player2.move == "Paper":
        return f"{player1.name} chose {player1.move} and is the winner!"
    if player1.move == player2.move:
        return f"{player1.name} and {player4.name} made the same move. It's a draw!"
    else:
        return f"{player2.name} chose {player2.move} and is the winner!"
    
