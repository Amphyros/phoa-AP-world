from typing import List
from BaseClasses import Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from .Options import PhoaOptions
from .Locations import PhoaLocation, location_data_table, location_table
from .Items import PhoaItem, item_data_table, item_table
from .Regions import region_data_table

class PhoaWebWorld(WebWorld):
    tutorials = Tutorial(
        tutorial_name="Start Guide",
        description="A guide to start playing Phoenotopia: Awakening in Archipelago",
        language="Engels",
        file_name="guide_en.md",
        link="guide/en",
        authors=["Lenamphy"]
    )

class PhoaWorld(World):
    game = "Phoenotopia: Awakening"
    web = PhoaWebWorld()
    # options: PhoaOptions
    options_dataclass = PhoaOptions
    location_name_to_id = location_table
    item_name_to_id = item_table

    def create_item(self, name: str) -> PhoaItem:
        return PhoaItem(name, item_data_table[name].type, item_data_table[name].code, self.player)
    
    def create_items(self) -> None:
        item_pool: List[PhoaItem] = []
        for name, item in item_data_table.items():
            if item.code:
                for _ in range(item.amount):
                    item_pool.append(self.create_item(name))
        
        self.multiworld.itempool += item_pool
    
    def create_regions(self):
        for region_name in region_data_table.keys():
            self.multiworld.regions.append(Region(region_name, self.player, self.multiworld))
        
        # Create Locations
        for region_name, region_data in region_data_table.items():
            region = self.get_region(region_name)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in location_data_table.items()
                if location_data.region == region_name
            }, PhoaLocation)
            region.add_exits(region_data_table[region_name].connecting_regions)

            # for location_name, location_data in 