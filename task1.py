import random
i = 1
random_numbers = []
while i <= 10:
    random_numbers.append(round(random.uniform(1.00, 100.00),2))
    i += 1
greatest_number = max(random_numbers)
print(greatest_number)