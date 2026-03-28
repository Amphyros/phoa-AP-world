from enum import Flag, auto
from typing import Dict, NamedTuple, Optional, Callable

from BaseClasses import Location, CollectionState
from worlds.phoa import PhoaOptions
from worlds.phoa.LogicExtensions import PhoaLogic


class PhoaFlag(Flag):
    DEFAULT = auto()
    MAINQUEST = auto()
    HEARTRUBY = auto()
    ENERGYGEM = auto()
    MOONSTONE = auto()
    DUNGEONITEM = auto()
    LUNARARTIFACT = auto()
    FISHINGSPOT = auto()
    NPCGIFTS = auto()
    PLANTO = auto()
    MISC = auto()
    SHOPSANITY = auto()
    SMALLANIMALS = auto()
    RINCHESTS = auto()
    RINCONTAINERS = auto()
    GEOCHALLENGE = auto()


class PhoaLocation(Location):
    game: str = "Phoenotopia: Awakening"


class PhoaLocationData(NamedTuple):
    region: str
    address: Optional[int]
    rule: Optional[Callable[[CollectionState], bool]] = None
    flags: PhoaFlag = PhoaFlag.DEFAULT
    vanillaItem: str = ""


def get_location_data(player: Optional[int], options: Optional[PhoaOptions]) -> Dict[str, PhoaLocationData]:
    logic = PhoaLogic(player)

    locations: Dict[str, PhoaLocationData] = {
        "Panselo Village - Watchtower (West) - Chest": PhoaLocationData(
            region="panselo_village",
            address=7676061,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="35 Rin",
        ),
        "Panselo Village - Watchtower (West) - Hidden in box": PhoaLocationData(
            region="panselo_village",
            address=7676031,
            flags=PhoaFlag.MISC,
            vanillaItem="Cheese",
        ),
        "Panselo Village - Watchtower (West) - Lizard": PhoaLocationData(
            region="panselo_village",
            address=7676041,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Panselo Village - Free Gift from Panselo Shop Keeper Tao": PhoaLocationData(
            region="panselo_village",
            address=7676070,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Fruit Jam",
        ),
        "Panselo Village - Panselo Shop Item 1": PhoaLocationData(
            region="panselo_village",
            address=7676072,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Perro Egg",
        ),
        "Panselo Village - Panselo Shop Item 2": PhoaLocationData(
            region="panselo_village",
            address=7676073,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Milk",
        ),
        "Panselo Village - Panselo Shop Item 3": PhoaLocationData(
            region="panselo_village",
            address=7676074,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Panselo Potato",
        ),
        "Panselo Village - Panselo Shop Box 1 after abduction": PhoaLocationData(
            region="panselo_village",
            address=7676084,
            rule=lambda state: state.has("Slargummy boss defeated", player),
            flags=PhoaFlag.MISC,
            vanillaItem="Panselo Potato",
        ),
        "Panselo Village - Panselo Shop Box 2 after abduction": PhoaLocationData(
            region="panselo_village",
            address=7676085,
            rule=lambda state: state.has("Slargummy boss defeated", player),
            flags=PhoaFlag.MISC,
            vanillaItem="Perro Egg",
        ),
        "Panselo Village - Panselo Shop Box 3 after abduction": PhoaLocationData(
            region="panselo_village",
            address=7676086,
            rule=lambda state: state.has("Slargummy boss defeated", player),
            flags=PhoaFlag.MISC,
            vanillaItem="Fruit Jam",
        ),
        "Panselo Village - Panselo Shop Box 4 after abduction": PhoaLocationData(
            region="panselo_village",
            address=7676087,
            rule=lambda state: state.has("Slargummy boss defeated", player),
            flags=PhoaFlag.MISC,
            vanillaItem="Milk",
        ),
        "Panselo Village - Panselo Shop Box 5 after abduction": PhoaLocationData(
            region="panselo_village",
            address=7676088,
            rule=lambda state: state.has("Slargummy boss defeated", player),
            flags=PhoaFlag.MISC,
            vanillaItem="Panselo Potato",
        ),
        "Panselo Village - Dojo high up punchbag": PhoaLocationData(
            region="panselo_village",
            address=7676082,
            rule=lambda state: logic.can_deal_damage(state, exclude_lamp=True),
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="20 Rin",
        ),
        "Panselo Village - Play Prelude of Panselo": PhoaLocationData(
            region="panselo_village",
            address=7676089,
            rule=lambda state: logic.has_music_instrument(state),
            flags=PhoaFlag.NPCGIFTS,  # Sidequest?
            vanillaItem="Prelude of Panselo",
        ),
        "Panselo Village - Inside coop": PhoaLocationData(
            region="panselo_village",
            address=7676030,
            flags=PhoaFlag.MISC,
            vanillaItem="Perro Egg",
        ),
        "Panselo Village - Orphanage roof": PhoaLocationData(
            region="panselo_village",
            address=7676028,
            flags=PhoaFlag.MISC,
            vanillaItem="Dandelion",
        ),
        "Panselo Village - On table in girl's room": PhoaLocationData(
            region="panselo_village",
            address=7676032,
            flags=PhoaFlag.MISC,
            vanillaItem="Berry Fruit",
        ),
        "Panselo Village - Pot in boys Room": PhoaLocationData(
            region="panselo_village",
            address=7676058,
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="5 Rin",
        ),
        "Panselo Village - Box at right side of orphanage hall": PhoaLocationData(
            region="panselo_village",
            address=7676059,
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="9 Rin",
        ),
        "Panselo Village - Orphanage attic chest": PhoaLocationData(
            region="panselo_village",
            address=7676060,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="35 Rin",
        ),
        "Panselo Village - Nana's Pumpkin Muffin": PhoaLocationData(
            region="panselo_village",
            address=7676068,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Pumpkin Muffin",
        ),
        "Panselo Village - Yesterday's lunch from Kitt": PhoaLocationData(
            region="panselo_village",
            address=7676077,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Cooked Toad Leg",
        ),
        "Panselo Village - Kitt's money for the milk": PhoaLocationData(
            region="panselo_village",
            address=7676078,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="20 Rin",
        ),
        "Panselo Village - Amanda's gift lunch": PhoaLocationData(
            region="panselo_village",
            address=7676090,
            rule=lambda state: state.has("Slargummy boss defeated", player),
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Potato Lunch",
        ),
        "Panselo Village - Warehouse Chest": PhoaLocationData(
            region="panselo_village",
            address=7676062,
            rule=lambda state: logic.can_break_big_object_with_tools(state),
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="25 Rin",
        ),
        "Panselo Village - Warehouse Free standing item": PhoaLocationData(
            region="panselo_village",
            address=7676080,
            flags=PhoaFlag.MAINQUEST,
            vanillaItem="Wooden Bat",
        ),
        "Panselo Village - Jon's Potato": PhoaLocationData(
            region="panselo_village",
            address=7676069,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Panselo Potato",
        ),
        "Panselo Village - On roof next to Stan": PhoaLocationData(
            region="panselo_village",
            address=7676029,
            flags=PhoaFlag.MISC,
            vanillaItem="Dandelion",
        ),
        "Panselo Village - Rutea's room": PhoaLocationData(
            region="panselo_village",
            address=7676001,
            flags=PhoaFlag.HEARTRUBY,
            vanillaItem="Heart Ruby",
        ),
        "Panselo Village - Watchtower (East) item up top": PhoaLocationData(
            region="panselo_village",
            address=7676000,
            rule=lambda state: logic.can_break_big_object_with_tools(state, exclude_spear=True),
            flags=PhoaFlag.HEARTRUBY,
            vanillaItem="Heart Ruby",
        ),
        "Panselo Region - End of secret fishing spot": PhoaLocationData(
            region="panselo_region",
            address=7676002,
            flags=PhoaFlag.ENERGYGEM,
            vanillaItem="Energy Gem",
        ),
        "Panselo Region - Franway roof": PhoaLocationData(
            region="panselo_region",
            address=7676034,
            flags=PhoaFlag.MISC,
            vanillaItem="Dandelion",
        ),
        "Panselo Region - GEO house roof": PhoaLocationData(
            region="panselo_region",
            address=7676033,
            flags=PhoaFlag.MISC,
            vanillaItem="Dandelion",
        ),
        "Panselo Region - GEO house reward": PhoaLocationData(
            region="panselo_region",
            address=7676083,
            flags=PhoaFlag.GEOCHALLENGE,
            rule=lambda state: logic.has_music_instrument(state)
                               and state.has("GEO Song", player),
            vanillaItem="GEO Ticket",
        ),
        "Panselo Region - Overworld encounter near Sunflower Road": PhoaLocationData(
            region="panselo_region",
            address=7676005,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Panselo Region - Underneath boulder north of Panselo": PhoaLocationData(
            region="panselo_region",
            address=7676004,
            rule=lambda state: logic.has_bombs(state) or logic.can_use_spear_bomb(state),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Panselo Region - Northeastern treetops right stone pot": PhoaLocationData(
            region="panselo_region",
            address=7676003,
            rule=lambda state: logic.can_hit_switch_from_a_distance(state)
                               or state.has("Rocket Boots", player),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Panselo Region - Northeastern treetops left stone pot": PhoaLocationData(
            region="panselo_region",
            address=7676081,
            rule=lambda state: logic.can_hit_switch_from_a_distance(state)
                               or state.has("Rocket Boots", player),
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="30 Rin",
        ),
        "Doki Forest - Cave guarded by Gummies - First item": PhoaLocationData(
            region="panselo_region",
            address=7676035,
            flags=PhoaFlag.MISC,
            vanillaItem="Doki Herb",
        ),
        "Doki Forest - Cave guarded by Gummies - Second item": PhoaLocationData(
            region="panselo_region",
            address=7676036,
            flags=PhoaFlag.MISC,
            vanillaItem="Doki Herb",
        ),
        "Doki Forest - Cave guarded by Gummies - Third item": PhoaLocationData(
            region="panselo_region",
            address=7676037,
            flags=PhoaFlag.MISC,
            vanillaItem="Doki Herb",
        ),
        "Doki Forest - Cave guarded by Gummies - Lizard": PhoaLocationData(
            region="panselo_region",
            address=7676042,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Doki Forest - Lizard at climbable roots": PhoaLocationData(
            region="panselo_region",
            address=7676043,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Doki Forest - Cave blocked by destructable blocks": PhoaLocationData(
            region="panselo_region",
            address=7676006,
            rule=lambda state: logic.has_explosives(state),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Doki Forest - Chest through crawl space": PhoaLocationData(
            region="panselo_region",
            address=7676063,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="35 Rin",
        ),
        "Doki Forest - Lizard in alcove": PhoaLocationData(
            region="panselo_region",
            address=7676044,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Doki Forest - Campfire cave - First Lizard": PhoaLocationData(
            region="panselo_region",
            address=7676045,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Doki Forest - Campfire cave - Second Lizard": PhoaLocationData(
            region="panselo_region",
            address=7676046,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Doki Forest - Campfire cave - Pot high up above statue": PhoaLocationData(
            region="panselo_region",
            address=7676092,
            rule=lambda state: logic.has_sonic_spear(state),
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="50 Rin",
        ),
        "Doki Forest - Shelby's gift for lighting the campfire": PhoaLocationData(
            region="panselo_region",
            address=7676076,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Doki Herb",
        ),
        "Doki Forest - Fish underneath Anuri Temple": PhoaLocationData(
            region="panselo_region",
            address=7676007,
            rule=lambda state: logic.has_fishing_rod(state),
            flags=PhoaFlag.FISHINGSPOT,
            vanillaItem="Dragon's Scale",
        ),
        # "Doki Forest - High up the mountain left of Anuri Temple entrance": PhoaLocationData(
        #     region="panselo_region",
        #     address=7676093,
        #     rule=lambda state: logic.has_sonic_spear(state),
        #     flags=PhoaFlag.RINCONTAINERS,
        #     vanillaItem="50 Rin",
        # ),
        "Doki Forest - Gift from Seth": PhoaLocationData(
            region="panselo_region",
            address=7676071,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Mystery Meat",
        ),
        "Doki Forest - Gift from Alex": PhoaLocationData(
            region="panselo_region",
            address=7676008,
            flags=PhoaFlag.MAINQUEST,
            vanillaItem="Slingshot",
        ),
        "Doki Forest - On Top of Anuri Temple": PhoaLocationData(
            region="panselo_region",
            address=7676079,
            rule=lambda state: logic.has_sonic_spear(state),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Anuri Temple - Lizard at top of climbable vines at entrance": PhoaLocationData(
            region="anuri_temple(main_entrance)",
            address=7676047,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Skeleton above first gate": PhoaLocationData(
            region="anuri_temple(main_entrance)",
            address=7676009,
            rule=lambda state: logic.can_deal_damage(state),
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Anuri Pearlstone",
        ),
        "Anuri Temple - Lizard behind Bombable Blocks": PhoaLocationData(
            region="anuri_temple(top_floor)",
            address=7676048,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Time the gates through Scaber funnel": PhoaLocationData(
            region="anuri_temple(scaber_switch_maze)",
            address=7676024,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Anuri Temple - Lizard left of Anuri throne": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676050,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Lizard right of Anuri throne": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676049,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Fight toads in treasure room": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676016,
            rule=lambda state: logic.can_break_big_object_with_tools(state),
            flags=PhoaFlag.LUNARARTIFACT,
            vanillaItem="Lunar Vase",
        ),
        "Anuri Temple - Lizard at the end of treasure room": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676051,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Scabers maze": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676010,
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Anuri Pearlstone",
        ),
        "Anuri Temple - High up pot in Scabers maze": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676066,
            rule=lambda state: logic.has_sonic_spear(state),
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="15 Rin",
        ),
        "Anuri Temple - Press the switches with pots and fruits": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676011,
            rule=lambda state: logic.can_hit_switch_from_a_distance(state, True),
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Anuri Pearlstone",
        ),
        "Anuri Temple - Side entrance room - First Lizard": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676055,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Carry pot across the water steps": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676012,
            flags=PhoaFlag.ENERGYGEM,
            vanillaItem="Energy Gem",
        ),
        "Anuri Temple - Lizard in water steps room": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676054,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Stackable pots room - Hidden item": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676013,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Anuri Temple - Stackable pots room - Lizard": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676053,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Stackable pots room - Anuri Skeleton": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676065,
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="15 Rin",
        ),
        "Anuri Temple - Sprint-jump on timed switches": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676014,
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Anuri Pearlstone",
        ),
        "Anuri Temple - Hit three switches in many pots room": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676019,
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Anuri Pearlstone",
        ),
        "Anuri Temple - Mouse in pot in many pots room": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676091,
            rule=lambda state: logic.has_bat(state),  # New logic rule can_reasonably_kill_small_animals?
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Skeleton at bottom of right elevator room": PhoaLocationData(
            region="anuri_temple(main)",
            address=7676064,
            rule=lambda state: logic.can_deal_damage(state),
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="15 Rin",
        ),
        "Anuri Temple - Side entrance room - Second Lizard": PhoaLocationData(
            region="anuri_temple(side_entrance)",
            address=7676056,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Side entrance first item": PhoaLocationData(
            region="anuri_temple(side_entrance)",
            address=7676038,
            flags=PhoaFlag.MISC,
            vanillaItem="Doki Herb",
        ),
        "Anuri Temple - Side entrance second item": PhoaLocationData(
            region="anuri_temple(side_entrance)",
            address=7676039,
            flags=PhoaFlag.MISC,
            vanillaItem="Doki Herb",
        ),
        "Anuri Temple - Moveable bridges room": PhoaLocationData(
            region="anuri_temple(moveable_bridge_area)",
            address=7676017,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Anuri Temple - Lizard in movable bridge room": PhoaLocationData(
            region="anuri_temple(moveable_bridge_area)",
            address=7676052,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Slingshot the switch with surfacing Toads": PhoaLocationData(
            region="anuri_temple(moveable_bridge_area)",
            address=7676018,
            rule=lambda state: logic.has_slingshot(state),
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Anuri Pearlstone",
        ),
        "Anuri Temple - Tall tower puzzle behind locked door": PhoaLocationData(
            region="anuri_temple(tall_tower_puzzle_room)",
            address=7676015,
            flags=PhoaFlag.HEARTRUBY,
            vanillaItem="Heart Ruby",
        ),
        "Anuri Temple - Tall tower puzzle side item": PhoaLocationData(
            region="anuri_temple(tall_tower_puzzle_room)",
            address=7676040,
            flags=PhoaFlag.MISC,
            vanillaItem="Doki Herb",
        ),
        "Anuri Temple Basement - Hit the switch hidden under breakable tomb": PhoaLocationData(
            region="anuri_temple(basement)",
            address=7676020,
            rule=lambda state: logic.has_explosives(state),
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Anuri Pearlstone",
        ),
        "Anuri Temple Basement - Push metal pot onto switch from above": PhoaLocationData(
            region="anuri_temple(basement)",
            address=7676021,
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Anuri Pearlstone",
        ),
        "Anuri Temple Basement - Within sarcophagus": PhoaLocationData(
            region="anuri_temple(basement)",
            address=7676022,
            rule=lambda state: logic.has_explosives(state),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Anuri Temple Basement - Defeat the glowing Slargummy": PhoaLocationData(
            region="anuri_temple(basement)",
            address=7676023,
            rule=lambda state: logic.has_light_source(state)
                               and logic.can_reasonably_kill_enemies(state),
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Anuri Pearlstone",
        ),
        "Anuri Temple Basement - Big pot in tomb tunnel": PhoaLocationData(
            region="anuri_temple(basement)",
            address=7676067,
            rule=lambda state: logic.can_break_big_object_with_tools(state),
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="20 Rin",
        ),
        "Anuri Temple - Fishing Spot After Slargummy": PhoaLocationData(
            region="anuri_temple(pond)",
            address=7676025,
            rule=lambda state: logic.has_fishing_rod(state),
            flags=PhoaFlag.FISHINGSPOT,
            vanillaItem="Moonstone",
        ),
        "Anuri Temple - Bart's head crater": PhoaLocationData(
            region="anuri_temple(pond)",
            address=7676075,
            flags=PhoaFlag.MAINQUEST,
            vanillaItem="Mysterious Golem Head",
        ),
        "Anuri Temple - Use slingshot to hit the switches below": PhoaLocationData(
            region="anuri_temple(post_pond)",
            address=7676026,
            rule=lambda state: logic.has_slingshot(state)
                               or logic.has_sonic_spear(state),
            flags=PhoaFlag.DUNGEONITEM,
            vanillaItem="Anuri Pearlstone",
        ),
        "Anuri Temple - Lizard at treasure room before century toad": PhoaLocationData(
            region="anuri_temple(post_pond)",
            address=7676057,
            rule=lambda state: logic.can_hit_switch_from_a_distance(state),
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Anuri Temple - Dive down in long vertical room": PhoaLocationData(
            region="anuri_temple(dive_room)",
            address=7676027,
            rule=lambda state: state.has("Life Saver", player),
            flags=PhoaFlag.LUNARARTIFACT,
            vanillaItem="Lunar Frog",
        ),
        "Sunflower Road - East - First item on sunflower leaf": PhoaLocationData(
            region="panselo_region",
            address=7676094,
            flags=PhoaFlag.MISC,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - East - Second item on sunflower leaf": PhoaLocationData(
            region="panselo_region",
            address=7676095,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Sunflower Road - East - Third item on sunflower leaf": PhoaLocationData(
            region="panselo_region",
            address=7676096,
            flags=PhoaFlag.MISC,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - East - First item hanging from sunflower stem": PhoaLocationData(
            region="panselo_region",
            address=7676097,
            flags=PhoaFlag.MISC,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - East - Fourth item on sunflower leaf": PhoaLocationData(
            region="panselo_region",
            address=7676098,
            flags=PhoaFlag.MISC,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - East - Chest on sunflower leaf": PhoaLocationData(
            region="panselo_region",
            address=7676099,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="35 Rin",
        ),
        "Sunflower Road - East - Second item hanging from sunflower stem": PhoaLocationData(
            region="panselo_region",
            address=7676100,
            flags=PhoaFlag.MISC,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - East - Fifth item on sunflower leaf": PhoaLocationData(
            region="panselo_region",
            address=7676101,
            flags=PhoaFlag.MISC,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - East - Item high up on sunflower leaf": PhoaLocationData(
            region="panselo_region",
            address=7676102,
            rule=lambda state: state.has("Rocket Boots", player),
            flags=PhoaFlag.HEARTRUBY,
            vanillaItem="Heart Ruby",
        ),
        "Sunflower Road - Honey Bee Lab and Inn - Item on sunflower leaf on the right": PhoaLocationData(
            region="panselo_region",
            address=7676103,
            flags=PhoaFlag.MISC,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - Honey Bee Lab and Inn - Item on sunflower leaf on the left": PhoaLocationData(
            region="panselo_region",
            address=7676104,
            flags=PhoaFlag.MISC,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - Honey Bee Lab and Inn - Mr. Planto's reward": PhoaLocationData(
            region="panselo_region",
            address=7676105,
            flags=PhoaFlag.PLANTO,
            vanillaItem="20 Rin",
        ),
        "Sunflower Road - Honey Bee Lab and Inn - Shop Item 1": PhoaLocationData(
            region="panselo_region",
            address=7676106,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Honey Bun",
        ),
        "Sunflower Road - Honey Bee Lab and Inn - Shop Item 2": PhoaLocationData(
            region="panselo_region",
            address=7676107,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Honey Brew",
        ),
        "Sunflower Road - Honey Bee Lab and Inn - Shop Item 3": PhoaLocationData(
            region="panselo_region",
            address=7676108,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Honey Drop",  # 3 of them
        ),
        "Sunflower Road - Honey Bee Lab and Inn - Inside box in shop attic": PhoaLocationData(
            region="panselo_region",
            address=7676109,
            flags=PhoaFlag.MISC,
            vanillaItem="Honey Drop",
        ),
        "Sunflower Road - West - First item hanging from sunflower stem": PhoaLocationData(
            region="panselo_region",
            address=7676110,
            flags=PhoaFlag.MISC,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - West - First item on sunflower leaf": PhoaLocationData(
            region="panselo_region",
            address=7676111,
            flags=PhoaFlag.MISC,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - West - Item on sunflower leaf under bee parkour": PhoaLocationData(
            region="panselo_region",
            address=7676112,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Sunflower Road - West - Item on sunflower leaf after bee parkour": PhoaLocationData(
            region="panselo_region",
            address=7676113,
            flags=PhoaFlag.MISC,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - West - Item surrounded by bees": PhoaLocationData(
            region="panselo_region",
            address=7676114,
            flags=PhoaFlag.ENERGYGEM,
            vanillaItem="Energy Gem",
        ),
        "Sunflower Road - West - Chest on sunflower leaf": PhoaLocationData(
            region="panselo_region",
            address=7676115,
            flags=PhoaFlag.ENERGYGEM,
            vanillaItem="35 Rin",
        ),
        "Sunflower Road - West - Second item hanging from sunflower stem": PhoaLocationData(
            region="panselo_region",
            address=7676131,
            flags=PhoaFlag.MISC,
            vanillaItem="Nectear",
        ),
        "Sunflower Road - West - Third item hanging from sunflower stem": PhoaLocationData(
            region="panselo_region",
            address=7676116,
            flags=PhoaFlag.MISC,
            vanillaItem="Nectear",
        ),
        "Panselo Region - Chest in dark cave": PhoaLocationData(
            region="panselo_region",
            address=7676117,
            rule=lambda state: logic.has_light_source(state),
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="50 Rin",
        ),
        "Panselo Region - Fish up turtle in dark cave": PhoaLocationData(
            region="panselo_region",
            address=7676118,
            rule=lambda state: logic.has_fishing_rod(state),
            flags=PhoaFlag.FISHINGSPOT,
            vanillaItem="Turtle",
        ),
        "Atelo Bridge - Top left box in east tower": PhoaLocationData(
            region="panselo_region",
            address=7676119,
            rule=lambda state: logic.can_break_big_object_with_tools(state),
            flags=PhoaFlag.MISC,
            vanillaItem="Cheese",
        ),
        "Atelo Bridge - Place boxes to fit into crawlspace ": PhoaLocationData(
            region="panselo_region",
            address=7676120,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Atelo Bridge - Alcove behind boulders": PhoaLocationData(
            region="panselo_region",
            address=7676121,
            rule=lambda state: (logic.has_explosives(state) and state.has("Life Saver", player))
                               or state.has("Rocket Boots", player),
            flags=PhoaFlag.HEARTRUBY,
            vanillaItem="Heart Ruby",
        ),
        "Atelo Bridge - Lizard in middle tower": PhoaLocationData(
            region="panselo_region",
            address=7676122,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Atelo Bridge - Small box in middle tower": PhoaLocationData(
            region="panselo_region",
            address=7676123,
            flags=PhoaFlag.MISC,
            vanillaItem="Raw Meat",
        ),
        "Atelo Bridge - Chest in middle tower": PhoaLocationData(
            region="panselo_region",
            address=7676124,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="20 Rin",
        ),
        "Atelo Bridge - GEO reward": PhoaLocationData(
            region="panselo_region",
            address=7676125,
            rule=lambda state: logic.has_music_instrument(state)
                               and state.has("GEO Song", player),
            flags=PhoaFlag.GEOCHALLENGE,
            vanillaItem="GEO Ticket",
        ),
        "Atelo Bridge - Chest on top of big box in alcove": PhoaLocationData(
            region="panselo_region",
            address=7676126,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="30 Rin",
        ),
        "Atelo Bridge - Moonstone deep in the water": PhoaLocationData(
            region="panselo_region",
            address=7676127,
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        "Atelo Bridge - Middle chest": PhoaLocationData(
            region="panselo_region",
            address=7676128,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="1 Rin",
        ),
        "Atelo Bridge - Crawlspace blocked by boulders": PhoaLocationData(
            region="panselo_region",
            address=7676129,
            rule=lambda state: logic.has_explosives(state),
            flags=PhoaFlag.ENERGYGEM,
            vanillaItem="Energy Gem",
        ),
        "Atelo Bridge - Puzzle in west tower": PhoaLocationData(
            region="panselo_region",
            address=7676130,
            rule=lambda state: logic.has_sonic_spear(state)
                               or state.has("Rocket Boots", player),
            flags=PhoaFlag.MOONSTONE,
            vanillaItem="Moonstone",
        ),
        # Events
        "Anuri Temple - Side entrance gate opened": PhoaLocationData(
            region="anuri_temple(main)",
            address=None,
        ),
        "Slargummy boss defeated": PhoaLocationData(
            region="anuri_temple(slargummy_boss)",
            address=None,
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
        ),
        "Strange Urn": PhoaLocationData(
            region="anuri_temple(urn_room)",
            address=None,
        ),

        # Location Additions

        "Atai Town - Dark Tower Pot": PhoaLocationData(
            region="atai_town",
            address=7676200,
            vanillaItem="Moonstone",
        ),
        "Atai Town - Dark Tower Chest": PhoaLocationData(
            region="atai_town",
            address=7676201,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="30 Rin",
        ),
        "Atai Town - Prison Pot": PhoaLocationData(
            region="atai_town",
            address=7676202,
            vanillaItem="Moonstone",
        ),
        "Atai Town - Prison Chest": PhoaLocationData(
            region="atai_town",
            address=7676203,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="40 Rin",
        ),
        # NUMBER
        "Atai Town - Storage room hidden behind carpet": PhoaLocationData(
            region="atai_town",
            address=7676204,
            vanillaItem="Heart Ruby",
        ),
        "Atai Town - Vegetable Shop Item 1": PhoaLocationData(
            region="atai_town",
            address=7676205,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Vala Bean",
        ),
        "Atai Town - Vegetable Shop Item 2": PhoaLocationData(
            region="atai_town",
            address=7676206,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Desert Squash",
        ),
        "Atai Town - Vegetable Shop Item 3": PhoaLocationData(
            region="atai_town",
            address=7676207,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Moon Kelp",
        ),
        "Atai Town - Meat Shop Item 1": PhoaLocationData(
            region="atai_town",
            address=7676208,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Big Raw Meat",
        ),
        "Atai Town - Meat Shop Item 2": PhoaLocationData(
            region="atai_town",
            address=7676209,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Drake Tail",
        ),
        "Atai Town - Meat Shop Item 3": PhoaLocationData(
            region="atai_town",
            address=7676210,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Prime Fish Fillet",
        ),
        "Atai Town - Weapon Shop Item 1": PhoaLocationData(
            region="atai_town",
            address=7676211,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Sky Vest",
        ),
        "Atai Town - Weapon Shop Item 2": PhoaLocationData(
            region="atai_town",
            address=7676212,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Civillian Crossbow",
        ),
        "Atai Town - Weapon Shop Item 3": PhoaLocationData(
            region="atai_town",
            address=7676213,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Composite Bat",
        ),
        "Atai Town - Weapon Shop Item 4": PhoaLocationData(
            region="atai_town",
            address=7676214,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Crank Lamp",
        ),
        "Atai Town - Weapon Shop Item 5": PhoaLocationData(
            region="atai_town",
            address=7676215,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Fishing Rod",
        ),

        "Atai Town - Weapon Shop Dropper Bottom": PhoaLocationData(
            region="atai_town(weapons_shop_dropper)",
            address=7676216,
            vanillaItem="Heart Ruby",
        ),
        "Atai Town - Weapon Shop Dropper Pot": PhoaLocationData(
            region="atai_town(weapons_shop_dropper)",
            address=7676217,
            vanillaItem="Moonstone",
        ),
        "Atai Town - Weapon Shop Dropper Chest": PhoaLocationData(
            region="atai_town(weapons_shop_dropper)",
            address=7676218,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="35 Rin",
        ),

        "Atai Town - Weapon Shop Balcony Chest": PhoaLocationData(
            region="atai_town",
            address=7676219,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="30 Rin",
        ),
        "Atai Town - Daycare Item 1": PhoaLocationData(
            region="atai_town",
            address=7676220,
            vanillaItem="Moonstone",
        ),
        "Atai Town - Daycare Item 2": PhoaLocationData(
            region="atai_town",
            address=7676221,
            vanillaItem="Moonstone",
        ),
        "Atai Town - Fruit Shop Item 1": PhoaLocationData(
            region="atai_town",
            address=7676222,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Prickle Fruit",
        ),
        "Atai Town - Fruit Shop Item 2": PhoaLocationData(
            region="atai_town",
            address=7676223,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Berry Fruit",
        ),
        "Atai Town - Fruit Shop Quest": PhoaLocationData(  # 4 Berry Fruit
            region="atai_town",
            address=7676224,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="25 Rin",
        ),
        "Atai Town - Tavern Shop Item 1": PhoaLocationData(
            region="atai_town",
            address=7676225,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Milk",
        ),
        "Atai Town - Tavern Shop Quest": PhoaLocationData(
            region="atai_town",
            address=7676226,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Bottle of Wine",
        ),
        "Atai Town - Guard Residence Mouse": PhoaLocationData(
            region="atai_town",
            address=7676227,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Atai Town - Bo Running Challenge": PhoaLocationData(
            region="atai_town",
            address=7676228,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="30 Rin",
        ),

        "Atai Town - Ouroboros Shrine": PhoaLocationData(
            region="atai_town(ouroboros_shrine)",
            address=7676229,
            vanillaItem="Ouroboros Scroll",
        ),

        "Atai Town - Metro Chest": PhoaLocationData(
            region="atai_town(metro)",
            address=7676230,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="Ouroboros Scroll",
        ),
        "Atai Town - Metro Train Car Crate": PhoaLocationData(
            region="atai_town(metro)",
            address=7676231,
            rule=lambda state: logic.has_explosives(state),
            vanillaItem="Moonstone",
        ),

        "Atai Town - Lisa's Item": PhoaLocationData(
            region="atai_town",
            address=7676332,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Lisa's ID Card",
        ),
        "Atai Town - Mansion Chef Item": PhoaLocationData(
            region="atai_town",
            address=7676232,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Cooked Squash",
        ),
        "Atai Town - Mansion Storage Pot": PhoaLocationData(
            region="atai_town",
            address=7676233,
            vanillaItem="Moonstone",
        ),
        "Atai Town - Mansion Storage Chest": PhoaLocationData(
            region="atai_town",
            address=7676234,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="30 Rin",
        ),
        "Atai Town - Mansion East Wing Lizard": PhoaLocationData(
            region="atai_town",
            address=7676235,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Atai Town - East Sewer Pipe Room Chest": PhoaLocationData(
            region="atai_town",
            address=7676236,
            flags=PhoaFlag.RINCHESTS,
            rule=lambda state: logic.has_light_source(state),
            vanillaItem="25 Rin",
        ),
        "Atai Town - East Sewer Crate": PhoaLocationData(
            region="atai_town",
            address=7676237,
            flags=PhoaFlag.MISC,
            rule=lambda state: logic.has_light_source(state),
            vanillaItem="Canned Beans",
        ),
        "Atai Town - East Residence Balcony Pot": PhoaLocationData(
            region="atai_town",
            address=7676238,
            vanillaItem="Moonstone",
        ),
        "Atai Town - Shooting Range Item 1": PhoaLocationData(
            region="atai_town",
            address=7676239,
            flags=PhoaFlag.SHOPSANITY,
            rule=lambda state: logic.can_hit_switch_from_a_distance(state),
            vanillaItem="Rubber Ducky",
        ),
        "Atai Town - Shooting Range Item 2": PhoaLocationData(
            region="atai_town",
            address=7676240,
            flags=PhoaFlag.SHOPSANITY,
            rule=lambda state: logic.can_hit_switch_from_a_distance(state),
            vanillaItem="Heart Ruby",
        ),
        "Atai Town - Shooting Range Item 3": PhoaLocationData(
            region="atai_town",
            address=7676241,
            flags=PhoaFlag.SHOPSANITY,
            rule=lambda state: logic.can_hit_switch_from_a_distance(state),
            vanillaItem="Moonstone",
        ),
        "Atai Town - Far East Residence Crate": PhoaLocationData(
            region="atai_town",
            address=7676242,
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="30 Rin",
        ),

        "Rhodus Checkpoint - East Tower Commons Crate": PhoaLocationData(
            region="atai_region",
            address=7676243,
            vanillaItem="Honey Bun",
        ),
        "Rhodus Checkpoint - East Tower Lizard": PhoaLocationData(
            region="atai_region",
            address=7676244,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Rhodus Checkpoint - East Tower Turret Guard": PhoaLocationData(
            region="atai_region",
            address=7676245,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Mystery Meat",
        ),
        "Rhodus Checkpoint - East Shop Item 1": PhoaLocationData(
            region="atai_region",
            address=7676246,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Honey Brew",
        ),
        "Rhodus Checkpoint - East Shop Item 2": PhoaLocationData(
            region="atai_region",
            address=7676247,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Chocolates",
            # Item is singular, but the guy gives 3. It is one check though, so should it be its own item?
        ),
        "Rhodus Checkpoint - Central Shop Item 1": PhoaLocationData(
            region="atai_region",
            address=7676248,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Rubber Ducky",
        ),
        "Rhodus Checkpoint - Central Shop Item 2": PhoaLocationData(
            region="atai_region",
            address=7676249,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Refurbished Crank Lamp",
        ),
        "Rhodus Checkpoint - West Shop Item 1": PhoaLocationData(
            region="atai_region",
            address=7676250,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Saffron Milk",
        ),
        "Rhodus Checkpoint - West Shop Item 2": PhoaLocationData(
            region="atai_region",
            address=7676251,
            flags=PhoaFlag.SHOPSANITY,
            vanillaItem="Curry Bento",
        ),
        "Rhodus Checkpoint - Golem Gift": PhoaLocationData(
            region="atai_region",
            address=7676252,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Dandelion",
        ),
        "Rhodus Checkpoint - West Tower Top Guard Gift": PhoaLocationData(  # Needs an amount of energy gems
            region="atai_region",
            address=7676253,
            flags=PhoaFlag.NPCGIFTS,
            rule=lambda state: state.has("Rocket Boots", player),
            vanillaItem="Moonstone",
        ),

        "Adar's House - Scorpion": PhoaLocationData(
            region="adars_house",
            address=7676254,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Adar's House - Cave Ledge Item": PhoaLocationData(
            region="adars_house(cave)",
            address=7676255,
            vanillaItem="Energy Gem",
        ),

        "Ancient Vault - Printer Item 1": PhoaLocationData(
            region="ancient_vault(printer_room)",
            address=7676330,
            vanillaItem="Heart Ruby",
        ),
        "Ancient Vault - Printer Item 2": PhoaLocationData(
            region="ancient_vault(printer_room)",
            address=7676331,
            vanillaItem="Energy Gem",
        ),

        "Atai Region - Northwest Cave Chest": PhoaLocationData(
            region="atai_region",
            address=7676256,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="50 Rin",
        ),
        "Atai Region - Northwest Cave Top Path Item": PhoaLocationData(
            region="atai_region",
            address=7676257,
            rule=lambda state: logic.has_explosives(state),
            vanillaItem="Heart Ruby",
        ),

        "Atai Region - Franway Songstone Chest": PhoaLocationData(
            region="atai_region",
            address=7676258,
            flags=PhoaFlag.RINCHESTS,
            rule=lambda state: logic.has_music_instrument(state),
            vanillaItem="45 Rin",
        ),
        "Atai Region - Franway Fish": PhoaLocationData(
            region="atai_region",
            address=7676259,
            rule=lambda state: logic.has_fishing_rod(state),
            vanillaItem="Moonstone",
        ),
        "Atai Region - Franway Cactus": PhoaLocationData(
            region="atai_region",
            address=7676260,
            flags=PhoaFlag.MISC,
            vanillaItem="Prickle Fruit",
        ),
        "Atai Region - Boar Boy Quest": PhoaLocationData(  # 4 Drake Tails
            region="atai_region",
            address=7676261,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Tusk Strike",
        ),
        "Atai Region - Oasis Guard Gift": PhoaLocationData(
            region="atai_region",
            address=7676262,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Saffron Milk",
        ),
        "Atai Region - Oasis Mr. Planto Quest": PhoaLocationData(  # 5 "Food"
            region="atai_region",
            address=7676263,
            flags=PhoaFlag.NPCGIFTS,
            rule=lambda state: logic.has_explosives(state),
            vanillaItem="20 Rin",
        ),
        "Atai Region - Oasis Shrine": PhoaLocationData(
            region="atai_region(ouroboros_shrine)",
            address=7676264,
            vanillaItem="Ouroboros Scroll",
        ),
        "Atai Region - Sand Drifts Access Lizard": PhoaLocationData(
            region="atai_region",
            address=7676265,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Atai Region - Sand Drifts Access Glowing Rock Item": PhoaLocationData(
            region="atai_region",
            address=7676266,
            vanillaItem="Moonstone",
        ),

        "Sand Drifts Region - West Tower Lizard": PhoaLocationData(
            region="sand_drifts_region",
            address=7676267,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Sand Drifts Region - West Tower Top": PhoaLocationData(
            region="sand_drifts_region",
            address=7676268,
            vanillaItem="Energy Gem",
        ),
        "Sand Drifts Region - West Tower Perro": PhoaLocationData(
            region="sand_drifts_region",
            address=7676269,
            vanillaItem="Perro",
        ),
        "Sand Drifts Region - West Tower Cactus 1": PhoaLocationData(
            region="sand_drifts_region",
            address=7676270,
            flags=PhoaFlag.MISC,
            vanillaItem="Prickle Fruit",
        ),
        "Sand Drifts Region - West Tower Cactus 2": PhoaLocationData(
            region="sand_drifts_region",
            address=7676271,
            flags=PhoaFlag.MISC,
            vanillaItem="Prickle Fruit",
        ),
        "Sand Drifts Region - Ouroboros Shrine": PhoaLocationData(
            region="sand_drifts_region(ouroboros_shrine)",
            address=7676272,
            vanillaItem="Ouroboros Scroll",
        ),
        "Sand Drifts Region - Ancient GEO Dungeon Solution 1 Item": PhoaLocationData(
            region="sand_drifts_region(ancient_geo_dungeon)",
            address=7676273,
            vanillaItem="Antique Pin",
        ),
        "Sand Drifts Region - Ancient GEO Dungeon Solution 2 Item": PhoaLocationData(
            region="sand_drifts_region(ancient_geo_dungeon)",
            address=7676274,
            vanillaItem="Heart Ruby",
        ),
        "Sand Drifts Region - South Tree Crate": PhoaLocationData(
            region="sand_drifts_region",
            address=7676275,
            vanillaItem="Heart Ruby",
        ),

        "Sand Drifts - Shelter Mouse": PhoaLocationData(
            region="sand_drifts",
            address=7676276,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Sand Drifts - East Tower Puzzle Item": PhoaLocationData(
            region="sand_drifts",
            address=7676277,
            rule=lambda state: logic.has_bombs(state),
            vanillaItem="Heart Ruby",
        ),
        "Sand Drifts - Above First Ruin Entrance Chest": PhoaLocationData(
            region="sand_drifts",
            address=7676278,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="25 Rin",
        ),
        "Sand Drifts - First Ruin Trapped Chest": PhoaLocationData(
            # Should/Could this be a check + Maybe Needs Logic? Have to sort out the softlocks
            region="sand_drifts(chest_trap_room)",
            address=7676279,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="1 Rin",
        ),
        "Sand Drifts - First Ruin Storage Crate": PhoaLocationData(
            region="sand_drifts(storage_room)",
            address=7676280,
            flags=PhoaFlag.RINCONTAINERS,
            vanillaItem="25 Rin",
        ),
        "Sand Drifts - First Ruin Center Room Scorpion": PhoaLocationData(
            region="sand_drifts",
            address=7676281,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Sand Drifts - Stealer Bird Plains Floor Patch": PhoaLocationData(
            region="sand_drifts",
            address=7676282,
            vanillaItem="Moonstone",
        ),
        "Sand Drifts - Ouroboros Shrine": PhoaLocationData(
            region="sand_drifts(ouroboros_shrine)",
            address=7676283,
            vanillaItem="Ouroboros Scroll",
        ),

        "Forlorn Ruins - Fountain Room Chest": PhoaLocationData(
            region="forlorn_ruins(fountain_room)",
            address=7676284,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="35 Rin",
        ),
        "Forlorn Ruins - Fountain Room Dive Item": PhoaLocationData(
            region="forlorn_ruins(fountain_room)",
            address=7676285,
            rule=lambda state: logic.has_sonic_spear(state)
                               and state.has("Lifesaver", player),
            vanillaItem="Moonstone",
        ),
        "Forlorn Ruins - Fountain Room Lizard": PhoaLocationData(
            region="forlorn_ruins(fountain_room)",
            address=7676286,
            flags=PhoaFlag.SMALLANIMALS,
            rule=lambda state: logic.has_slingshot(state) or logic.has_sonic_spear(state) or logic.has_crossbow(state),
            vanillaItem="Mystery Meat",
        ),

        "Forlorn Ruins - Bombable Wall Room Pot": PhoaLocationData(
            region="forlorn_ruins(bombable_wall)",
            address=7676287,
            vanillaItem="Moonstone",
        ),
        "Forlorn Ruins - Bombable Wall Room Mouse": PhoaLocationData(
            region="forlorn_ruins(bombable_wall)",
            address=7676288,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),

        "Forlorn Ruins - Dragon Snare Room Chest": PhoaLocationData(
            region="forlorn_ruins(dragon_snare_room)",
            address=7676289,
            flags=PhoaFlag.RINCHESTS,
            rule=lambda state: logic.has_explosives(state),
            vanillaItem="35 Rin",
        ),

        "Forlorn Ruins - Stairwell Scorpion": PhoaLocationData(
            region="forlorn_ruins",
            address=7676290,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),

        "Forlorn Ruins - Stairwell Keydoor Gauntlet Item": PhoaLocationData(
            region="forlorn_ruins(staircase_room_key_door)",
            address=7676291,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),

        "Forlorn Ruins - Falafel Trap": PhoaLocationData(  # Maybe Needs Logic? Have to sort out the softlocks
            region="forlorn_ruins(falafel_trap)",
            address=7676292,
            flags=PhoaFlag.MISC,
            vanillaItem="Falafel",
        ),

        "Forlorn Ruins - Drake Death Room Pot": PhoaLocationData(
            region="forlorn_ruins",
            address=7676293,
            vanillaItem="Canned Beans",
        ),
        "Forlorn Ruins - Ceiling Switch Room Pot": PhoaLocationData(
            region="forlorn_ruins",
            address=7676294,
            vanillaItem="Canned Beans",
        ),

        "Forlorn Ruins - Trapped Chest": PhoaLocationData(  # Maybe Needs Logic? Have to sort out the softlocks
            region="forlorn_ruins(chest_trap)",
            address=7676295,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="25 Rin",

        ),
        "Forlorn Ruins - Dragon Snare Keydoor Pot": PhoaLocationData(
            region="forlorn_ruins(switch_room_key_door)",
            address=7676296,
            vanillaItem="Moonstone",
        ),
        "Forlorn Ruins - Dragon Snare Keydoor Chest": PhoaLocationData(
            region="forlorn_ruins(switch_room_key_door)",
            address=7676297,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="20 Rin",
        ),

        "Forlorn Ruins - Hideout Entrance Pot": PhoaLocationData(
            region="forlorn_ruins",
            address=7676298,
            vanillaItem="Canned Beans",
        ),
        "Forlorn Ruins - Hideout entrance behind a hidden wall": PhoaLocationData(
            region="forlorn_ruins",
            address=7676299,
            rule=lambda state: logic.has_explosives(state),
            vanillaItem="Honey Brew",
        ),

        "Ouroboros Hideout - West entrance behind the save book": PhoaLocationData(
            region="ouroboros_hideout",
            address=7676300,
            vanillaItem="Pooki Jerky",
        ),
        "Ouroboros Hideout - Main Hideout Shuriken Guard Item": PhoaLocationData(
            region="ouroboros_hideout",
            address=7676301,
            rule=lambda state: logic.can_deal_damage(state),
            vanillaItem="Ouro Guard Key",
        ),

        "Ouroboros Hideout - Songstone Treasure Room Mouse Item 1": PhoaLocationData(
            region="ouroboros_hideout(treasure_room)",
            address=7676302,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),
        "Ouroboros Hideout - Songstone Treasure Room Mouse Item 2": PhoaLocationData(
            region="ouroboros_hideout(treasure_room)",
            address=7676303,
            vanillaItem="Ouro Guard Key",
        ),
        "Ouroboros Hideout - Songstone Treasure Room Pot": PhoaLocationData(
            region="ouroboros_hideout(treasure_room)",
            address=7676304,
            rule=lambda state: logic.has_music_instrument(state),
            vanillaItem="Moonstone",
        ),
        "Ouroboros Hideout - Songstone Treasure Room Crate 1": PhoaLocationData(
            region="ouroboros_hideout(treasure_room)",
            address=7676305,
            flags=PhoaFlag.MISC,
            rule=lambda state: logic.has_music_instrument(state),
            vanillaItem="Prickle Fruit",
        ),
        "Ouroboros Hideout - Songstone Treasure Room Crate 2": PhoaLocationData(
            region="ouroboros_hideout(treasure_room)",
            address=7676306,
            flags=PhoaFlag.MISC,
            rule=lambda state: logic.has_music_instrument(state),
            vanillaItem="Pooki Jerky",
        ),
        "Ouroboros Hideout - Songstone Treasure Room Bombable Wall Chest": PhoaLocationData(
            region="ouroboros_hideout(treasure_room)",
            address=7676307,
            flags=PhoaFlag.RINCHESTS,
            rule=lambda state: logic.has_music_instrument(state)
                               and logic.has_explosives(state),
            vanillaItem="40 Rin",
        ),

        "Ouroboros Hideout - Melody's Gift": PhoaLocationData(
            region="ouroboros_hideout(fountain_room)",
            address=7676308,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Ouro Guard Key",
        ),
        "Ouroboros Hideout - Fountain Room Underwater": PhoaLocationData(
            region="ouroboros_hideout(fountain_room)",
            address=7676309,
            vanillaItem="Moonstone",
        ),

        "Ouroboros Hideout - Ruby's Gift": PhoaLocationData(
            region="ouroboros_hideout(prison_key_door)",
            address=7676310,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Heart Ruby",
        ),

        "Ouroboros Hideout - Storage Item 1": PhoaLocationData(
            region="ouroboros_hideout(storage_key_door)",
            address=7676311,
            flags=PhoaFlag.MISC,
            vanillaItem="Prickle Fruit",
        ),
        "Ouroboros Hideout - Storage Item 2": PhoaLocationData(
            region="ouroboros_hideout(storage_key_door)",
            address=7676312,
            flags=PhoaFlag.MISC,
            vanillaItem="Perro Egg",
        ),
        "Ouroboros Hideout - Storage Item 3": PhoaLocationData(
            region="ouroboros_hideout(storage_key_door)",
            address=7676313,
            flags=PhoaFlag.MISC,
            vanillaItem="Stink Root",
        ),
        "Ouroboros Hideout - Storage Item 4": PhoaLocationData(
            region="ouroboros_hideout(storage_key_door)",
            address=7676314,
            flags=PhoaFlag.MISC,
            vanillaItem="Honey Bun",
        ),
        "Ouroboros Hideout - Storage Chest": PhoaLocationData(
            region="ouroboros_hideout(storage_key_door)",
            address=7676315,
            flags=PhoaFlag.RINCHESTS,
            vanillaItem="30 Rin",
        ),
        "Ouroboros Hideout - Storage Mouse": PhoaLocationData(
            region="ouroboros_hideout(storage_key_door)",
            address=7676316,
            flags=PhoaFlag.SMALLANIMALS,
            vanillaItem="Mystery Meat",
        ),

        "Ouroboros Hideout - Box Breaker Challenge 1": PhoaLocationData(
            region="ouroboros_hideout(balo_challenge_room)",
            address=7676317,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Energy Gem",
        ),
        "Ouroboros Hideout - Box Breaker Challenge 2": PhoaLocationData(
            region="ouroboros_hideout(balo_challenge_room)",
            address=7676318,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Heart Ruby",
        ),

        "Ouroboros Hideout - Drake Hatchery Guard": PhoaLocationData(
            region="ouroboros_hideout(infant_drake_arena)",
            address=7676319,
            vanillaItem="Ouro Guard Key",
        ),
        "Ouroboros Hideout - Drake Hatchery Pot 1": PhoaLocationData(
            region="ouroboros_hideout(infant_drake_arena)",
            address=7676320,
            flags=PhoaFlag.MISC,
            vanillaItem="Pooki Jerky",
        ),
        "Ouroboros Hideout - Drake Hatchery Pot 2": PhoaLocationData(
            region="ouroboros_hideout(infant_drake_arena)",
            address=7676321,
            rule=lambda state: logic.has_slingshot(state) or logic.has_crossbow(state),
            vanillaItem="Lunar Drake",
        ),
        "Ouroboros Hideout - Drake Hatchery Chest": PhoaLocationData(
            region="ouroboros_hideout(infant_drake_arena)",
            address=7676322,
            flags=PhoaFlag.RINCHESTS,
            rule=lambda state: logic.has_slingshot(state) or logic.has_crossbow(state),
            vanillaItem="35 Rin",
        ),

        "Ouroboros Hideout - Trial 1 Guard": PhoaLocationData(
            region="ouroboros_hideout(trial_one)",
            address=7676323,
            vanillaItem="Ouro Guard Key",
        ),
        "Ouroboros Hideout - Trial 1 Completion": PhoaLocationData(
            region="ouroboros_hideout(trial_one)",
            address=7676324,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Ouroboros Proof",
        ),

        "Ouroboros Hideout - Trial 2 Completion": PhoaLocationData(
            region="ouroboros_hideout(trial_two)",
            address=7676325,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Ouroboros Proof",
        ),

        "Ouroboros Hideout - Trial 3 Completion": PhoaLocationData(
            region="ouroboros_hideout(trial_three)",
            address=7676326,
            flags=PhoaFlag.NPCGIFTS,
            vanillaItem="Ouroboros Proof",
        ),

        "Ouroboros Hideout - Atri Training 1": PhoaLocationData(  # 2 Ouroboros Scrolls
            region="ouroboros_hideout(great_drake_arena)",
            address=7676327,
            flags=PhoaFlag.NPCGIFTS,
            rule=lambda state: logic.has_sonic_spear(state),
            vanillaItem="Spear Bomb",
        ),
        "Ouroboros Hideout - Atri Training 2": PhoaLocationData(  # 4 Ouroboros Scrolls Total
            region="ouroboros_hideout(great_drake_arena)",
            address=7676328,
            flags=PhoaFlag.NPCGIFTS,
            rule=lambda state: logic.has_sonic_spear(state) and state.has("Prelude of Panselo", player),
            vanillaItem="Spell of Rejuvination",
        ),
        "Ouroboros Hideout - Atri Training 3": PhoaLocationData(  # 6 Ouroboros Scrolls Total
            region="ouroboros_hideout(great_drake_arena)",
            address=7676329,
            flags=PhoaFlag.NPCGIFTS,
            rule=lambda state: logic.has_sonic_spear(state) and state.has("Prelude of Panselo", player),
            vanillaItem="Baroque of Battle",
        ),

        # LAST ADDRESS 7676332

    }

    if not options:
        return locations

    filters = [
        (options.enable_main_quest_locations <= 0, PhoaFlag.MAINQUEST),
        (options.enable_heart_ruby_locations <= 0, PhoaFlag.HEARTRUBY),
        (options.enable_energy_gem_locations <= 0, PhoaFlag.ENERGYGEM),
        (options.enable_moonstone_locations <= 0, PhoaFlag.MOONSTONE),
        (options.enable_lunar_artifacts_locations <= 0, PhoaFlag.LUNARARTIFACT),
        (options.enable_fishing_spots <= 0, PhoaFlag.FISHINGSPOT),
        (options.enable_npc_gifts <= 0, PhoaFlag.NPCGIFTS),
        (options.enable_planto_rewards <= 0, PhoaFlag.PLANTO),
        (options.enable_misc <= 0, PhoaFlag.MISC),
        (options.shop_sanity <= 0, PhoaFlag.SHOPSANITY),
        (options.enable_small_animal_drops <= 0, PhoaFlag.SMALLANIMALS),
        (options.enable_rin_locations <= 0, PhoaFlag.RINCHESTS),
        (options.enable_rin_locations <= 1, PhoaFlag.RINCONTAINERS),
        (options.enable_geo_challenge_rewards <= 0, PhoaFlag.GEOCHALLENGE)
    ]

    for option, flag in filters:
        if option:
            locations = {
                name: data for name, data in locations.items() if data.flags != flag
            }

    return locations
