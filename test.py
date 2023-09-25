import pygame
import unittest
import numpy as np
from button import Button
from deck import Deck
from tile import Tile

class TestButton(unittest.TestCase):
    pygame.init()
    
    #Make a test function and button
    test_x = 40
    test_y = 50
    test_width = 60
    test_height = 70
    test_text = "CLICK ME"
    test_color = 'white'
    test_hover_color = 'grey'
    test_click_color = 'red'
    test_font_size = 30
    def temp_function(self):
        return True
    test_button = Button(test_x, test_y, test_width, test_height, test_text, temp_function, test_color, test_hover_color, test_click_color, test_font_size)
    
    def test_rect(self):
        self.assertIsInstance(TestButton.test_button.rect, pygame.Rect, "Button.rect is not using pygame's built in class")
        self.assertEqual(TestButton.test_button.rect.x, TestButton.test_x, "Button.rect.x does not match passed value")
        self.assertEqual(TestButton.test_button.rect.y, TestButton.test_y, "Button.rect.y does not match passed value")
        self.assertEqual(TestButton.test_button.rect.width, TestButton.test_width, "Button.rect.width does not match passed value")
        self.assertEqual(TestButton.test_button.rect.height, TestButton.test_height, "Button.rect.height does not match passed value")
        
    def test_colors(self):
        self.assertEqual(TestButton.test_button.button_color, TestButton.test_color, "Button.button_color does not match passed value")
        self.assertEqual(TestButton.test_button.click_color, TestButton.test_click_color, "Button.click_color does not match passed value")
        self.assertEqual(TestButton.test_button.hover_color, TestButton.test_hover_color, "Button.hover_color does not match passed value")
    
    def test_font(self):
        self.assertIsInstance(TestButton.test_button.font, pygame.font.Font, "Button.font is not using pygame's built in class")
        
    def test_click_function(self):
        self.assertTrue(TestButton.test_button.click_function)
        
class TestDeck(unittest.TestCase):
    pygame.init()
    
    test_deck_1 = Deck()
    test_deck_2 = Deck()
    
    def test_same_start(self):
        self.assertFalse(np.array_equal(TestDeck.test_deck_1.game_deck, TestDeck.test_deck_2.game_deck), "Initial shuffle results in the same order or tiles")\
    
    def test_drawTile(self):
        self.assertIsInstance(TestDeck.test_deck_1.drawTile(), Tile, "Function does not return a tile object")
        self.assertTrue(len(TestDeck.test_deck_1.game_deck) == (len(TestDeck.test_deck_2.game_deck) - 1), "Unexpected deck size after drawing tile")
        
    def test_empty_deck_draw(self):
        for i in range(len(TestDeck.test_deck_1.game_deck)):
            temp = TestDeck.test_deck_1.drawTile()
        try:
            TestDeck.test_deck_1.drawTile()
        except IndexError:
            self.assertTrue(False, "Crashed due to drawing tile from empty deck")
        
        self.assertTrue(True)
           

class TestTile(unittest.TestCase):
    pass

class TestMeeple(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()