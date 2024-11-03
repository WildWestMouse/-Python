def find_common_participants(string_1, string_2, split=","):  # TODO Напишите функцию find_common_participants
    list_1 = string_1.split(split)
    list_2 = string_2.split(split)
    names = list()
    for item_1 in range(len(list_1)):
        for item_2 in range(len(list_2)):
            if list_1[item_1] == list_2[item_2]:
                names.append(list_1[item_1])
    return  names


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))# TODO Провеьте работу функции с разделителем отличным от запятой
