numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
varuable = 0

while numbers[varuable] is not None:
  varuable += 1

sum_ = sum(numbers[:varuable]) + sum(numbers[varuable + 1:])
average_numbers = sum_ / len(numbers)
numbers[varuable] = average_numbers

print("Измененный список:", numbers)
