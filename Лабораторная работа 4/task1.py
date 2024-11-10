import json


def task() -> float:
    with open('input.json') as file:
        data = json.load(file)
        data_sum = sum([dictionary["score"] * dictionary["weight"] for dictionary in data])
    return round(data_sum, 3)


print(task())
