import utils


def kg_to_pounds(weight):
    return weight * 2.20462


def pounds_to_kg(weight):
    return weight / 2.20462


integers = [12, 11, 16, 14, 18, 14, 11, 16, 12]
print(utils.max_number(integers))
print(max(integers))
