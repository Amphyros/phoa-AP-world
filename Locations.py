from enum import Flag, auto
from typing import Dict, NamedTuple, Optional, Callable

from BaseClasses import Location, CollectionState
from worlds.phoa import PhoaOptions
from worlds.phoa.LogicExtensions import PhoaLogic


class PhoaFlag(Flag):
    DEFAULT = auto()
    NPCGIFTS = auto()
    MISC = auto()
    SHOPSANITY = auto()
    SMALLANIMALS = auto()
    RINCHESTS = auto()
    RINCONTAINERS = auto()


class PhoaLocation(Location):
    game: str = "Phoenotopia: Awakening"


class PhoaLocationData(NamedTuple):
    region: str
    address: Optional[int]
    rule: Optional[Callable[[CollectionState], bool]] = None
    flags: PhoaFlag = PhoaFlag.DEFAULT


def get_location_data(player: Optional[int], options: Optional[PhoaOptions]) -> Dict[str, PhoaLocationData]:
    logic = PhoaLogic(player)

    locations: Dict[str, PhoaLocationData] = {
        "Panselo Village - Watchtower (West) - Chest": PhoaLocationData(
            region="panselo_village",
            address=7676061,
            flags=PhoaFlag.RINCHESTS,
        ),  # 35 Rin
        "Panselo Village - Watchtower (West) - Hidden in box": PhoaLocationData(
            region="panselo_village",
            address=7676031,
            flags=PhoaFlag.MISC,
        ),  # Cheese
        "Panselo Village - Watchtower (West) - Lizard": PhoaLocationData(
            region="panselo_village",
            address=7676041,
            flags=PhoaFlag.SMALLANIMALS,
        ),  # Mystery Meat
        "Panselo Village - Free Gift from Panselo Shop Keeper Tao": PhoaLocationData(
            region="panselo_village",
            address=7676070,
            flags=PhoaFlag.NPCGIFTS,
        ),  # Fruit Jam
        "Panselo Village - Panselo Shop Item 1": PhoaLocationData(
            region="panselo_village",
            address=7676072,
            flags=PhoaFlag.SHOPSANITY,
        ),  # Perro egg
        "Panselo Village - Panselo Shop Item 2": PhoaLocationData(
            region="panselo_village",
            address=7676073,
            flags=PhoaFlag.SHOPSANITY,
        ),  # Milk
        "Panselo Village - Panselo Shop Item 3": PhoaLocationData(
            region="panselo_village",
            address=7676074,
            flags=PhoaFlag.SHOPSANITY,
        ),  # Panselo Potato
        "Panselo Village - Inside coop": PhoaLocationData(
            region="panselo_village",
            address=7676030,
            flags=PhoaFlag.MISC,
        ),  # Perro egg
        "Panselo Village - Orphanage roof": PhoaLocationData(
            region="panselo_village",
            address=7676028,
            flags=PhoaFlag.MISC,
        ),  # Dandelion
        "Panselo Village - On table in girl's room": PhoaLocationData(
            region="panselo_village",
            address=7676032,
            flags=PhoaFlag.MISC,
        ),  # Berry Fruit
        "Panselo Village - Pot in boys Room": PhoaLocationData(
            region="panselo_village",
            address=7676058,
            flags=PhoaFlag.RINCONTAINERS,
        ),  # 5 Rin
        "Panselo Village - Box at right side of orphanage hall": PhoaLocationData(
            region="panselo_village",
            address=7676059,
            flags=PhoaFlag.RINCONTAINERS,
        ),  # 9 Rin
        "Panselo Village - Orphanage attic chest": PhoaLocationData(
            region="panselo_village",
            address=7676060,
            flags=PhoaFlag.RINCHESTS,
        ),  # 35 Rin
        "Panselo Village - Nana's Pumpkin Muffin": PhoaLocationData(
            region="panselo_village",
            address=7676068,
            flags=PhoaFlag.NPCGIFTS,
        ),  # Pumpkin Muffin
        "Panselo Village - Warehouse Chest": PhoaLocationData(
            region="panselo_village",
            address=7676062,
            flags=PhoaFlag.RINCHESTS,
        ),  # 25 Rin
        "Panselo Village - Jon's Potato": PhoaLocationData(
            region="panselo_village",
            address=7676069,
            flags=PhoaFlag.NPCGIFTS,
        ),  # Panselo Potato
        "Panselo Village - On roof next to Stan": PhoaLocationData(
            region="panselo_village",
            address=7676029,
            flags=PhoaFlag.MISC,
        ),  # Dandelion
        "Panselo Village - Rutea's room": PhoaLocationData(
            region="panselo_village",
            address=7676001,
            rule=lambda state: state.has_any({"Slingshot", "Bombs"}, player),
        ),  # Heart Ruby
        "Panselo Village - Watchtower (East) item up top": PhoaLocationData(
            region="panselo_village",
            address=7676000,
            # Locked by Bat
        ),  # Heart Ruby
        "Panselo Region - End of secret fishing spot": PhoaLocationData(
            region="panselo_region",
            address=7676002,
        ),  # Energy Gem
        "Panselo Region - Franway roof": PhoaLocationData(
            region="panselo_region",
            address=7676034,
            flags=PhoaFlag.MISC,
        ),  # Dandelion
        "Panselo Region - GEO house roof": PhoaLocationData(
            region="panselo_region",
            address=7676033,
            flags=PhoaFlag.MISC,
        ),  # Dandelion
        "Panselo Region - Overworld encounter near Sunflower Road": PhoaLocationData(
            region="panselo_region",
            address=7676005,
            rule=lambda state: state.has_any({"Slingshot", "Bombs"}, player),
        ),  # Moonstone
        "Panselo Region - Underneath boulder north of Panselo": PhoaLocationData(
            region="panselo_region",
            address=7676004,
            rule=lambda state: state.has("Bombs", player),
        ),  # Moonstone
        "Panselo Region - Northeastern treetops": PhoaLocationData(
            region="panselo_region",
            address=7676003,
            rule=lambda state: state.has_any({"Slingshot", "Bombs"}, player),
        ),  # Moonstone
        "Doki Forest - Cave guarded by Gummies - First item": PhoaLocationData(
            region="panselo_region",
            address=7676035,
            flags=PhoaFlag.MISC,
        ),  # Doki Herb
        "Doki Forest - Cave guarded by Gummies - Second item": PhoaLocationData(
            region="panselo_region",
            address=7676036,
            flags=PhoaFlag.MISC,
        ),  # Doki Herb
        "Doki Forest - Cave guarded by Gummies - Third item": PhoaLocationData(
            region="panselo_region",
            address=7676037,
            flags=PhoaFlag.MISC,
        ),  # Doki Herb
        "Doki Forest - Cave guarded by Gummies - Lizard": PhoaLocationData(
            region="panselo_region",
            address=7676042,
            flags=PhoaFlag.SMALLANIMALS,
        ),  # Mystery Meat
        "Doki Forest - Lizard at climbable roots": PhoaLocationData(
            region="panselo_region",
            address=7676043,
            flags=PhoaFlag.SMALLANIMALS,
        ),  # Mystery Meat
        "Doki Forest - Cave blocked by destructable blocks": PhoaLocationData(
            region="panselo_region",
            address=7676006,
            rule=lambda state: state.has("Bombs", player),
        ),  # Moonstone
        "Doki Forest - Chest through crawl space": PhoaLocationData(
            region="panselo_region",
            address=7676063,
            flags=PhoaFlag.RINCHESTS,
        ),  # 35 Rin
        "Doki Forest - Lizard in alcove": PhoaLocationData(
            region="panselo_region",
            address=7676044,
            flags=PhoaFlag.SMALLANIMALS,
        ),  # Mystery Meat
        "Doki Forest - Campfire cave - First Lizard": PhoaLocationData(
            region="panselo_region",
            address=7676045,
            flags=PhoaFlag.SMALLANIMALS,
        ),  # Mystery Meat
        "Doki Forest - Campfire cave - Second Lizard": PhoaLocationData(
            region="panselo_region",
            address=7676046,
            flags=PhoaFlag.SMALLANIMALS,
        ),  # Mystery Meat
        "Doki Forest - Fish underneath Anuri Temple": PhoaLocationData(
            region="panselo_region",
            address=7676007,
            rule=lambda state: state.has("Fishing Rod", player),
        ),  # Dragon's Scale
        "Doki Forest - Gift from Seth": PhoaLocationData(
            region="panselo_region",
            address=7676071,
            flags=PhoaFlag.NPCGIFTS,
        ),  # Mystery Meat
        "Doki Forest - Gift from Alex": PhoaLocationData(
            region="panselo_region",
            address=7676008,
        ),  # Slingshot
        # "On Top of Anuri Temple": PhoaLocationData(
        #     region="Overworld",
        #     address=7676009,
        #     rule=lambda state: state.has("Sonic Spear", player),
        # ), # Moonstone
        "Anuri Temple - Lizard at top of climbable vines at entrance": PhoaLocationData(
            region="anuri_temple(main_entrance)",
            address=7676047,
            flags=PhoaFlag.SMALLANIMALS,
        ),  # Mystery Meat
        "Anuri Temple - Skeleton above first gate": PhoaLocationData(
            region="anuri_temple(main_entrance)",
            address=7676009,
        ),  # Anuri Pearlstone
        "Anuri Temple - Lizard behind Bombable Blocks": PhoaLocationData(
            region="anuri_temple(top_floor)",
            address=7676048,
            flags=PhoaFlag.SMALLANIMALS,
        ),  # Mystery Meat
        "Anuri Temple - Time the gates through Scaber funnel": PhoaLocationData(
            region="anuri_temple(scaber_switch_maze)",
            address=7676024,
        ),  # Moonstone
        "Anuri Temple - Lizard left of Anuri throne": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676050,
            flags=PhoaFlag.SMALLANIMALS,
        ),  # Mystery Meat
        "Anuri Temple - Lizard right of Anuri throne": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676049,
            flags=PhoaFlag.SMALLANIMALS,
        ),  # Mystery Meat
        "Anuri Temple - Fight toads in treasure room": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676016,
        ),  # Lunar Vase
        "Anuri Temple - Lizard at the end of treasure room": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676051,
            flags=PhoaFlag.SMALLANIMALS,
        ),  # Mystery Meat
        "Anuri Temple - Scabers maze": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676010,
        ),  # Anuri Pearlstone
        # "Anuri Temple - High up pot in Scabers maze": PhoaLocationData(
        #     region="anuri_temple(main)",
        #     address=7676066,
        #     flags=PhoaFlag.RINCONTAINERS,
        #     rule=lambda state: state.has_any({"Slingshot", "Bombs"}, player),
        # ),  # 15 Rin
        "Anuri Temple - Press the switches with pots and fruits": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676011,
            rule=lambda state: state.has("Slingshot", player),
        ),  # Anuri Pearlstone
        "Anuri Temple - Side entrance room - First Lizard": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676055,
            flags=PhoaFlag.SMALLANIMALS,
        ),  # Mystery Meat
        "Anuri Temple - Carry pot across the water steps": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676012,
        ),  # Energy Gem
        "Anuri Temple - Lizard in water steps room": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676054,
            flags=PhoaFlag.SMALLANIMALS,
        ),  # Mystery Meat
        "Anuri Temple - Stackable pots room - Hidden item": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676013,
        ),  # Moonstone
        "Anuri Temple - Stackable pots room - Lizard": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676053,
            flags=PhoaFlag.SMALLANIMALS,
        ),  # Mystery Meat
        "Anuri Temple - Stackable pots room - Anuri Skeleton": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676065,
            flags=PhoaFlag.RINCONTAINERS,
        ),  # 15 Rin
        "Anuri Temple - Sprint-jump on timed switches": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676014,
        ),  # Anuri Pearlstone
        "Anuri Temple - Hit three switches in many pots room": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676019,
        ),  # Anuri Pearlstone
        "Anuri Temple - Skeleton at bottom of right elevator room": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676064,
            flags=PhoaFlag.RINCONTAINERS,
        ),  # 15 Rin
        "Anuri Temple - Side entrance room - Second Lizard": PhoaLocationData(
            region="anuri_temple(side_entrance)",
            address=7676056,
            flags=PhoaFlag.SMALLANIMALS,
        ),  # Mystery Meat
        "Anuri Temple - Side entrance first item": PhoaLocationData(
            region="anuri_temple(side_entrance)",
            address=7676038,
            flags=PhoaFlag.MISC,
        ),  # Doki Herb
        "Anuri Temple - Side entrance second item": PhoaLocationData(
            region="anuri_temple(side_entrance)",
            address=7676039,
            flags=PhoaFlag.MISC,
        ),  # Doki Herb
        "Anuri Temple - Moveable bridges room": PhoaLocationData(
            region="anuri_temple(moveable_bridge_area)",
            address=7676017,
        ),  # Moonstone
        "Anuri Temple - Lizard in movable bridge room": PhoaLocationData(
            region="anuri_temple(moveable_bridge_area)",
            address=7676052,
            flags=PhoaFlag.SMALLANIMALS,
        ),  # Mystery Meat
        "Anuri Temple - Slingshot the switch and surfacing Toads": PhoaLocationData(
            region="anuri_temple(moveable_bridge_area)",
            address=7676018,
            rule=lambda state: state.has("Slingshot", player),
        ),  # Anuri Pearlstone
        "Anuri Temple - Tall tower puzzle behind locked door": PhoaLocationData(
            region="anuri_temple(tall_tower_puzzle_room)",
            address=7676015,
        ),  # Heart Ruby
        "Anuri Temple - Tall tower puzzle side item": PhoaLocationData(
            region="anuri_temple(tall_tower_puzzle_room)",
            address=7676040,
            flags=PhoaFlag.MISC,
        ),  # Doki Herb
        "Anuri Temple Basement - Hit the switch hidden under breakable tomb": PhoaLocationData(
            region="anuri_temple(basement)",
            address=7676020,
            rule=lambda state: state.has("Bombs", player),
        ),  # Anuri Pearlstone
        "Anuri Temple Basement - Push metal pot onto switch from above": PhoaLocationData(
            region="anuri_temple(basement)",
            address=7676021,
        ),  # Anuri Pearlstone
        "Anuri Temple Basement - Within sarcophagus": PhoaLocationData(
            region="anuri_temple(basement)",
            address=7676022,
            rule=lambda state: state.has("Bombs", player),
        ),  # Moonstone
        "Anuri Temple Basement - Defeat the glowing slargummy": PhoaLocationData(
            region="anuri_temple(basement)",
            address=7676023,
            rule=lambda state: state.has("Crank Lamp", player),
        ),  # Anuri Pearlstone
        "Anuri Temple Basement - Big pot in tomb tunnel": PhoaLocationData(
            region="anuri_temple(basement)",
            address=7676067,
            flags=PhoaFlag.RINCONTAINERS,
        ),  # 20 Rin
        # "Anuri Temple - Fishing Spot After Slargummy": PhoaLocationData(
        #     region="anuri_temple(pond)",
        #     address=7676025,
        # ), # Moonstone
        # Camera doesn't move with the rod yet. Not sure why. This check also requires about 10 Energy Gems anyway
        "Anuri Temple - Bart's head crater": PhoaLocationData(
            region="anuri_temple(pond)",
            address=7676075,
        ),  # Broken Golem Hat
        "Anuri Temple - Use slingshot to hit the switches below": PhoaLocationData(
            region="anuri_temple(post_pond)",
            address=7676026,
            rule=lambda state: state.has("Slingshot", player),
        ),  # Anuri Pearlstone
        "Anuri Temple - Lizard at treasure room before century toad": PhoaLocationData(
            region="anuri_temple(post_pond)",
            address=7676057,
            flags=PhoaFlag.SMALLANIMALS,
            rule=lambda state: state.has_any({"Slingshot", "Bombs"}, player),
        ),  # Mystery Meat
        "Anuri Temple - Dive down in long vertical room": PhoaLocationData(
            region="anuri_temple(dive_room)",
            address=7676027,
            rule=lambda state: state.has("Life Saver", player),
        ),  # Lunar Frog
        "Anuri Temple - Side entrance gate opened": PhoaLocationData(
            region="anuri_temple(main)",
            address=None,
        ),
        "Strange Urn": PhoaLocationData(
            region="anuri_temple(urn_room)",
            address=None,
        ),
    }

    if not options:
        return locations

    filters = [
        (options.enable_npc_gifts <= 0, PhoaFlag.NPCGIFTS),
        (options.enable_misc <= 0, PhoaFlag.MISC),
        (options.shop_sanity <= 0, PhoaFlag.SHOPSANITY),
        (options.enable_small_animal_drops <= 0, PhoaFlag.SMALLANIMALS),
        (options.enable_rin_locations <= 0, PhoaFlag.RINCHESTS),
        (options.enable_rin_locations <= 1, PhoaFlag.RINCONTAINERS),
    ]

    for option, flag in filters:
        if option:
            locations = {
                name: data for name, data in locations.items() if data.flags != flag
            }

    return locations
