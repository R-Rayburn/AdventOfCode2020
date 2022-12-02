TICKER_TAPE = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

GREATER_THAN = ['cats', 'trees']
LESS_THAN = ['pomeranians', 'goldfish']

with open('data.txt', 'r') as file:
    aunt_sues = file.read().split('\n')

def format_sue(sue):
    _, sue, *attributes = sue.split(' ')
    attributes = [attributes[n:n+2] for n in range(0, len(attributes), 2)]
    return sue.replace(':', ''), {k.replace(':', ''):int(v.replace(',', '')) for k, v in attributes}

def get_sue_info(sues):
    sue_info = {}
    for sue in sues:
        number, attributes = format_sue(sue)
        sue_info[number] = attributes
    return sue_info


def filter_out_incorrect_sues(sues):
    sue_info = get_sue_info(sues)
    for key in TICKER_TAPE:
        sues_to_remove = []
        for sue in sue_info.keys():
            if key in sue_info[sue].keys() and TICKER_TAPE[key] != sue_info[sue][key]:
                sues_to_remove.append(sue)
        for sue in sues_to_remove:
            sue_info.pop(sue)
    return sue_info



print(filter_out_incorrect_sues(aunt_sues))


def filter_out_incorrect_sues_p2(sues):
    sue_info = get_sue_info(sues)
    for key in TICKER_TAPE:
        sues_to_remove = []
        for sue in sue_info.keys():
            if key in sue_info[sue].keys():
                if (key in GREATER_THAN and TICKER_TAPE[key] >= sue_info[sue][key])\
                    or (key in LESS_THAN and TICKER_TAPE[key] <= sue_info[sue][key])\
                    or (key not in LESS_THAN and key not in GREATER_THAN and TICKER_TAPE[key] != sue_info[sue][key]):
                    sues_to_remove.append(sue)
        for sue in sues_to_remove:
            sue_info.pop(sue)
    return sue_info

print(filter_out_incorrect_sues_p2(aunt_sues))

