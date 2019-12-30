from dice_logic import dice

dice_map = {
    "bd": [dice.set_back_die, "Boost Die"],
    "boost die": [dice.set_back_die, "Boost Die"],
    "set back die": [dice.set_back_die, "Set Back Die"],
    "sbd": [dice.set_back_die, "Set Back Die"],
    "ability die": [dice.ability_die, "Ability Die"],
    "ad": [dice.ability_die, "Ability Die"],
    "difficulty die": [dice.difficulty_die, "Difficulty Die"],
    "dd": [dice.difficulty_die, "Difficulty Die"],
    "proficiency die": [dice.proficiency_die, "Proficiency Die"],
    "pd": [dice.proficiency_die, "Proficiency Die"],
    "challenge die": [dice.challenge_die, "Challenge Die"],
    "cd": [dice.challenge_die, "Challenge Die"],
    "force die": [dice.force_die, "Force Die"],
    "fd": [dice.force_die, "Force Die"],
}
