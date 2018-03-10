import collections
import json
import logging

Troops = collections.namedtuple('Troops',
                                ['inf', 'arch', 'calv', 'seige'], verbose=True)

LEVEL1 = "Level 1"
LEVEL2 = "Level 2"
LEVEL3 = "Level 3"
LEVEL4 = "Level 4"
LEVELALL = "all"

TYPE_INF = "Infantry"
TYPE_RNG = "Ranged"
TYPE_CAV = "Calvery"
TYPE_SEG = "Seige"

TYPE_INF_INDEX = 0
TYPE_RNG_INDEX = 1
TYPE_CAV_INDEX = 2
TYPE_SEG_INDEX = 3


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


def unit_classes():
    return [TYPE_INF, TYPE_RNG, TYPE_CAV, TYPE_SEG]


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
    return troops


def calculate_totals(troops):
    total_troops = {}
    total_troops[LEVEL1] = sum(troops[LEVEL1])
    total_troops[LEVELALL] = total_troops[LEVEL1]
    total_troops[LEVEL2] = sum(troops[LEVEL2])
    total_troops[LEVELALL] += total_troops[LEVEL2]
    total_troops[LEVEL3] = sum(troops[LEVEL3])
    total_troops[LEVELALL] += total_troops[LEVEL3]
    total_troops[LEVEL4] = sum(troops[LEVEL4])
    total_troops[LEVELALL] += total_troops[LEVEL4]
    return total_troops


def calculate_type_percents(troops):
    log = logging.getLogger('Lords.test_precentstroop_type')
    total_troop_type = {}
    troop_type_percent = {}
    unit_class = unit_classes()
    totals = calculate_totals(troops)
    total_troop_type[unit_class[TYPE_CAV_INDEX]] = (
        troops[LEVEL1].inf + troops[LEVEL2].inf +
        troops[LEVEL3].inf + troops[LEVEL4].inf)
    total_troop_type[unit_class[TYPE_INF_INDEX]] = (
        troops[LEVEL1].arch + troops[LEVEL2].arch +
        troops[LEVEL3].arch + troops[LEVEL4].arch)
    total_troop_type[unit_class[TYPE_RNG_INDEX]] = (
        troops[LEVEL1].calv + troops[LEVEL2].calv +
        troops[LEVEL3].calv + troops[LEVEL4].calv)
    total_troop_type[unit_class[TYPE_SEG_INDEX]] = (
        troops[LEVEL1].seige + troops[LEVEL2].seige +
        troops[LEVEL3].seige + troops[LEVEL4].seige)
    for unit_type in unit_class:
        if total_troop_type[unit_type] == 0:
            troop_type_percent[unit_type] = 0.0
        else:
            log.info('type %f all %f' % (total_troop_type[unit_type],
                                         totals[LEVELALL]))
            troop_type_percent[unit_type] = int(
                float(total_troop_type[unit_type]) /
                float(totals[LEVELALL]) * 100)
    return total_troop_type, troop_type_percent


def calculate_percents(troops, totals):
    percents = collections.defaultdict(list)
    if totals[LEVEL1] == 0:
        percents[LEVEL1].extend([0, 0, 0, 0])
    else:
        percents[LEVEL1].append(troops[LEVEL1].inf /
                                float(totals[LEVEL1]))
        percents[LEVEL1].append(troops[LEVEL1].arch /
                                float(totals[LEVEL1]))
        percents[LEVEL1].append(troops[LEVEL1].calv /
                                float(totals[LEVEL1]))
        percents[LEVEL1].append(troops[LEVEL1].seige /
                                float(totals[LEVEL1]))
    if totals[LEVEL2] == 0:
        percents[LEVEL2].extend([0, 0, 0, 0])
    else:
        percents[LEVEL2].append(troops[LEVEL2].inf /
                                float(totals[LEVEL2]))
        percents[LEVEL2].append(troops[LEVEL2].arch /
                                float(totals[LEVEL2]))
        percents[LEVEL2].append(troops[LEVEL2].calv /
                                float(totals[LEVEL2]))
        percents[LEVEL2].append(troops[LEVEL2].seige /
                                float(totals[LEVEL2]))
    if totals[LEVEL3] == 0:
        percents[LEVEL3].extend([0, 0, 0, 0])
    else:
        percents[LEVEL3].append(troops[LEVEL3].inf /
                                float(totals[LEVEL3]))
        percents[LEVEL3].append(troops[LEVEL3].arch /
                                float(totals[LEVEL3]))
        percents[LEVEL3].append(troops[LEVEL3].calv /
                                float(totals[LEVEL3]))
        percents[LEVEL3].append(troops[LEVEL3].seige /
                                float(totals[LEVEL3]))
    if totals[LEVEL4] == 0:
        percents[LEVEL4].extend([0, 0, 0, 0])
    else:
        percents[LEVEL4].append(troops[LEVEL4].inf /
                                float(totals[LEVEL4]))
        percents[LEVEL4].append(troops[LEVEL4].arch /
                                float(totals[LEVEL4]))
        percents[LEVEL4].append(troops[LEVEL4].calv /
                                float(totals[LEVEL4]))
        percents[LEVEL4].append(troops[LEVEL4].seige /
                                float(totals[LEVEL4]))
    return percents


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
