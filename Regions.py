from typing import Dict, List, NamedTuple


class PhoaRegionData(NamedTuple):
    connecting_regions: List[str] = []

region_data_table: Dict[str, PhoaRegionData] = {
    "Menu": PhoaRegionData(["Panselo Village"]),
    "Panselo Village": PhoaRegionData(["Panselo (Region)"]),
    "Panselo (Region)": PhoaRegionData([
        "Panselo Village",
        "Doki Forest"
    ]),
    "Doki Forest": PhoaRegionData([
        "Panselo (Region)",
        "Anuri Temple",
    ]),
    "Anuri Temple": PhoaRegionData(["Doki Forest"]),
}