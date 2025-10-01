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
        code=3,
        type=ItemClassification.useful,
        amount=3,
    ),
    "Energy Gem": PhoaItemData(
        code=4,
        type=ItemClassification.useful,
        amount=2,
    ),
    "Moonstone": PhoaItemData(
        code=5,
        # type=ItemClassification.progression,
        amount=4,
    ), # Actual amount is 9 (-5 for progression items)
    "Dragon's Scale": PhoaItemData(
        code=185,
    ),
    "Anuri Pearlstone": PhoaItemData(
        code=98,
        type=ItemClassification.progression,
        amount=10
    ),
    "Lunar Frog": PhoaItemData(
        code=99,
    ),
    "Lunar Vase": PhoaItemData(
        code=100
    ),
    "Slingshot": PhoaItemData(
        code=30,
        type=ItemClassification.progression,
    ),
    "Bombs": PhoaItemData(
        code=31,
        type=ItemClassification.progression,
    ),
    "Fishing Rod": PhoaItemData(
        code=40,
        type=ItemClassification.progression,
    ),
    "Life Saver": PhoaItemData(
        code=14,
        type=ItemClassification.progression,
    ),
    "Crank Lamp": PhoaItemData(
        code=32,
        type=ItemClassification.progression,
    ),
    # "Sonic Spear": PhoaItemData(
    #     code=7676012,
    #     type=ItemClassification.progression,
    # ),
}

item_table = {name: data.code for name, data in item_data_table.items()}
