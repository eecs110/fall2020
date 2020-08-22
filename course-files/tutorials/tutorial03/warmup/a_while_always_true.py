import time
'''
A few things to note here:
    1. The while loop never terminates. It will print this greeting until
       you cancel out of the program (Ctl+C), and "Program terminated"
       will never print.
    2. This is known as an infinite loop. These kinds of loops are useful
       for animations (or anything that you want to keep running).
    3. The time.sleep(1) is important here. Without the pause, the
       program will execute the code as fast as it can (very fast) and use 
       up all of your RAM (try removing the time.sleep(1) to see what 
       happens).
'''


while True:
    print('Hello! How are you doing today (this will go on forever)?')
    time.sleep(1)

print('Program terminated')