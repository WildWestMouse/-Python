numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
a = 0

while numbers[a] is not None:
  a += 1

sum_ = sum(numbers[:a]) + sum(numbers[a+1:])
average_numbers = sum_ / len(numbers)
numbers[a] = average_numbers

print("Измененный список:", numbers)
