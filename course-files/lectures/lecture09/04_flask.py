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
                <title>Hi CS110!</title>
                <style>
                    img {{ width: 300px; }}
                </style>
            </head>
            <body>
                <h1>Hey There, CS110!</h1>
                <p>This is my dog Seamus.</p>
                <img src="{seamus}" 
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
    return template.format(
        seamus=base_url + random.choice(seamus_pics),
        border_width=5,
        border_color='hotpink'
    )

if __name__ == "__main__":
    app.run()