import collections
import json
import logging

Troops = collections.namedtuple('Troops', 'inf, arch calv siege')

LEVEL1 = "Level 1"
LEVEL2 = "Level 2"
LEVEL3 = "Level 3"
LEVEL4 = "Level 4"
LEVELALL = "all"


def unit_names():
    unit_names = {}
    unit_names[LEVEL1] = ["Grunt", "Archer", "Cataphract", "Ballista"]
    unit_names[LEVEL2] = ["Gladiator", "Sharpshooter", "Reptilian Raider",
                          "Catabult"]
    unit_names[LEVEL3] = ["Royal Guard", "Stealth Sniper", "Royal Cavalry",
                          "Fire Trebucket"]
    unit_names[LEVEL4] = ["Heroic FIghter", "Herioc Cannoneer",
                          "Ancient Dreake Rider", "Destroyer"]
    return unit_names


def tag_names():
    tag_names = {}
    tag_names[LEVEL1] = ['inf1', 'arch1', 'cav1', 'seige1']
    tag_names[LEVEL2] = ['inf2', 'arch2', 'cav2', 'seige2']
    tag_names[LEVEL3] = ['inf3', 'arch3', 'cav3', 'seige3']
    tag_names[LEVEL4] = ['inf4', 'arch4', 'cav4', 'seige4']
    return tag_names


def display_levels():
    display_levels = [LEVEL1, LEVEL2, LEVEL3, LEVEL4]
    return display_levels


def process_input(request):
    # process the input
    troops = {}
    troops[LEVEL1] = Troops(int(request.get('inf1', '0')),
                            int(request.get('arch1', '0')),
                            int(request.get('cav1', '0')),
                            int(request.get('seige1', '0')))
    troops[LEVEL2] = Troops(int(request.get('inf2', '0')),
                            int(request.get('arch2', '0')),
                            int(request.get('cav2', '0')),
                            int(request.get('seige2', '0')))
    troops[LEVEL3] = Troops(int(request.get('inf3', '0')),
                            int(request.get('arch3', '0')),
                            int(request.get('cav3', '0')),
                            int(request.get('seige3', '0')))
    troops[LEVEL4] = Troops(int(request.get('inf4', '0')),
                            int(request.get('arch4', '0')),
                            int(request.get('cav4', '0')),
                            int(request.get('seige4', '0')))
    logging.info(troops[LEVEL1])


def calculate_percents(troops):
    percents = {}
    total_troops = {}
    total_troops[LEVEL1] = sum(troops[LEVEL1])
    total_troops[LEVEL2] = sum(troops[LEVEL2])
    total_troops[LEVEL3] = sum(troops[LEVEL3])
    total_troops[LEVEL4] = sum(troops[LEVEL4])
    percents = collections.defaultdict(list)
    percents[LEVEL1].append(troops[LEVEL1].inf / float(total_troops[LEVEL1]))
    percents[LEVEL1].append(troops[LEVEL1].arch / float(total_troops[LEVEL1]))
    percents[LEVEL1].append(troops[LEVEL1].calv / float(total_troops[LEVEL1]))
    percents[LEVEL1].append(troops[LEVEL1].siege / float(total_troops[LEVEL1]))
    percents[LEVEL2].append(troops[LEVEL2].inf / float(total_troops[LEVEL2]))
    percents[LEVEL2].append(troops[LEVEL2].arch / float(total_troops[LEVEL2]))
    percents[LEVEL2].append(troops[LEVEL2].calv / float(total_troops[LEVEL2]))
    percents[LEVEL2].append(troops[LEVEL2].siege / float(total_troops[LEVEL2]))
    percents[LEVEL3].append(troops[LEVEL3].inf / float(total_troops[LEVEL3]))
    percents[LEVEL3].append(troops[LEVEL3].arch / float(total_troops[LEVEL3]))
    percents[LEVEL3].append(troops[LEVEL3].calv / float(total_troops[LEVEL3]))
    percents[LEVEL3].append(troops[LEVEL3].siege / float(total_troops[LEVEL3]))
    percents[LEVEL4].append(troops[LEVEL4].inf / float(total_troops[LEVEL4]))
    percents[LEVEL4].append(troops[LEVEL4].arch / float(total_troops[LEVEL4]))
    percents[LEVEL4].append(troops[LEVEL4].calv / float(total_troops[LEVEL4]))
    percents[LEVEL4].append(troops[LEVEL4].siege / float(total_troops[LEVEL4]))
    return total_troops, percents


def init_data():
    # process the input
    inputs = {}
    inputs[LEVEL1] = Troops(0, 0, 0, 0)
    inputs[LEVEL2] = Troops(0, 0, 0, 0)
    inputs[LEVEL3] = Troops(0, 0, 0, 0)
    inputs[LEVEL4] = Troops(0, 0, 0, 0)
    return inputs


def troops_as_json(troops):
    out = ["{\"troops\":"]
    out.append(json.dumps(troops))
    out.append("}")
    result = "".join(out)
    logging.info(result)
    return result
