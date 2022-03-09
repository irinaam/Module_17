a = [int(x) for x in input("Введите последовательность через пробел:").split()]

element = int(input("Введите любое число:"))

def binary_search(a, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2 # находим середину
    if a[middle] == element:     # если элемент в середине
        return middle - 1,
    elif element < a[middle]: # если элемент меньше элемента в середине
        return binary_search(a, element, left, middle - 1)
    else:
        return binary_search(a, element, middle + 1, right)

if element == min(a) or element == max(a):
    print("Ошибка")

print(binary_search(sorted(a), element, 0, len(a)))