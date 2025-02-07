from typing import Dict, NamedTuple

from BaseClasses import Location

class PhoaLocation(Location):
    game: str = "Phoenotopia Awakening"

class PhoaLocationData(NamedTuple):
    region: str
    address: int
    locked_by: tuple = None

access_logic: Dict[tuple] = {
    "Anuri Temple Access": (("Slingshot"), ("Bombs"))
}

location_data_table: Dict[str, PhoaLocationData] = {
    "Watchtower (East)": PhoaLocationData(
        region="Panselo Village",
        address=7676000,
        # Locked by Bat
    ), # Heart Ruby
    "Rutea's laboratory": PhoaLocationData(
        region="Panselo Village",
        address=7676001,
        locked_by=(("Slingshot"), ("Bombs")),
    ), # Heart Ruby
    "End of Secret Fishing Spot": PhoaLocationData(
        region="Panselo (Region)",
        address=7676002,
    ), # Energy Gem
    "Northeastern Treetops": PhoaLocationData(
        region="Panselo (Region)",
        address=7676005,
        locked_by=(("Slingshot"), ("Bombs")),
    ), # Moonstone
    "Underneath Boulder": PhoaLocationData(
        region="Panselo (Region)",
        address=7676006,
        locked_by=(("Bombs")),
    ), # Moonstone
    "Overworld Encounter Near Sunflower Road": PhoaLocationData(
        region="Panselo (Region)",
        address=7676007,
    ), # Moonstone
    "Cave Blocked by Destructable Blocks": PhoaLocationData(
        region="Doki Forest",
        address=7676008,
        locked_by=(("Bombs")),
    ), # Moonstone
    "On Top of Anuri Temple": PhoaLocationData(
        region="Doki Forest",
        address=7676009,
        locked_by=(("Sonic Spear")),
    ), # Moonstone
    "Fish Underneath Anuri Temple": PhoaLocationData(
        region="Doki Forest",
        address=7676011,
        locked_by=(("Fishing Rod")),
    ), # Dragon's Scale
    "Gift from Alex": PhoaLocationData(
        region="Doki Forest",
        address=7676027,
    ), # Lunar Vase
    "Tall Tower Puzzle Behind Locked Door": PhoaLocationData(
        region="Anuri Temple",
        address=7676003,
        locked_by=(access_logic.get("Anuri Temple Access")),
    ), # Heart Ruby
    "Carry Pot Across the Water and Bats": PhoaLocationData(
        region="Anuri Temple",
        address=7676004,
        locked_by=(access_logic.get("Anuri Temple Access")),
    ), # Energy Gem
    "Moveable Bridges Room": PhoaLocationData(
        region="Anuri Temple",
        address=7676012,
        locked_by=(access_logic.get("Anuri Temple Access")),
    ), # Moonstone
    "Stackable Pots Room": PhoaLocationData(
        region="Anuri Temple",
        address=7676013,
        locked_by=(access_logic.get("Anuri Temple Access")),
    ), # Moonstone
    "Fishing Spot After Slargummy": PhoaLocation (
        region="Anuri Temple",
        address=7676014,
        locked_by=(access_logic.get("Anuri Temple Access")),
    ), # Moonstone
    "Above Throne Past Destructable Wall": PhoaLocationData(
        region="Anuri Temple",
        address=7676010,
        locked_by=(access_logic.get("Anuri Temple Access")),
    ), # Moonstone
    "Within Sarcophagus": PhoaLocationData(
        region="Anuri Temple",
        address=7676015,
        locked_by=(access_logic.get("Anuri Temple Access")),
    ), # Moonstone
    "Skeleton Above First Gate": PhoaLocationData(
        region="Anuri Temple",
        address=7676016,
        locked_by=(access_logic.get("Anuri Temple Access")),
    ), # Anuri Pearlstone
    "Press the Switches with Pots and Fruits": PhoaLocationData(
        region="Anuri Temple",
        address=7676017,
        locked_by=(access_logic.get("Anuri Temple Access")),
    ), # Anuri Pearlstone
    "Maze with Scrabers": PhoaLocationData(
        region="Anuri Temple",
        address=7676018,
        locked_by=(access_logic.get("Anuri Temple Access")),
    ), # Anuri Pearlstone
    "Slingshot and Toads": PhoaLocationData(
        region="Anuri Temple",
        address=7676019,
        locked_by=(access_logic.get("Anuri Temple Access")),
    ), # Anuri Pearlstone
    "Three Switches With Lots of Pots": PhoaLocationData(
        region="Anuri Temple",
        address=7676020,
        locked_by=(access_logic.get("Anuri Temple Access")),
    ), # Anuri Pearlstone
    "Sprint-jump on Timed Switches": PhoaLocationData(
        region="Anuri Temple",
        address=7676021,
        locked_by=(access_logic.get("Anuri Temple Access")),
    ), # Anuri Pearlstone
    "Hit the Switch Hidden Under a Breakable Tomb": PhoaLocationData(
        region="Anuri Temple",
        address=7676022,
        locked_by=(access_logic.get("Anuri Temple Access")),
    ), # Anuri Pearlstone
    "Push the Metal Pot Onto the Switch From Above": PhoaLocationData(
        region="Anuri Temple",
        address=7676023,
        locked_by=(access_logic.get("Anuri Temple Access")),
    ), # Anuri Pearlstone
    "Defeat the Glowing Slargummy": PhoaLocationData(
        region="Anuri Temple",
        address=7676024,
        locked_by=(access_logic.get("Anuri Temple Access")),
    ), # Anuri Pearlstone
    "Use Slingshot to Hit the Switches Below": PhoaLocationData(
        region="Anuri Temple",
        address=7676025,
        locked_by=(access_logic.get("Anuri Temple Access")),
    ), # Lunar Frog
    "Dive in the Room Past Second Gate": PhoaLocationData(
        region="Anuri Temple",
        address=7676026,
        locked_by=(access_logic.get("Anuri Temple Access")),
    ), # Lunar Vase
}

location_table = {name: data.address for name, data in location_data_table.items()}