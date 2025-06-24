
import pytest
from gilded_rose import Item, GildedRose

def test_foo(standard_item):
    """Test that demonstrates the basic test structure."""
    gilded_rose = GildedRose([standard_item])
    gilded_rose.update_quality()
    assert standard_item.quality >= 0, "Quality should never be negative"
    assert standard_item.name == "standard item"
