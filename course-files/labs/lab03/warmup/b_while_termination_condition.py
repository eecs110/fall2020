import time
'''
A few things to note here:
    1. A counter is initialized before the while loop begins.
    2. The counter is updated each time the code block within the while
       loop executes.
    3. If counter is less than 5, the block executes, otherwise, the 
       while loop terminates.
    4. The condition is always checked before each iteration.
'''

counter = 0
while counter < 5:
    print('Hello! How are you doing today?')
    time.sleep(0.5)
    counter += 1
    
print('Program terminated')