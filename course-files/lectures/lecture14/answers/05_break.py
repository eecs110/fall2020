numbers = [
    76, 76, 76, 72, 76, 79, 67, 72, 67, 64, 69, 71,
    70, 69, 67, 76, 79, 81, 77, 79, 76, 72, 74, 71
]

# Challenge: using a for loop, break out of the loop if you
# get to a number that equals 67

for num in numbers:
    if num == 67:
        print('just reached 67!')
        break
    print(num)
