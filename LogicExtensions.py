from BaseClasses import CollectionState


class PhoaLogic:
    player: int

    def __init__(self, player: int):
        self.player = player

    def has_anuri_temple_access(self, state: CollectionState) -> bool:
        return state.has_any({"Slingshot", "Bombs"}, self.player)

    def has_bat(self, state: CollectionState) -> bool:
        return state.has_any({"Wooden Bat", "Composite Bat"}, self.player)

    def has_slingshot(self, state: CollectionState) -> bool:
        return state.has_any({"Slingshot", "Treble Shot"}, self.player)

    def has_bombs(self, state: CollectionState) -> bool:
        return state.has_any({"Bombs", "Remote Bombs"}, self.player)

    def has_crossbow(self, state: CollectionState) -> bool:
        return state.has_any({"Civilian Crossbow", "Double Crossbow"}, self.player)

    def has_sonic_spear(self, state: CollectionState) -> bool:
        return state.has("Sonic Spear", self.player)

    def has_fishing_rod(self, state: CollectionState) -> bool:
        return state.has_any({"Fishing Rod", "Serpent Rod"}, self.player)

    def has_light_source(self, state: CollectionState) -> bool:
        return state.has_any({"Refurbished Crank Lamp", "Crank Lamp", "Neutron Lamp"}, self.player)

    def has_anuri_pearlstones(self, amount: int, state: CollectionState) -> bool:
        return state.has("Anuri Pearlstone", self.player, amount)

    def can_use_spear_bomb(self, state: CollectionState) -> bool:
        return state.has_all({"Sonic Spear", "Spear Bomb"}, self.player)

    def has_explosives(self, state: CollectionState) -> bool:
        return (self.has_bombs(state)
                or self.can_use_spear_bomb(state)
                or state.has("Kobold Blaster", self.player))

    def can_deal_damage(self, state: CollectionState) -> bool:
        return (self.has_bat(state)
                or self.has_slingshot(state)
                or self.has_bombs(state)
                or self.has_crossbow(state)
                or self.has_sonic_spear(state)
                or state.has_any({"Refurbished Crank Lamp", "Kobold Blaster"}, self.player))

    def can_reasonably_kill_enemies(self, state: CollectionState) -> bool:
        return (self.has_bat(state)
                or (self.has_slingshot(state))
                or self.has_bombs(state)
                or self.has_crossbow(state)
                or self.has_sonic_spear(state)
                or state.has_any({"Kobold Blaster"}, self.player))

    def can_hit_switch_from_a_distance(self, state: CollectionState, bombless: bool = False) -> bool:
        return (self.has_slingshot(state)
                or (self.has_bombs(state) and not bombless)
                or self.has_crossbow(state)
                or self.has_sonic_spear(state)
                or state.has("Kobold Blaster", self.player))
