numbers = [
    76, 76, 76, 72, 76, 79, 67, 72, 67, 64, 69, 71,
    70, 69, 67, 76, 79, 81, 77, 79, 76, 72, 74, 71
]

# Solution 1 (of many), using modulus:
counter = 0
for num in numbers:
    if counter % 3 == 0:
        print(num)
    counter += 1
# end Solution 1

# Solution 2 (of many), using range function:
for i in range(0, len(numbers), 3):  # start at 0, end at len(numbers), increment by 3
    print(numbers[i])
