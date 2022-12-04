def delete(list_, index=None):
      # TODO реализовать функцию удаления элемента из списка по индексу

      if index == None:  # или задать значение по умолчанию вх параметра delete(list_, index=-1)
          index = -1

      if index < 0:
          index += len(list_)

      if index <= len(list_) and index >= 0:  # рассматриваем только значения индекса, не "out of range"

          list_ = list_[:index] + list_[index + 1:]

      return (list_)



print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
