import unittest
from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Socrates", "Rock")
        self.player2 = Player("Plato", "Paper")
        self.player3 = Player("Aristotle", "Scissors")
        self.game1 = Game({self.player1.name: self.player1.move, self.player2.name: self.player2.move})

    def test_game_has_players(self):
        self.assertEqual({}, self.game1.players)



