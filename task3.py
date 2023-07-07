all_numbers = list(range(1, 101))
result_numbers = []
index = 0
while index < len(all_numbers):
    number = all_numbers[index]
    if number % 7 == 0 and number % 5 != 0:
        result_numbers.append(number)
    index += 1
print(result_numbers)
