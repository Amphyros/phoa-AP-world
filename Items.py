from typing import Dict, NamedTuple
from BaseClasses import Item, ItemClassification


class PhoaItem(Item):
    game: str = "Phoenotopia: Awakening"


class PhoaItemData(NamedTuple):
    code: int
    type: ItemClassification = ItemClassification.filler
    amount: int = 1


item_data_table: Dict[str, PhoaItemData] = {
    "Heart Ruby": PhoaItemData(
        code=7676000,
        amount=3,
    ),
    "Energy Gem": PhoaItemData(
        code=7676001,
        amount=2,
    ),
    "Moonstone": PhoaItemData(
        code=7676002,
        type=ItemClassification.progression,
        amount=5,
    ), # Actual amount is 10 (-5 for progression items)
    "Dragon's Scale": PhoaItemData(
        code=7676003,
    ),
    "Anuri Pearlstone": PhoaItemData(
        code=7676004,
        type=ItemClassification.progression,
        amount=9
    ),
    "Lunar Frog": PhoaItemData(
        code=7676005,
    ),
    "Lunar Vase": PhoaItemData(
        code=7676006
    ),
    "Slingshot": PhoaItemData(
        code=7676007,
        type=ItemClassification.progression,
    ),
    "Bombs": PhoaItemData(
        code=7676008,
        type=ItemClassification.progression,
    ),
    "Fishing Rot": PhoaItemData(
        code=7676009,
        type=ItemClassification.progression,
    ),
    "Life Saver": PhoaItem(
        code=7676010,
        type=ItemClassification.progression,
    ),
    "Crank Lamp": PhoaItem(
        code=7676011,
        type=ItemClassification.progression,
    ),
}

item_table = {name: data.code for name, data in item_data_table.items()}
