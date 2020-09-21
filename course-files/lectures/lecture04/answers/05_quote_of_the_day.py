# given the list of inspirational quotes, write a program that picks a different
# one everytime your computer runs this program
import random

quotes = [
    '“We May Encounter Many Defeats But We Must Not Be Defeated.” – Maya Angelou',
    '“The Way Get Started Is To Quit Talking And Begin Doing.” – Walt Disney',
    '“Security Is Mostly A Superstition. Life Is Either A Daring Adventure Or Nothing.” – Life Quote By Helen Keller',
    '“The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty.” – Winston Churchill',
    '“Don’t Let Yesterday Take Up Too Much Of Today.” – Will Rogers',
    '“You Learn More From Failure Than From Success. Don’t Let It Stop You. Failure Builds Character.” – Unknown',
    '“If You Are Working On Something That You Really Care About, You Don’t Have To Be Pushed. The Vision Pulls You.” – Steve Jobs',
]

selection = random.randint(0, len(quotes) - 1)
print()
print(quotes[selection])
print()