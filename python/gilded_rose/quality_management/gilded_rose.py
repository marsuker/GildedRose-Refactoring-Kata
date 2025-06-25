from gilded_rose.core.item_factory import BehaviorFactory

"""
GildedRose is the main class that manages the quality of items.
"""
class GildedRose(object):
    
    """
    Initialize the GildedRose with a list of items.
    Assign a behavior to each item based on its name.
    """
    def __init__(self, items):
        self.items = items
        self.behaviors = {item: BehaviorFactory.get_behavior(item) for item in items}

    """
    Update the quality of each item based on its behavior.
    """
    def update_quality(self):
        for item in self.items:
            behavior = self.behaviors[item]
            behavior.update_quality(item)
    
    