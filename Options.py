from dataclasses import dataclass
from Options import DefaultOnToggle, Toggle, PerGameCommonOptions, DeathLink

class EnableHeartRubies(DefaultOnToggle):
    """Include Heart Rubies in the item pool"""
    display_name = "Include Heart Ruby locations"

class EnableEnergyGems(DefaultOnToggle):
    """Include Energy Gems in the item pool"""
    display_name = "Include Energy Gem locations"

class EnableMoonstones(DefaultOnToggle):
    """Include Moonstones in the item pool"""
    display_name = "Include Moonstones locations"

@dataclass
class PhoaOptions(PerGameCommonOptions):
    heart_rubies: EnableHeartRubies
    energy_gems: EnableEnergyGems
    moonstones: EnableMoonstones
    death_link: DeathLink