# -*- coding: utf-8 -*-
import unittest

from gilded_rose.core.items import Item
from gilded_rose.quality_management.gilded_rose import GildedRose


class GildedRoseTest(unittest.TestCase):

    """Test that the quality of a common item is updated correctly"""
    def test_common_item_update_quality(self):
        items = [Item("Some Common Item", 2, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Some Common Item", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(9, items[0].quality)

    """Test that the quality of a common item is updated correctly when sell_in is negative"""
    def test_common_item_update_quality_when_sell_in_is_negative(self):
        items = [Item("Some Common Item", -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Some Common Item", items[0].name)
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    """Test that the quality of a common item is updated correctly when quality is at min"""
    def test_common_item_update_quality_when_quality_is_at_min(self):
        items = [Item("Some Common Item", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Some Common Item", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    """Test that the quality of a Aged Brie sulfuras item is updated correctly"""
    def test_common_item_update_when_ambigious_item_name(self):
        items = [Item("Aged Brie Sulfuras", 2, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie Sulfuras", items[0].name)
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    # TODO: Add more Unit Tests for other items
    
if __name__ == '__main__':
    unittest.main()
