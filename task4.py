import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file_csv) -> list[dict]:
    ...  # TODO реализовать конвертер из csv в json

    list_dict = []
    f = open(file_csv, 'r', encoding='utf8')
    list_ = f.readlines()  # считывает все строки в список и возвращает список
    f.close()

    title = list_[0].rstrip().split(',')

    for line in list_[1:]:
        dict_ = {}
        for i, str in enumerate(line.rstrip().split(',')):
            dict_[title[i]] = str
        list_dict.append(dict_)


    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))



