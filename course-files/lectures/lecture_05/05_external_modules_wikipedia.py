# To get this program to work, you must install wikipedia using pip:
# pip install wikipedia

import wikipedia

term = input('What do you want to search for? ')
results = wikipedia.search(term)

print(results)
print(*results, sep='\n\n')

page = wikipedia.page('Northwestern_University')
print(page.content)