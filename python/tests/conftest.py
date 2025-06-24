import pytest
from gilded_rose import Item, GildedRose

@pytest.fixture
def standard_item():
    """Fixture that returns a standard item with default values."""
    return Item("standard item", 10, 20)

@pytest.fixture
def aged_brie():
    """Fixture that returns an Aged Brie item."""
    return Item("Aged Brie", 2, 0)

@pytest.fixture
def sulfuras():
    """Fixture that returns a Sulfuras item."""
    return Item("Sulfuras, Hand of Ragnaros", 0, 80)

@pytest.fixture
def backstage_pass():
    """Fixture that returns a Backstage Pass item."""
    return Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)

@pytest.fixture
def gilded_rose(request):
    """Fixture that returns a GildedRose instance with specified items."""
    if hasattr(request, 'param'):
        items = request.param
    else:
        items = []
    return GildedRose(items)
