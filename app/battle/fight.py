from app.skil.data import KNIGHTS
from app.skil.factories import build_knights
from app.skil.model import Knight


pairs = [("lancelot", "mordred"), ("arthur", "red_knight")]
knights = build_knights(KNIGHTS)


def battle(
        knights: dict[str, Knight],
) -> dict[str, int]:
    result = {}
    for knight_a,knight_b in pairs:
        attacker = knights[knight_a]
        defender = knights[knight_b]
        damage_a_to_b = max(0, attacker.power - defender.protection)
        damage_b_to_a = max(0, defender.power - attacker.protection)
        new_hp_a = max(0, attacker.hp - damage_b_to_a)
        new_hp_b = max(0, defender.hp - damage_a_to_b)
        result[attacker.name] = new_hp_a
        result[defender.name] = new_hp_b

    return result
