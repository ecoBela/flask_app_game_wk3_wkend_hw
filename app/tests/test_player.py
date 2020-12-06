import unittest
from app.models.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Socrates", "Rock")
        self.player2 = Player("Plato", "Paper")
        self.player3 = Player("Aristotle", "Scissors")

    def test_player_has_name(self):
        self.assertEqual("Socrates", self.player1.name)

    def test_player_has_a_move(self):
        self.assertEqual("Rock", self.player1.move)


