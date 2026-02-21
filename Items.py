from typing import Dict, NamedTuple, TYPE_CHECKING
from BaseClasses import Item
from BaseClasses import ItemClassification as IC
from worlds.phoa import PhoaOptions
from worlds.phoa.Locations import PhoaLocationData

if TYPE_CHECKING:
    from .. import PhoaWorld


class PhoaItem(Item):
    game: str = "Phoenotopia: Awakening"


class PhoaItemData(NamedTuple):
    code: int
    amount: int
    type: IC


# @formatter:off
item_table: Dict[str, PhoaItemData] = {
    "Heart Ruby":               PhoaItemData(3,     3,  IC.useful),
    "Energy Gem":               PhoaItemData(4,     2,  IC.useful),
    "Moonstone":                PhoaItemData(5,     9,  IC.filler),
    "Life Saver":               PhoaItemData(14,    1,  IC.progression),
    "Slingshot":                PhoaItemData(30,    1,  IC.progression),
    "Bombs":                    PhoaItemData(31,    1,  IC.progression),
    "Crank Lamp":               PhoaItemData(32,    1,  IC.progression),  # Ignore light requirement option?
    "Sonic Spear":              PhoaItemData(33,    1,  IC.progression),
    "Fishing Rod":              PhoaItemData(40,    1,  IC.progression),  # Only if fishing spots are included?
    "Doki Herb":                PhoaItemData(45,    7,  IC.filler),
    "Pumpkin Muffin":           PhoaItemData(47,    1,  IC.filler),
    "Cooked Toad Leg":          PhoaItemData(49,    1,  IC.filler),
    "Berry Fruit":              PhoaItemData(50,    1,  IC.filler),
    "Perro Egg":                PhoaItemData(52,    2,  IC.filler),
    "Fruit Jam":                PhoaItemData(57,    1,  IC.filler),
    "Cheese":                   PhoaItemData(64,    1,  IC.filler),
    "Milk":                     PhoaItemData(67,    1,  IC.filler),
    "Anuri Pearlstone":         PhoaItemData(98,    10, IC.progression),  # Dungeon option?
    "Lunar Frog":               PhoaItemData(99,    1,  IC.filler),
    "Lunar Vase":               PhoaItemData(100,   1,  IC.filler),
    "Dandelion":                PhoaItemData(101,   4,  IC.filler),
    "Panselo Potato":           PhoaItemData(102,   2,  IC.filler),
    "Mystery Meat":             PhoaItemData(112,   18, IC.filler),
    "Mysterious Golem Head":    PhoaItemData(166,   1,  IC.filler),
    "Dragon's Scale":           PhoaItemData(185,   1,  IC.filler),
    "5 Rin":                    PhoaItemData(305,   1,  IC.filler),
    "9 Rin":                    PhoaItemData(309,   1,  IC.filler),
    "15 Rin":                   PhoaItemData(315,   2,  IC.filler),
    "20 Rin":                   PhoaItemData(320,   2,  IC.filler),
    "25 Rin":                   PhoaItemData(325,   1,  IC.filler),
    "35 Rin":                   PhoaItemData(335,   3,  IC.filler),
}
# @formatter:on

item_inclusion_priority: list[str] = \
    ["Energy Gem", "Heart Ruby", "Dragon's Scale", "35 Rin", "25 Rin", "20 Rin", "15 Rin", "Pumpkin Muffin",
     "Cooked Toad Leg", "Milk", "Cheese", "Panselo Potato", "Mystery Meat", "Fruit Jam", "Berry Fruit", "Perro Egg",
     "Doki Herb", "Dandelion", "9 Rin", "5 Rin", "Lunar Frog", "Lunar Vase", "Moonstone", "Mysterious Golem Head"]


def get_item_pool(world: "PhoaWorld", locations: dict[str, PhoaLocationData]) -> list[str]:
    # TODO: Handling for upgrade type items (eg. bats)
    # TODO: Starting items

    # Determine item classifications based on settings
    adjust_item_classifications(world.options)

    # Remove events from locations
    locations = {key: location for key, location in locations.items() if location.vanillaItem}
    location_count = len(locations)

    # Initialize item pools based on classifications
    progressive_items = []
    useful_items = []

    for item_name, item_data in item_table.items():
        if item_data.type == IC.progression:
            progressive_items.extend([item_name] * item_data.amount)
        elif item_data.type == IC.useful:  # and (item_name is not "Heart Ruby" or item_name is not "Energy Gem")
            useful_items.extend([item_name] * item_data.amount)

    items_from_locations: list[str] = [location.vanillaItem for location in locations.values()]

    # Check whether enough locations are available to place all progressive items
    if len(progressive_items) > location_count:
        raise ValueError(
            f"Not enough progress locations({str(location_count)}) "
            f"to place all progressive items({str(len(progressive_items))})"
        )

    # Remove progressive and useful items from the items_from_locations
    items_from_locations = [item for item in items_from_locations if item not in set(progressive_items)]
    items_from_locations = [item for item in items_from_locations if item not in set(useful_items)]

    # Sort items on importance
    def sort_by_priority(items, priority_list: list[str]) -> list[str]:
        priority_map = {item: i for i, item in enumerate(priority_list)}
        default_priority = len(priority_list)
        return sorted(items, key=lambda x: priority_map.get(x, default_priority))

    useful_items = sort_by_priority(useful_items, item_inclusion_priority)
    items_from_locations = sort_by_priority(items_from_locations, item_inclusion_priority)

    # Construct the item pool
    item_pool = progressive_items.copy()

    remaining_slots = location_count - len(item_pool)

    item_pool.extend(useful_items[:remaining_slots])
    remaining_slots = location_count - len(item_pool)

    item_pool.extend(items_from_locations[:remaining_slots])
    remaining_slots = location_count - len(item_pool)

    item_pool.extend(world.get_filler_item_name() for _ in range(remaining_slots))

    return item_pool


def adjust_item_classifications(options: PhoaOptions) -> None:
    pass  # TODO: Change item classifications based on included checks
