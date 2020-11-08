# pip3 install bs4
from bs4 import BeautifulSoup
import requests
import ssl
import urllib.request
import time
import math

def get_file_path(file_name, subdirectory=None):
    import os
    import sys
    dir_path = os.path.dirname(sys.argv[0])
    if subdirectory:
        return os.path.join(dir_path, subdirectory, file_name)
    else:
        return os.path.join(dir_path, file_name)

def file_already_exists(file_path):
    # returns True if it does, False if it doesn't.
    from os import path
    return path.exists(file_path)

def get_files_in_directory(directory):
    import os
    import sys
    from os import listdir
    pwd = os.path.dirname(sys.argv[0])
    full_path = os.path.join(pwd, directory)
    files = listdir(full_path)
    return sorted(files, key=lambda x: x.split('.')[0])

def get_covid_file_links():
    # 1. download web page from the internet
    url = "https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports"
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    file_data = response.read()
    
    # 2. use BeautifulSoup to extract the links:
    soup = BeautifulSoup(file_data, 'html.parser')
    data_files = []
    for a in soup.find_all('a', href=True, text=True):
        link_text = a['href']
        if link_text.find('.csv') != -1:
            url = 'https://raw.githubusercontent.com' + link_text.replace('blob/', '')
            data_files.append(url)
    return data_files

def download_remote_file(url:str, file_path:str):
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    file_data = response.read()

    # create a local file with the 'wb' flag
    f = open(file_path, 'wb')
    f.write(file_data)
    f.close()

def download_all_data_files(sleep_time:float=0.5):
    # your job:
    pass

def make_rectangle(canvas, top_left, width, height, color="#3D9970", tag=None):
    x, y = top_left
    return canvas.create_rectangle(
        [(x, y), (x + width, y + height)], 
        fill=color, 
        width=0,
        tags=tag
    )

def make_line(canvas, coordinates, curvy=False, width=2, tag=None, color='black'):
    canvas.create_line(
        coordinates, 
        width=width, 
        smooth=curvy,
        tag=tag,
        fill=color)

def make_circle(canvas, center, radius, color='#FF4136', tag=None, stroke_width=2, outline=None):
    make_oval(
        canvas, center, radius, radius, color=color, tag=tag,
        stroke_width=stroke_width, outline=outline
    )

def make_oval(canvas, center, radius_x, radius_y, color='#FF4136', tag=None, stroke_width=1, outline=None):
    x, y = center
    return canvas.create_oval(
        [ x - radius_x, y - radius_y, x + radius_x, y + radius_y ],
        fill=color,
        width=stroke_width,
        tags=tag,
        outline=outline
    )

def make_bar_chart(data:list=[], title='COVID-19 Data'):
    # your job (if time):
    from tkinter import Canvas, Tk
    import random

    gui = Tk()
    gui.title('Bar Chart')
    w = 1200
    h = 600
    canvas = Canvas(gui, width=w, height=h)
    canvas.pack()

    # chart title:
    canvas.create_text(
        (w/2, 50), 
        text='Create COVID-19 Visualization Here...',
        font=('Purisa', 40),
        anchor='center'
    )
    canvas.mainloop()