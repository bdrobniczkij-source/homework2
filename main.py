def sum_numbers(numbers):
    return sum(numbers)


numbers = list(map(int, input("Введите числа через пробел: ").split()))
print("Сумма:", sum_numbers(numbers))