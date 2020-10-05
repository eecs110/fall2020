# To get this program to work, you must install wikipedia using pip:
# pip3 install flask

from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def show_page():
    template = '''
        <html>
            <head>
                <title>{my_title}</title>
                <style>
                    img {{ height: 300px; }}
                </style>
            </head>
            <body>
                <h1>{my_title}</h1>
                <p>{quote_of_the_day}</p>
                <img src="{seamus_url}" 
                    style="border: solid {border_width}px {border_color};" />
            </body>
        </html>
    '''
    base_url = 'https://eecs110.github.io/fall2020/assets/images/lectures/'
    seamus_pics = [
        'seamus.jpg',
        'seamus1.jpg',
        'seamus2.jpg'
    ]
    quotes = (
        '“We May Encounter Many Defeats But We Must Not Be Defeated.” – Maya Angelou',
        '“The Way Get Started Is To Quit Talking And Begin Doing.” – Walt Disney',
        '“Security Is Mostly A Superstition. Life Is Either A Daring Adventure Or Nothing.” – Life Quote By Helen Keller',
        '“The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty.” – Winston Churchill',
        '“Don’t Let Yesterday Take Up Too Much Of Today.” – Will Rogers',
        '“You Learn More From Failure Than From Success. Don’t Let It Stop You. Failure Builds Character.” – Unknown',
        '“If You Are Working On Something That You Really Care About, You Don’t Have To Be Pushed. The Vision Pulls You.” – Steve Jobs',
    )
    return template.format(
        my_title='Hey There, CS110!',
        quote_of_the_day=random.choice(quotes),
        seamus_url=base_url + random.choice(seamus_pics) + '?a=b',
        border_width=random.randint(5, 20),
        border_color=random.choice(['hotpink', 'red', 'blue', 'orange'])
    )

if __name__ == "__main__":
    app.run()