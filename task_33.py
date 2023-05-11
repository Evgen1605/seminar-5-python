# Хакер Василий получил доступ к классному журналу
# и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.
# [1, 2, 3, 1, 1, 3, 4, 5, 5, 5] -> [1, 2, 3, 1, 1, 3, 4, 1, 1, 1]


# решение  в группе
def change_nums(arr):
    max_num = max(arr)
    min_num = min(arr)
    for i in range(len(arr)):
        if arr[i] == max_num:
            arr[i] = min_num
    return arr


arr = [1, 2, 3, 4, 4, 5, 5, 3, 2]
print(change_nums(arr))


# решение в группе через рекурсию
lst = list(map(int, input("list: ").split()))


def downgrade(some_list, max_grade, min_grade):
    if max_grade not in lst:
        return some_list
    ind = lst.index(max_grade)
    lst[ind] = min_grade
    return downgrade(some_list, max_grade, min_grade)


print(downgrade(lst, max(lst), min(lst)))


# решение преподавателя
def change_marks(marks: list[int]) -> list[int]:
    """Рекурсивная замена максимальных оценок минимальными"""
    max_mark = max(marks)
    min_mark = min(marks)
    marks[marks.index(max_mark)] = min_mark
    if max_mark not in marks:
        return marks
    return change_marks(marks)


print([1, 5, 3, 1, 2, 3, 5, 4, 5, 4])
print(change_marks([1, 5, 3, 1, 2, 3, 5, 4, 5, 4]))


# def change_marks(marks: list[int]) -> list[int]:
#     """Рекурсивная замена максимальных оценок минимальными"""

#     max_mark = max(marks)
#     min_mark = min(marks)
#     marks[marks.index(max_mark)] = min_mark

#     if max_mark not in marks:
#         return marks
#     return change_marks(marks)


# print(change_marks([1, 5, 3, 1, 2, 3, 5, 4, 5, 4]))

# a = [1, 2, 3, 1, 1, 3, 4, 5, 5, 5]
# print(a.index(5))

# a[a.index(5)] = 1
# print(a)
