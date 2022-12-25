import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(file_csv, delimiter=',',new_line='\n') -> list[dict]:
    ...  # TODO реализовать конвертер из csv в json

    list_dict = []

    with open(file_csv, 'r', encoding='utf8') as f:
        title = f.readline().rstrip(new_line).split(delimiter)

        for line in f.readlines():
            list_dict.append(dict(zip(title, line.rstrip(new_line).split(delimiter))))


    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))



