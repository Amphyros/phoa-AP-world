from BaseClasses import Tutorial, ItemClassification, Item
from worlds.AutoWorld import WebWorld, World
from .Options import PhoaOptions
from .Locations import PhoaLocation, get_location_data
from .Items import PhoaItem, item_table, PhoaItemData, get_item_pool
from .Regions import create_regions_and_locations


class PhoaWebWorld(WebWorld):
    tutorials = [Tutorial(
        tutorial_name="Start Guide",
        description="A guide to start playing Phoenotopia: Awakening in Archipelago",
        language="English",
        file_name="setup_en.md",
        link="guide/en",
        authors=["Lenamphy"]
    )]


class PhoaWorld(World):
    game = "Phoenotopia: Awakening"
    web = PhoaWebWorld()
    options: PhoaOptions
    options_dataclass = PhoaOptions
    location_name_to_id = {name: data.address for name, data in get_location_data(-1, None).items()}
    item_name_to_id = {name: data.code for name, data in item_table.items()}

    def create_item(self, name: str) -> PhoaItem:
        return PhoaItem(name, item_table[name].type, item_table[name].code, self.player)

    def create_items(self):
        self.create_and_assign_event_items()

        item_pool_strings: list[str] = get_item_pool(self, get_location_data(self.player, self.options))
        item_pool: list[PhoaItem] = []

        for item_name in item_pool_strings:
            item_pool.append(self.create_item(item_name))

        self.multiworld.itempool += item_pool

    def create_regions(self):
        create_regions_and_locations(self.multiworld, self.player, self.options)

    def set_rules(self):
        self.multiworld.completion_condition[self.player] = lambda state: state.has(
            "Strange Urn", self.player
        )

    def get_filler_item_name(self) -> str:
        return '20 Rin'

    def create_and_assign_event_items(self):
        for location in self.multiworld.get_locations(self.player):
            if location.address is None:
                location.place_locked_item(
                    Item(location.name, ItemClassification.progression, None, self.player))

    def fill_slot_data(self):
        return {
            "DeathLink": self.options.death_link.value,
        }
