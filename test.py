import pygame
import unittest
import numpy as np
from button import Button
from deck import Deck
from tile import Tile


class TestTile(unittest.TestCase):
    pygame.init()
    test_x = 50
    test_y = 50
    test_image_path = 'TileAssets/Tile1_4.png'
    test_tile = Tile(x=test_x, y=test_y, image_path=test_image_path)

    def test_rect(self):
        self.assertIsInstance(TestTile.test_tile.rect, pygame.Rect,"Button.rect is not using pygame's built in class")
        self.assertEqual(TestTile.test_tile.rect.x, TestTile.test_x, "Button.rect.x does not match passed value")

    def test_image(self):
        self.assertEqual(TestTile.test_tile.rect.y, TestTile.test_y, "Button.rect.y does not match passed value")

    def test_image(self):
        self.assertEqual(TestTile.test_tile.image_path, TestTile.test_image_path, "Tile image path does not match")


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
        
    def test_update_text(self):
        TestButton.test_button.update_text(69)
        self.assertEqual('Draw Tile (69)', TestButton.test_button.text)
        
class TestDeck(unittest.TestCase):
    pygame.init()
    
    test_deck_1 = Deck()
    test_deck_2 = Deck()
    
    def test_num_tiles(self):
        self.assertEqual(len(TestDeck.test_deck_2.game_deck), 72, "Deck does not have the correct number of starting tiles")
        
    def test_tile1_4(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile1_4.png':
                num = num + 1
        self.assertEqual(num, 4, "Incorrect amount of Tile1_4 in deck")
        
    def test_tile2_2(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile2_2.png':
                num = num + 1
        self.assertEqual(num, 2, "Incorrect amount of Tile2_2 in deck")
        
    def test_tile3_8(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile3_8.png':
                num = num + 1
        self.assertEqual(num, 8, "Incorrect amount of Tile3_8 in deck")
        
    def test_tile4_9(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile4_9.png':
                num = num + 1
        self.assertEqual(num, 9, "Incorrect amount of Tile4_9 in deck")
        
    def test_tile5_4(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile5_4.png':
                num = num + 1
        self.assertEqual(num, 4, "Incorrect amount of Tile5_4 in deck")
        
    def test_tile6_1(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile6_1.png':
                num = num + 1
        self.assertEqual(num, 1, "Incorrect amount of Tile6_1 in deck")
        
    def test_tile7_5(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile7_5.png':
                num = num + 1
        self.assertEqual(num, 5, "Incorrect amount of Tile7_5 in deck")
        
        
    def test_tile8_4(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile8_4.png':
                num = num + 1
        self.assertEqual(num, 4, "Incorrect amount of Tile8_4 in deck")
        
    def test_tile9_3(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile9_3.png':
                num = num + 1
        self.assertEqual(num, 3, "Incorrect amount of Tile9_3 in deck")
        
    def test_tile10_3(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile10_3.png':
                num = num + 1
        self.assertEqual(num, 3, "Incorrect amount of Tile10_3 in deck")
    
    def test_tile11_3(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile11_3.png':
                num = num + 1
        self.assertEqual(num, 3, "Incorrect amount of Tile11_3 in deck")
        
    def test_tile12_1(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile12_1.png':
                num = num + 1
        self.assertEqual(num, 1, "Incorrect amount of Tile12_1 in deck")
        
    def test_tile13_3(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile13_3.png':
                num = num + 1
        self.assertEqual(num, 3, "Incorrect amount of Tile13_3 in deck")
        
    def test_tile14_3(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile14_3.png':
                num = num + 1
        self.assertEqual(num, 3, "Incorrect amount of Tile14_3 in deck")
    
    def test_tile15_2(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile15_2.png':
                num = num + 1
        self.assertEqual(num, 2, "Incorrect amount of Tile15_2 in deck")
        
    def test_tile16_3(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile16_3.png':
                num = num + 1
        self.assertEqual(num, 3, "Incorrect amount of Tile16_3 in deck")
    
    def test_tile17_2(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile17_2.png':
                num = num + 1
        self.assertEqual(num, 2, "Incorrect amount of Tile17_2 in deck")
    
    def test_tile18_2(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile18_2.png':
                num = num + 1
        self.assertEqual(num, 2, "Incorrect amount of Tile18_2 in deck")
        
    def test_tile19_2(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile19_2.png':
                num = num + 1
        self.assertEqual(num, 2, "Incorrect amount of Tile19_2 in deck")
    
    def test_tile20_3(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile20_3.png':
                num = num + 1
        self.assertEqual(num, 3, "Incorrect amount of Tile20_3 in deck")
        
    def test_tile21_1(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile21_1.png':
                num = num + 1
        self.assertEqual(num, 1, "Incorrect amount of Tile21_1 in deck")
        
    def test_tile22_1(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile22_1.png':
                num = num + 1
        self.assertEqual(num, 1, "Incorrect amount of Tile22_1 in deck")
        
    def test_tile23_2(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile23_2.png':
                num = num + 1
        self.assertEqual(num, 2, "Incorrect amount of Tile23_2 in deck")
        
    def test_tile24_1(self):
        num = 0
        for i in TestDeck.test_deck_2.game_deck:
            if i.image_path == 'TileAssets\Tile24_1.png':
                num = num + 1
        self.assertEqual(num, 1, "Incorrect amount of Tile24_1 in deck")
        
    
    
    def test_same_start(self):
        self.assertFalse(np.array_equal(TestDeck.test_deck_1.game_deck, TestDeck.test_deck_2.game_deck), "Initial shuffle results in the same order or tiles")
    
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
           
class TestMeeple(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()