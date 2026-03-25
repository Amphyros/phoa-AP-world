from typing import Dict, Callable, Optional, NamedTuple

from BaseClasses import MultiWorld, Region, Location, CollectionState
from Utils import visualize_regions
from worlds.phoa import get_location_data, PhoaOptions
from worlds.phoa.Locations import PhoaLocationData
from worlds.phoa.LogicExtensions import PhoaLogic


class PhoaExit(NamedTuple):
    name: str
    region: str
    connection: str
    rule: Optional[Callable[[CollectionState], bool]] = None
    one_way: bool = False


def get_exit_data(player: int, options: PhoaOptions) -> list[PhoaExit]:
    logic = PhoaLogic(player)

    exits: list[PhoaExit] = [
        # Menu
        PhoaExit(
            name="game_start",
            region="Menu",
            connection="panselo_village",
            one_way=True,
        ),
        # panselo_village
        PhoaExit(
            name="panselo_gate",
            region="panselo_village",
            connection="panselo_region",
            rule=lambda state: logic.can_deal_damage(state) or options.open_panselo_gates,
        ),
        PhoaExit(
            name="rutea's_lab_gate",
            region="panselo_village",
            connection="panselo_village_rutea's_lab",
            rule=lambda state: logic.can_hit_switch_from_a_distance(state),
        ),
        # panselo_region
        PhoaExit(
            name="anuri_temple_entrance",
            region="panselo_region",
            connection="anuri_temple(main_entrance)",
            rule=lambda state: logic.can_hit_switch_from_a_distance(state),
        ),
        PhoaExit(
            name="anuri_temple_side_entrance",
            region="panselo_region",
            connection="anuri_temple(side_entrance)",
            rule=lambda state: logic.has_explosives(state),
        ),
        PhoaExit(
            name="over_anuri_temple",
            region="panselo_region",
            connection="anuri_temple(slargummy_boss)",
            rule=lambda state: logic.has_sonic_spear(state),
            one_way=True,
        ),
        # anuri_temple(main_entrance)
        PhoaExit(
            name="anuri_temple_main_exit",
            region="anuri_temple(main_entrance)",
            connection="panselo_region",
        ),
        PhoaExit(
            name="anuri_temple_pearl_entrance",
            region="anuri_temple(main_entrance)",
            connection="anuri_temple(main)",
            rule=lambda state: logic.has_anuri_pearlstones(1, state)
        ),
        PhoaExit(
            name="anuri_temple_top_floor_boulder",
            region="anuri_temple(main_entrance)",
            connection="anuri_temple(top_floor)",
            rule=lambda state: logic.has_explosives(state)
                               or (logic.has_sonic_spear(state) and state.has("Hover Boots", player)),
        ),
        # anuri_temple(top_floor)
        PhoaExit(
            name="anuri_temple_drop_to_throne",
            region="anuri_temple(top_floor)",
            connection="anuri_temple(main)",
            one_way=True,
        ),
        PhoaExit(
            name="anuri_temple_door_to_scaber_maze",
            region="anuri_temple(top_floor)",
            connection="anuri_temple(scaber_switch_maze)",
            rule=lambda state: logic.has_anuri_pearlstones(10, state)
        ),
        # anuri_temple(main)
        PhoaExit(
            name="anuri_temple_to_main_entrance",
            region="anuri_temple(main)",
            connection="anuri_temple(main_entrance)",
        ),
        PhoaExit(
            name="anuri_temple_to_tall_tower_puzzle_room",
            region="anuri_temple(main)",
            connection="anuri_temple(tall_tower_puzzle_room)",
            rule=lambda state: logic.has_anuri_pearlstones(10, state),
        ),
        PhoaExit(
            name="anuri_temple_to_side_entrance",
            region="anuri_temple(main)",
            connection="anuri_temple(side_entrance)",
        ),
        PhoaExit(
            name="anuri_temple_to_basement",
            region="anuri_temple(main)",
            connection="anuri_temple(basement)",
            rule=lambda state: logic.has_explosives(state),
        ),
        PhoaExit(
            name="anuri_temple_bridge_switch",
            region="anuri_temple(main)",
            connection="anuri_temple(moveable_bridge_area)",
            rule=lambda state: logic.can_hit_switch_from_a_distance(state)
                               or state.has("Hover Boots", player),
        ),
        PhoaExit(
            name="anuri_temple_to_slargummy",
            region="anuri_temple(main)",
            connection="anuri_temple(slargummy_boss)",
            rule=lambda state: logic.has_anuri_pearlstones(6, state),
        ),
        # anuri_temple(side_entrance)
        PhoaExit(
            name="anuri_temple_side_exit",
            region="anuri_temple(side_entrance)",
            connection="panselo_region",
            rule=lambda state: logic.has_explosives(state),
        ),
        PhoaExit(
            name="anuri_temple_side_exit",
            region="anuri_temple(side_entrance)",
            connection="anuri_temple(main)",
            rule=lambda state: state.has("Anuri Temple - Side entrance gate opened", player),
        ),
        # anuri_temple(slargummy_boss)
        PhoaExit(
            name="anuri_temple_slargummy_to_main",
            region="anuri_temple(slargummy_boss)",
            connection="anuri_temple(main)",
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
        ),
        PhoaExit(
            name="anuri_temple_slargummy_to_pond",
            region="anuri_temple(slargummy_boss)",
            connection="anuri_temple(pond)",
            rule=lambda state: logic.can_reasonably_kill_enemies(state),
        ),
        # anuri_temple(pond)
        PhoaExit(
            name="anuri_temple_to_post_pond",
            region="anuri_temple(pond)",
            connection="anuri_temple(post_pond)",
            rule=lambda state: logic.has_anuri_pearlstones(9, state),
        ),
        # anuri_temple(post_pond)
        PhoaExit(
            name="anuri_temple_to_dive_room",
            region="anuri_temple(post_pond)",
            connection="anuri_temple(dive_room)",
            rule=lambda state: logic.has_anuri_pearlstones(10, state),
        ),
        PhoaExit(
            name="anuri_temple_to_urn_room",
            region="anuri_temple(post_pond)",
            connection="anuri_temple(urn_room)",
            rule=lambda state: logic.has_bombs(state),
        ),





        # PHOAEXIT ADDITIONS

        PhoaExit(
            name="atai_west_exit",
            region="atai_town",
            connection="atai_region",
            group="region",
        ),
        PhoaExit(
            name="atai_east_exit",
            region="atai_town",
            connection="atai_region",
            group="region",
        ),
        PhoaExit(
            name="atai_town_to_weapon_shop_dropper",
            region="atai_town",
            connection="atai_town(weapons_shop_dropper)",
            rule=lambda state: logic.has_rocket_boots(state),
            group="logic",
        ),
        PhoaExit(
            name="atai_town_to_shrine",
            region="atai_town",
            connection="atai_town(ouroboros_shrine)",
            rule=lambda state: logic.has_flute(state) and state.has("Song of Ouroboros", player),
            group="logic",
        ),
        PhoaExit( # Does this break logic? I might need to add an "or has_ouroboros_metro_access" or something
            name="atai_town_to_metro",
            region="atai_town",
            connection="atai_town(metro)",
            rule=lambda state: state.has("Lifesaver", player),
            group="logic",
        ),
        PhoaExit( # Key shenanigans
            name="town_metro_to_sand_drifts",
            region="atai_town(metro)",
            connection="sand_drifts(metro_stairwell)",
            rule=lambda state: state.has("Ouro Guard Key", player, 5),
            group="logic", # logic and region?
        ),
        PhoaExit(
            name="adars_house_east_exit",
            region="adars_house",
            connection="atai_region",
            group="region",
        ),
        PhoaExit(
            name="adars_house_to_cave",
            region="adars_house",
            connection="adars_house(cave)",
            rule=lambda state: logic.has_explosives(state),
            group="logic",
        ),
        PhoaExit(
            name="adars_cave_to_ancient_vault",
            region="adars_house(cave)",
            connection="ancient_vault",
            rule=lambda state: state.has("Spheralis", player),
            group="logic",
        ),
        PhoaExit( # Needs logic for how well equipped the player needs to be for fights
            name="ancient_vault_to_printer_room",
            region="ancient_vault",
            connection="ancient_vault(printer_room)",
            rule=lambda state: state.has("Spheralis", player),
            group="logic",
        ),
        






        PhoaExit(
            name="atai_region_to_shrine",
            region="atai_region",
            connection="atai_region(ouroboros_shrine)",
            rule=lambda state: state.has("Sonic Spear", "Lifesaver", player),
            group="logic",
        ),
        PhoaExit(
            name="atai_region_to_sand_drifts_region",
            region="atai_region",
            connection="sand_drifts_region",
            rule=lambda state: logic.has_explosives(state) and logic.has_flute(state),
            group="logic" # logic and region?
        ),
        PhoaExit(
            name="sand_drifts_region_to_ouroboros_shrine",
            region="sand_drifts_region",
            connection="sand_drifts_region(ouroboros_shrine)",
            rule=lambda state: logic.has_flute(state) and state.has("Song of Ouroboros", player),
            group="logic",
        ),
        PhoaExit(
            name="sand_drifts_region_to_ancient_geo_dungeon",
            region="sand_drifts_region",
            connection="sand_drifts_region(ancient_geo_dungeon)",
            rule=lambda state: logic.has_flute(state),
            group="logic"
        ),
        PhoaExit(
            name="sand_drifts_east_exit",
            region="sand_drifts",
            connection="sand_drifts_region",
            group="region",
        ),
        PhoaExit(
            name="sand_drifts_to_metro_stairwell",
            region="sand_drifts",
            connection="sand_drifts(metro_stairwell)",
            rule=lambda state: logic.has_explosives(state),
            group="logic"
        ),
        PhoaExit( # Possible softlock without an explosive
            name="sand_drifts_to_chest_trap",
            region="sand_drifts",
            connection="sand_drifts(chest_trap_room_1)",
            rule=lambda state: logic.can_hit_switch_from_a_distance(state),
            group="logic"
        ),
        PhoaExit(
            name="sand_drifts_to_storage_room",
            region="sand_drifts",
            connection="sand_drifts(storage_room)",
            rule=lambda state: logic.can_hit_switch_from_a_distance(state),
            group="logic"
        ),
        PhoaExit(
            name="sand_drifts_to_shrine",
            region="sand_drifts",
            connection="sand_drifts(ouroboros_shrine)",
            rule=lambda state: logic.has_flute(state) and state.has("Song of Ouroboros", "Rocket Boots", player),
            group="logic"
        ),
        PhoaExit(
            name="sand_drifts_to_forlorn_ruins",
            region="sand_drifts",
            connection="forlorn_ruins",
            rule=lambda state: logic.has_flute(state) and state.has("Song of Ouroboros", player),
            group="logic" # logic and region?
        ),
        PhoaExit(
            name="forlorn_ruins_to_fountain",
            region="forlorn_ruins",
            connection="forlorn_ruins(fountain_room)",
            rule=lambda state: logic.can_deal_damage(state),
            group="logic"
        ),
        PhoaExit(
            name="forlorn_ruins_to_dragon_snare",
            region="forlorn_ruins",
            connection="forlorn_ruins(dragon_snare_room)",
            group="region"
        ),
        PhoaExit(
            name="forlorn_ruins_bombable_wall",
            region="forlorn_ruins",
            connection="forlorn_ruins(bombable_wall)",
            rule=lambda state: logic.has_explosives(state),
            group="logic"
        ),
        PhoaExit( # Possible softlock without an explosive
            name="forlorn_ruins_to_falafel_trap",
            region="forlorn_ruins",
            connection="forlorn_ruins(falafel_trap)",
            group="region"
        ),
        PhoaExit( # Key shenanigans
            name="forlorn_ruins_staircase_key_door",
            region="forlorn_ruins",
            connection="forlorn_ruins(staircase_room_key_door)",
            rule=lambda state: state.has("Ouro Guard Key", player, 5),
            group="logic"
        ),
        PhoaExit( # Possible softlock without an explosive and music tool
            name="forlorn_ruins_to_chest_trap",
            region="forlorn_ruins",
            connection="forlorn_ruins(chest_trap)",
            group="region"
        ),
        PhoaExit( # Key shenanigans
            name="forlorn_ruins_switch_room_key_door",
            region="forlorn_ruins",
            connection="forlorn_ruins(switch_room_key_door)",
            rule=lambda state: state.has("Ouro Guard Key", player, 5),
            group="logic"
        ),
        PhoaExit(
            name="forlorn_ruins_to_ouroboros_hideout",
            region="forlorn_ruins",
            connection="ouroboros_hideout",
            rule=lambda state: logic.has_explosives(state) and logic.has_flute(state) and state.has("Song of Ouroboros", player),
            group="logic" # logic and region?
        ),
        PhoaExit(
            name="sand_drifts_to_ouroboros_hideout",
            region="sand_drifts",
            connection="ouroboros_hideout(tower)",
            rule=lambda state: state.has_any("Sonic Spear", "Rocket Boots", player),
            group="logic" # logic and region?
        ),
        PhoaExit(
            name="ouroboros_hideout_to_tower",
            region="ouroboros_hideout",
            connection="ouroboros_hideout(tower)",
            rule=lambda state: state.has("Sonic Spear", player),
            group="logic"
        ),
        PhoaExit(
            name="ouroboros_hideout_to_fountain",
            region="ouroboros_hideout",
            connection="ouroboros_hideout(fountain_room)",
            group="region"
        ),
        PhoaExit(
            name="ouroboros_hideout_to_balo_challenge",
            region="ouroboros_hideout",
            connection="ouroboros_hideout(balo_challenge_room)",
            group="region"
        ),
        PhoaExit( # Key shenanigans
            name="ouroboros_hideout_to_prison",
            region="ouroboros_hideout",
            connection="ouroboros_hideout(prison_key_door)",
            rule=lambda state: state.has("Ouro Guard Key", player, 5),
            group="logic"
        ),
        PhoaExit( # Key shenanigans
            name="ouroboros_hideout_to_storage",
            region="ouroboros_hideout",
            connection="ouroboros_hideout(storage_key_door)",
            rule=lambda state: state.has("Ouro Guard Key", player, 5),
            group="logic"
        ),
        PhoaExit( # I can do has_melee_weapon instead if we want to be more lax on the fights
            name="ouroboros_hideout_to_infant_drake_arena",
            region="ouroboros_hideout",
            connection="ouroboros_hideout(infant_drake_arena)",
            rule=lambda state: logic.can_deal_damage(state),
            group="logic"
        ),
        PhoaExit(
            name="ouroboros_hideout_to_treasure_room",
            region="ouroboros_hideout",
            connection="ouroboros_hideout(treasure_room)",
            group="region"
        ),
        PhoaExit(
            name="ouroboros_hideout_to_trial_one",
            region="ouroboros_hideout",
            connection="ouroboros_hideout(trial_one)",
            group="region"
        ),
        PhoaExit( # I can do has_melee_weapon instead if we want to be more lax on the fights
            name="ouroboros_hideout_to_trial_two",
            region="ouroboros_hideout",
            connection="ouroboros_hideout(trial_two)",
            rule=lambda state: logic.can_deal_damage(state),
            group="logic"
        ),
        PhoaExit(
            name="ouroboros_hideout_to_trial_three",
            region="ouroboros_hideout",
            connection="ouroboros_hideout(trial_three)",
            group="region"
        ),
        PhoaExit( # Key Shenanigans (this one's probably fine)
            name="ouroboros_hideout_to_great_drake_arena",
            region="ouroboros_hideout",
            connection="ouroboros_hideout(great_drake_arena)",
            rule=lambda state: state.has("Ouroboros_Proof", player, 3),
            group="logic"
        ),
        
        # END OF PHOAEXIT ADDITIONS
    ]

    return exits


def create_regions_and_locations(world: MultiWorld, player: int, options: PhoaOptions):
    locations_per_region: Dict[str, Dict[str, PhoaLocationData]] = split_locations_per_region(
        get_location_data(player, options))

    regions = [
        create_region(world, player, locations_per_region, "Menu"),
        create_region(world, player, locations_per_region, "panselo_village"),
        create_region(world, player, locations_per_region, "panselo_village_rutea's_lab"),
        create_region(world, player, locations_per_region, "panselo_region"),
        create_region(world, player, locations_per_region, "anuri_temple(main_entrance)"),
        create_region(world, player, locations_per_region, "anuri_temple(top_floor)"),
        create_region(world, player, locations_per_region, "anuri_temple(scaber_switch_maze)"),
        create_region(world, player, locations_per_region, "anuri_temple(main)"),
        create_region(world, player, locations_per_region, "anuri_temple(tall_tower_puzzle_room)"),
        create_region(world, player, locations_per_region, "anuri_temple(side_entrance)"),
        create_region(world, player, locations_per_region, "anuri_temple(basement)"),
        create_region(world, player, locations_per_region, "anuri_temple(moveable_bridge_area)"),
        create_region(world, player, locations_per_region, "anuri_temple(slargummy_boss)"),
        create_region(world, player, locations_per_region, "anuri_temple(pond)"),
        create_region(world, player, locations_per_region, "anuri_temple(post_pond)"),
        create_region(world, player, locations_per_region, "anuri_temple(dive_room)"),
        create_region(world, player, locations_per_region, "anuri_temple(urn_room)"),





        # CREATE_REGION ADDITIONS

        # ATAI REGION

        create_region(world, player, locations_per_region, "atai_region"),
        create_region(world, player, locations_per_region, "adars_house"),
        create_region(world, player, locations_per_region, "adars_house(cave)"),
        create_region(world, player, locations_per_region, "ancient_vault"),
        create_region(world, player, locations_per_region, "ancient_vault(printer_room)"),
        create_region(world, player, locations_per_region, "atai_region(ouroboros_shrine)"),


        # ATAI TOWN

        create_region(world, player, locations_per_region, "atai_town"),
        create_region(world, player, locations_per_region, "atai_town(weapons_shop_dropper)"),
        create_region(world, player, locations_per_region, "atai_town(ouroboros_shrine)"),
        create_region(world, player, locations_per_region, "atai_town(metro)"),



        # SAND DRIFTS REGION
        
        # Needs Explosive and Flute or Lifesaver and Ouro Guard Key for logic
        create_region(world, player, locations_per_region, "sand_drifts_region"),
        create_region(world, player, locations_per_region, "sand_drifts_region(ouroboros_shrine)"),
        create_region(world, player, locations_per_region, "sand_drifts_region(ancient_geo_dungeon)"),


        # SAND DRIFTS

        create_region(world, player, locations_per_region, "sand_drifts"),

        # Explosive (Sand Drifts, Forlorn) or Spear or Rocket Boots (Tower) or Lifesaver and Ouro Guard Key (Metro)
        create_region(world, player, locations_per_region, "sand_drifts(metro_stairwell)"),

        # Weapon (Potential Soflock without Explosive)
        create_region(world, player, locations_per_region, "sand_drifts(chest_trap_room)"),

        # Weapon
        create_region(world, player, locations_per_region, "sand_drifts(storage_room)"),

        # Rocket Boots and Flute
        create_region(world, player, locations_per_region, "sand_drifts(ouroboros_shrine)"),


        # FORLORN RUINS (SAND DRIFTS MAIN RUIN)

        # Flute
        create_region(world, player, locations_per_region, "forlorn_ruins"),

        # Weapon
        create_region(world, player, locations_per_region, "forlorn_ruins(fountain_room)"),

        # None
        create_region(world, player, locations_per_region, "forlorn_ruins(dragon_snare_room)"),

        # Explosive
        create_region(world, player, locations_per_region, "forlorn_ruins(bombable_wall)"),

        # None (Potential Soflock without Explosive)
        create_region(world, player, locations_per_region, "forlorn_ruins(falafel_trap)"),

        # Key
        create_region(world, player, locations_per_region, "forlorn_ruins(staircase_room_key_door)"),

        # None (Potential Soflock without Explosive + Flute)
        create_region(world, player, locations_per_region, "forlorn_ruins(chest_trap_room)"),

        # Key
        create_region(world, player, locations_per_region, "forlorn_ruins(switch_room_key_door)"),


        # OUROBOROS HIDEOUT

        # Spear or Rocket Boots
        create_region(world, player, locations_per_region, "ouroboros_hideout(tower)"),

        # On top of Explosive and Flute or Lifesaver and Ouro Guard Key, needs Explosive (Forlorn) or Spear or Rocket Boots (Tower)
        create_region(world, player, locations_per_region, "ouroboros_hideout"),

        # None
        create_region(world, player, locations_per_region, "ouroboros_hideout(fountain_room)"),
        create_region(world, player, locations_per_region, "ouroboros_hideout(balo_challenge_room)"),
        create_region(world, player, locations_per_region, "ouroboros_hideout(infant_drake_arena)"),
        create_region(world, player, locations_per_region, "ouroboros_hideout(treasure_room)"),
        create_region(world, player, locations_per_region, "ouroboros_hideout(trial_one)"),
        create_region(world, player, locations_per_region, "ouroboros_hideout(trial_three)"),

        # Weapon
        create_region(world, player, locations_per_region, "ouroboros_hideout(trial_two)"),

        # Key
        create_region(world, player, locations_per_region, "ouroboros_hideout(prison_key_door)"),
        create_region(world, player, locations_per_region, "ouroboros_hideout(storage_key_door)"),

        # Three Ourobos Proofs
        create_region(world, player, locations_per_region, "ouroboros_hideout(great_drake_arena)"),

        # END OF CREATE_REGION ADDITIONS
    ]

    world.regions += regions

    connect_regions(world, player, get_exit_data(player, options))


def create_region(world: MultiWorld, player: int, locations_per_region: Dict[str, Dict[str, PhoaLocationData]],
                  name: str) -> Region:
    region = Region(name, player, world)

    if name in locations_per_region:
        for location_name, location_data in locations_per_region[name].items():
            location = create_location(player, location_name, location_data, region)
            region.locations.append(location)

    return region


def create_location(player: int, location_name: str, location_data: PhoaLocationData, region: Region):
    location = Location(player, location_name, location_data.address, region)

    if location_data.rule:
        location.access_rule = location_data.rule

    return location


def connect_regions(world: MultiWorld, player: int, exits: list[PhoaExit]):
    for regionExit in exits:
        connect(world, player, regionExit.region, regionExit.connection, regionExit.rule, regionExit.name)


def connect(world: MultiWorld, player: int, source: str, target: str,
            rule: Optional[Callable[[CollectionState], bool]] = None, name: str = None):
    source_region = world.get_region(source, player)
    target_region = world.get_region(target, player)
    entrance = source_region.create_exit(name)

    if rule is not None:
        entrance.access_rule = rule

    entrance.connect(target_region)


def split_locations_per_region(locations: Dict[str, PhoaLocationData]):
    locations_per_region: Dict[str, Dict[str, PhoaLocationData]] = {}

    for location_name, location_data in locations.items():
        if location_data.region not in locations_per_region:
            locations_per_region[location_data.region] = {}

        locations_per_region[location_data.region][location_name] = location_data

    return locations_per_region
