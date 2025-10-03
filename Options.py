from dataclasses import dataclass
from Options import Toggle, PerGameCommonOptions, DeathLink


class EnableMisc(Toggle):
    """Include miscellaneous locations and items"""
    display_name = "Include miscellaneous"


@dataclass
class PhoaOptions(PerGameCommonOptions):
    enable_misc: EnableMisc
    death_link: DeathLink
