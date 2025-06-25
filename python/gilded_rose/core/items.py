from .constants import MIN_QUALITY, MAX_QUALITY, LEGENDARY_QUALITY

"""Legacy Item class"""
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


"""Default behavior for items"""
class ItemBehavior:
    def update_quality(self, item: Item) -> None:
        self.calculate_sell_in(item)
        self.calculate_quality(item)

    def calculate_sell_in(self, item: Item) -> None:
        decrease_sell_in(item)

    def calculate_quality(self, item: Item) -> None:
        """Template method that enforces quality limits after calculation"""
        self._update_quality(item)
        self.enforce_quality_limits(item)

    def _update_quality(self, item: Item) -> None:
        """Hook method for subclasses to implement specific quality calculation"""
        if has_sell_deadline_passed(item.sell_in):
            decrease_item_quality_by_amount(item, 2)
        else:
            decrease_item_quality_by_amount(item, 1)
            
    def enforce_quality_limits(self, item: Item) -> None:
        if is_item_quality_above_max_quality(item.quality):
            set_item_quality_to_max_quality(item)
        if is_item_quality_below_min_quality(item.quality):
            set_item_quality_to_min_quality(item)


"""Behavior for legendary items"""
class LegendaryBehavior(ItemBehavior):
    def calculate_quality(self, item: Item) -> None:
        # Legendary items have a quality of 80 and never change
        set_item_quality_to_legendary_quality(item)
    
    def calculate_sell_in(self, item: Item) -> None:
        pass


"""Behavior for conjured items"""
class ConjuredBehavior(ItemBehavior):
    def _update_quality(self, item: Item) -> None:
        if has_sell_deadline_passed(item.sell_in):
            decrease_item_quality_by_amount(item, 4)
        else:
            decrease_item_quality_by_amount(item, 2)


"""Behavior for aged brie items"""
class AgedBrieBehavior(ItemBehavior):
    def _update_quality(self, item: Item) -> None:
        if has_sell_deadline_passed(item.sell_in):
            increase_item_quality_by_amount(item, 2)
        else:
            increase_item_quality_by_amount(item, 1)
        

"""Behavior for backstage passes items"""
class BackstagePassesBehavior(ItemBehavior):
    def _update_quality(self, item: Item) -> None:
        if has_sell_deadline_passed(item.sell_in):
            set_item_quality_to_min_quality(item)
        elif is_sell_deadline_within_5_days(item.sell_in):
            increase_item_quality_by_amount(item, 3)
        elif is_sell_deadline_within_10_days(item.sell_in):
            increase_item_quality_by_amount(item, 2)
        else:
            increase_item_quality_by_amount(item, 1)


# Helper functions            
def has_sell_deadline_passed(sell_in: int) -> bool:
    return sell_in < 0


def decrease_sell_in(item: Item) -> None:
    item.sell_in = item.sell_in - 1


def decrease_item_quality_by_amount(item: Item, amount: int) -> None:
    item.quality = item.quality - amount


def increase_item_quality_by_amount(item: Item, amount: int) -> None:
    item.quality = item.quality + amount


def is_sell_deadline_within_10_days(sell_in: int) -> bool:
    return sell_in < 10


def is_sell_deadline_within_5_days(sell_in: int) -> bool:
    return sell_in < 5


def is_item_quality_above_max_quality(quality: int) -> bool:
    return quality > MAX_QUALITY


def is_item_quality_below_min_quality(quality: int) -> bool:
    return quality < MIN_QUALITY


def set_item_quality_to_max_quality(item: Item) -> None:
    item.quality = MAX_QUALITY


def set_item_quality_to_min_quality(item: Item) -> None:
    item.quality = MIN_QUALITY


def set_item_quality_to_legendary_quality(item: Item) -> None:
    item.quality = LEGENDARY_QUALITY