from email.headerregistry import Address
from typing import Dict, NamedTuple, Optional, Callable

from kivy.core.window.window_pygame import android

from BaseClasses import Location, CollectionState
from worlds.phoa.LogicExtensions import PhoaLogic


class PhoaLocation(Location):
    game: str = "Phoenotopia: Awakening"

class PhoaLocationData(NamedTuple):
    region: str
    address: Optional[int]
    rule: Optional[Callable[[CollectionState], bool]] = None

def get_location_data(player: Optional[int]) -> Dict[str, PhoaLocationData]:

    logic = PhoaLogic(player)

    location_data: Dict[str, PhoaLocationData] = {
        "Watchtower (East)": PhoaLocationData(
            region="Overworld",
            address=7676000,
            # Locked by Bat
        ), # Heart Ruby
        "Rutea's laboratory": PhoaLocationData(
            region="Overworld",
            address=7676001,
            rule=lambda state: state.has("Slingshot", player) or
                               state.has("Bombs", player),
        ), # Heart Ruby
        "End of Secret Fishing Spot": PhoaLocationData(
            region="Overworld",
            address=7676002,
        ), # Energy Gem
        "Northeastern Treetops": PhoaLocationData(
            region="Overworld",
            address=7676003,
            rule=lambda state: state.has("Slingshot", player) or
                               state.has("Bombs", player),
        ), # Moonstone
        "Underneath Boulder": PhoaLocationData(
            region="Overworld",
            address=7676004,
            rule=lambda state: state.has("Bombs", player),
        ), # Moonstone
        "Overworld Encounter Near Sunflower Road": PhoaLocationData(
            region="Overworld",
            address=7676005,
            rule=lambda state: state.has("Slingshot", player) or
                               state.has("Bombs", player),
        ), # Moonstone
        "Cave Blocked by Destructable Blocks": PhoaLocationData(
            region="Overworld",
            address=7676006,
            rule=lambda state: state.has("Bombs", player),
        ), # Moonstone
        # "On Top of Anuri Temple": PhoaLocationData(
        #     region="Overworld",
        #     address=7676009,
        #     rule=lambda state: state.has("Sonic Spear", player),
        # ), # Moonstone
        "Fish Underneath Anuri Temple": PhoaLocationData(
            region="Overworld",
            address=7676007,
            rule=lambda state: state.has("Fishing Rod", player),
        ), # Dragon's Scale
        "Gift from Alex": PhoaLocationData(
            region="Overworld",
            address=7676008,
        ), # Slingshot
        "Skeleton Above First Gate": PhoaLocationData(
            region="Anuri Temple",
            address=7676009,
            rule=lambda state: logic.has_anuri_temple_access(state),
        ), # Anuri Pearlstone
        "Maze with Scabers": PhoaLocationData(
            region="Anuri Temple",
            address=7676010,
            rule=lambda state: logic.has_anuri_temple_access(state) and
                               state.has("Slingshot", player),
        ), # Anuri Pearlstone
        "Press the Switches with Pots and Fruits": PhoaLocationData(
            region="Anuri Temple",
            address=7676011,
            rule=lambda state: logic.has_anuri_temple_access(state),
        ), # Anuri Pearlstone
        "Carry Pot Across the Water and Bats": PhoaLocationData(
            region="Anuri Temple",
            address=7676012,
            rule=lambda state: logic.has_anuri_temple_access(state),
            # Requires Slingshot or Bombs
        ), # Energy Gem
        "Stackable Pots Room": PhoaLocationData(
            region="Anuri Temple",
            address=7676013,
            rule=lambda state: logic.has_anuri_temple_access(state),
        ), # Moonstone
        "Sprint-jump on Timed Switches": PhoaLocationData(
            region="Anuri Temple",
            address=7676014,
            rule=lambda state: logic.has_anuri_temple_access(state),
        ), # Anuri Pearlstone
        "Tall Tower Puzzle Behind Locked Door": PhoaLocationData(
            region="Anuri Temple",
            address=7676015,
            rule=lambda state: logic.has_anuri_temple_access(state) and
                               state.has("Anuri Pearlstone", player, 10),
            # Requires 1 pearlstone to enter
        ),  # Heart Ruby
        "Fight toads in treasure room": PhoaLocationData(
            region="Anuri Temple",
            address=7676016,
            rule=lambda state: logic.has_anuri_temple_access(state),
        ), # Lunar Vase
        "Moveable Bridges Room": PhoaLocationData(
            region="Anuri Temple",
            address=7676017,
            rule=lambda state: logic.has_anuri_temple_access(state),
            # Requires Slingshot or Bombs
        ),  # Moonstone
        "Slingshot the switch and surfacing Toads": PhoaLocationData(
            region="Anuri Temple",
            address=7676018,
            rule=lambda state: logic.has_anuri_temple_access(state) and
                               state.has("Slingshot", player),
        ), # Anuri Pearlstone
        "Three Switches With Lots of Pots": PhoaLocationData(
            region="Anuri Temple",
            address=7676019,
            rule=lambda state: logic.has_anuri_temple_access(state),
        ), # Anuri Pearlstone
        "Hit the Switch Hidden Under a Breakable Tomb": PhoaLocationData(
            region="Anuri Temple",
            address=7676020,
            rule=lambda state: logic.has_anuri_temple_access(state) and
                               state.has("Bombs", player),
        ), # Anuri Pearlstone
        "Push the Metal Pot Onto the Switch From Above": PhoaLocationData(
            region="Anuri Temple",
            address=7676021,
            rule=lambda state: logic.has_anuri_temple_access(state) and
                               state.has("Bombs", player),
        ), # Anuri Pearlstone
        "Within Sarcophagus": PhoaLocationData(
            region="Anuri Temple",
            address=7676022,
            rule=lambda state: logic.has_anuri_temple_access(state) and
                               state.has("Bombs", player),
        ), # Moonstone
        "Defeat the Glowing Slargummy": PhoaLocationData(
            region="Anuri Temple",
            address=7676023,
            rule=lambda state: logic.has_anuri_temple_access(state) and
                               state.has("Bombs", player) and
                               state.has("Crank Lamp", player),
        ), # Anuri Pearlstone
        "Time the gates through Scaber funnel": PhoaLocationData(
            region="Anuri Temple",
            address=7676024,
            rule=lambda state: logic.has_anuri_temple_access(state) and
                               state.has("Anuri Pearlstone", player, 10),
            # Requires 1 pearlstone to enter
        ), # Moonstone
        # "Fishing Spot After Slargummy": PhoaLocationData(
        #     region="Anuri Temple",
        #     address=7676025,
        #     rule=lambda state: logic.has_anuri_temple_access(state) and
        #                        state.has("Anuri Pearlstone", player, 6),
        #     # Requires 3 pearlstones to enter
        # ), # Moonstone
        # For some reason, the fish with the moonstone doesn't spawn on the first visit
        "Use Slingshot to Hit the Switches Below": PhoaLocationData(
            region="Anuri Temple",
            address=7676026,
            rule=lambda state: logic.has_anuri_temple_access(state) and
                               state.has("Sling Shot", player) and
                               state.has("Anuri Pearlstone", player, 9),
            # Requires 6 pearlstones to enter
        ), # Anuri Pearlstone
        "Dive down in long vertical room": PhoaLocationData(
            region="Anuri Temple",
            address=7676027,
            rule=lambda state: logic.has_anuri_temple_access(state) and
                               state.has("Anuri Pearlstone", player, 10),
            # Requires 7 pearlstones to enter
        ), # Lunar Frog
        "Strange Urn": PhoaLocationData(
            region="Anuri Temple",
            address=None,
            rule=lambda state: logic.has_anuri_temple_access(state) and
                               state.has("Anuri Pearlstone", player, 9),
            # Requires 6 pearlstones to enter
        ),
    }

    return location_data