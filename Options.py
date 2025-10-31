from dataclasses import dataclass
from Options import Toggle, PerGameCommonOptions, DeathLink, Choice


class EnableMisc(Toggle):
    """Include miscellaneous locations and items"""
    display_name = "Include miscellaneous"

class EnableSmallAnimalDrops(Toggle):
    """Includes drops from animals like lizards, mice, scorpions and birds"""
    display_name = "Include small animal drops"

class EnableRinLocations(Choice):
    """Includes rin pickups from chests and other breakables that give at least 5 rin"""
    display_name = "Include rin locations"
    options_No = 0
    option_Chests_only = 1
    option_Everything = 2

@dataclass
class PhoaOptions(PerGameCommonOptions):
    enable_misc: EnableMisc
    enable_small_animal_drops: EnableSmallAnimalDrops
    enable_rin_locations: EnableRinLocations
    death_link: DeathLink
