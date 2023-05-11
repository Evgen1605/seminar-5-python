# 37. Дано натуральное число *N* и последовательность
# из *N* элементов. Требуется вывести эту последовательность
# в обратном порядке.

# ***Примечание.*** В программе запрещается объявлять
# массивы и использовать циклы (даже для ввода и вывода).
# 5 | 1 2 3 4 5 -> 5 4 3 2 1

# Решение в группе
def rev(num):
    n = input("Enter: ")
    if num == 1:
        return n
    return rev(num - 1) + f" {n}"


print(rev(int(input("Введите длину: "))))

# Решение преподавателя
def reverse(n: int) -> None:
    """Переворот строки рекурсией"""
    if n == 0:
        return print('')
    k = int(input())
    reverse(n - 1)
    return print(k)


n = int(input())
reverse(n)

#  Через составление строки
# def f(n):
#     if n == 0:
#         return ''
#     k = int(input())
#     return f(n - 1) + f' {k}'


# n = int(input())
# print(f(n))
