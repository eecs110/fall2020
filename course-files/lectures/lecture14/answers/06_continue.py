numbers = [
    76, 76, 76, 72, 76, 79, 67, 72, 67, 64, 69, 71,
    70, 69, 67, 76, 79, 81, 77, 79, 76, 72, 74, 71
]

# Challenge: skip over all of numbers that equal 67
for num in numbers:
    if num == 67:
        print('skipping...', num)
        continue
    print(num)
