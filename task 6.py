list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_number = list_numbers[0]
max_ind = 0


last_number = list_numbers[-1]


for i, current_number in enumerate(list_numbers):
    if current_number >= max_number:
        max_number = current_number
        max_ind = i


list_numbers[-1], list_numbers[max_ind] = max_number, last_number

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]

