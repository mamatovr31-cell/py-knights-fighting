from app.skil.data import KNIGHTS
from app.skil.factories import build_knights
from app.skil.model import Knight


pairs = [("lancelot", "mordred"), ("arthur", "red_knight")]
knights = build_knights(KNIGHTS)


def battle(
        knights: dict[str, Knight],
) -> dict[str, int]:
    result = {}
    a = knights["lancelot"]
    b = knights["mordred"]
    c = knights["arthur"]
    d = knights["red_knight"]
    damage_a_to_b = max(0, a.power - b.protection)
    damage_b_to_a = max(0, b.power - a.protection)
    new_hp_a = max(0, a.hp - damage_b_to_a)
    new_hp_b = max(0, b.hp - damage_a_to_b)
    damage_c_to_d = max(0, c.power - d.protection)
    damage_d_to_c = max(0, d.power - c.protection)
    new_hp_c = max(0, c.hp - damage_d_to_c)
    new_hp_d = max(0, d.hp - damage_c_to_d)
    result[a.name] = new_hp_a
    result[b.name] = new_hp_b
    result[c.name] = new_hp_c
    result[d.name] = new_hp_d
    return result
