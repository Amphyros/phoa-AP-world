from BaseClasses import CollectionState


class PhoaLogic:
    player: int

    def __init__(self, player: int):
        self.player = player

    def has_anuri_temple_access(self, state: CollectionState) -> bool:
        return state.has_any({"Slingshot", "Bombs"}, self.player)

    def can_activate_weapon_switch(self, state: CollectionState) -> bool:
        return True
        # return state.has_any({"Progressive_bat", "Slingshot", "Bombs"})

    def can_kill_slargummy(self, state: CollectionState) -> bool:
        return True
        # return state.has_any({"items"}, self.player)
