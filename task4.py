import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(file_csv) -> list[dict]:
    ...  # TODO реализовать конвертер из csv в json

    list_dict = []
    with open(file_csv, 'r', encoding='utf8') as f:
        for i, line in enumerate(f):
            if i == 0:
                title = line.rstrip().split(',')
            else:
                list_dict.append(dict(zip(title, line.rstrip().split(','))))

    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))



