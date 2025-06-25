from .items import (
    Item,
    ItemBehavior,
    LegendaryBehavior,
    AgedBrieBehavior,
    BackstagePassesBehavior,
    ConjuredBehavior
)
from .constants import (
    SULFURAS_IDENTIFIER,
    AGED_BRIE_IDENTIFIER,
    BACKSTAGE_PASSES_IDENTIFIER,
    CONJURED_IDENTIFIER
)
from typing import Type

"""
Factory for creating different types of item behaviors based on their names.
"""
class BehaviorFactory:

    ITEM_BEHAVIORS: dict[str, Type[ItemBehavior]] = {
        SULFURAS_IDENTIFIER: LegendaryBehavior,
        AGED_BRIE_IDENTIFIER: AgedBrieBehavior,
        BACKSTAGE_PASSES_IDENTIFIER: BackstagePassesBehavior,
        CONJURED_IDENTIFIER: ConjuredBehavior
    }

    @staticmethod
    def get_behavior(item: Item) -> ItemBehavior:
        for pattern, behavior_class in BehaviorFactory.ITEM_BEHAVIORS.items():
            if pattern in item.name:
                return behavior_class()
        
        return ItemBehavior()