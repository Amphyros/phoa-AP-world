from dataclasses import dataclass
from Options import Toggle, PerGameCommonOptions, DeathLink


class EnableMisc(Toggle):
    """Include miscellaneous locations and items"""
    display_name = "Include miscellaneous"

class EnableSmallAnimalDrops(Toggle):
    """Includes drops from animals like lizards, mice, scorpions and birds"""
    display_name = "Include small animal drops"

@dataclass
class PhoaOptions(PerGameCommonOptions):
    enable_misc: EnableMisc
    enable_small_animal_drops: EnableSmallAnimalDrops
    death_link: DeathLink
