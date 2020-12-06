import unittest
from app.models.game import Game
from app.models.games import *
from app.models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Socrates", "Rock")
        self.player2 = Player("Plato", "Paper")
        self.player3 = Player("Aristotle", "Scissors")
        self.game1 = Game([self.player1, self.player2])

    def test_game_has_players(self):
        self.assertEqual([], self.game1.players)

    def test_choose_rock_over_scissors(self):
        result = choose_winner(self.player1, self.player3)
        self.assertEqual(self.player1, result)
        
        result = choose_winner(self.player1, self.player2)
        self.assertEqual(self.player2, result)
        
    
    # def test_choose_rock_over_scissors_reversed(self):
    #     result = choose_winner(self.player3, self.player1)
    #     self.assertEqual(self.player1, result)

        



