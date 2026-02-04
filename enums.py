from enum import Enum

class Data(Enum):
    name = 'name'
    char_class = 'class'
    race = 'race'
    level = 'level'

enums = {}
for data_type in Data:
    enums.update({data_type: data_type.value})

enum_vals = []
for data_type in Data:
    enum_vals.append(data_type.value)