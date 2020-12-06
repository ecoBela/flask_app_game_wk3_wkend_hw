from app.models.game import *
from app.models.player import *


player1 = Player("Socrates", "Rock")
player2 = Player("Plato", "Paper")
player3 = Player("Aristotle", "Scissors")
game1 = Game({player1, player2})