from dataclasses import dataclass
from typing import Any

from Options import Toggle, PerGameCommonOptions, DeathLink, Choice, DefaultOnToggle, OptionGroup


class EnableNpcGifts(Toggle):
    """Include free gifts from NPCs"""
    display_name = "Include NPC gifts"


class EnableMisc(Toggle):
    """Include miscellaneous locations and items"""
    display_name = "Include miscellaneous"


class EnableShopSanity(Toggle):
    """Includes items that can be bought it shops"""
    display_name = "Shop sanity"


class EnableSmallAnimalDrops(Toggle):
    """Includes drops from animals like lizards, mice, scorpions and birds"""
    display_name = "Include small animal drops"


class EnableRinLocations(Choice):
    """Includes rin pickups from chests and other breakables that give at least 5 rin"""
    display_name = "Include rin locations"
    option_no = 0
    option_chests_only = 1
    option_everything = 2
    default = 0


class StartWithWoodenBat(DefaultOnToggle):
    """Start out with wooden bat"""
    display_name = "Start with wooden bat"


class OpenPanseloGates(Toggle):
    """Opens the Panselo gates by default. The gates require a weapon to be opened. Enabling this setting will increase the amount of starting locations"""
    display_name = "Open Panselo gates"


class UpgradableBats(Toggle):
    """Instead of finding bats of random tiers, upgrade up one tier every time you find a bat"""
    display_name = "Upgradable bats"


class UpgradableTools(Toggle):
    """Upgradable tools are found in order. e.g. civilian crossbow is always found before double crossbow"""
    display_name = "Upgradable moonstone tools"


class UpgradableSpear(Toggle):
    """Instead of Sonic Spear and Spear Bomb being two separate items, you will always find Sonic Spear first and then upgrade with the Spear Bomb"""
    display_name = "Upgradable Spear"


@dataclass
class PhoaOptions(PerGameCommonOptions):
    enable_npc_gifts: EnableNpcGifts
    enable_misc: EnableMisc
    shop_sanity: EnableShopSanity
    enable_small_animal_drops: EnableSmallAnimalDrops
    enable_rin_locations: EnableRinLocations
    start_with_wooden_bat: StartWithWoodenBat
    open_panselo_gates: OpenPanseloGates
    upgradable_bats: UpgradableBats
    upgradable_tools: UpgradableTools
    upgradable_spear: UpgradableSpear
    death_link: DeathLink

    def get_slot_data_dict(self) -> dict[str, Any]:
        return self.as_dict(
            "enable_npc_gifts",
            "enable_misc",
            "shop_sanity",
            "enable_small_animal_drops",
            "enable_rin_locations",
            "start_with_wooden_bat",
            "open_panselo_gates",
            "upgradable_bats",
            "upgradable_tools",
            "upgradable_spear",
            "death_link"
        )


phoa_option_groups: list[OptionGroup] = [
    OptionGroup(
        "Progress Locations",
        [
            EnableNpcGifts,
            EnableMisc,
            EnableShopSanity,
            EnableSmallAnimalDrops,
            EnableRinLocations,
        ],
    ),
    OptionGroup(
        "Item Randomizer Modes",
        [
            StartWithWoodenBat,
            OpenPanseloGates,
            UpgradableBats,
            UpgradableTools,
            UpgradableSpear,
        ],
    ),
]
