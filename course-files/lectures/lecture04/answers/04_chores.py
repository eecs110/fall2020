chores = [
    'Feed the dog',
    'Take out the trash',
    'Call Alex',
    'Study for test',
    'Go shopping',
    'Do the dishes'
]

# you will learn more about the while loop in a few weeks. For now, all you need
# to know is that it repeats the statements inside of the while block until the 
# while condition (len(chores) > 0) is False:
while len(chores) > 0:
    print('\nHere are your list of chores that you have left to do:')
    print(chores)
    completed = input('Type the index of the chore you\'ve completed: ')
    chore = chores.pop(int(completed))
    print('Congrats! You just finished:', chore)

print('\nHorray! You\'re done!')
