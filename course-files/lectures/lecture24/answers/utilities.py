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
            url = 'https://raw.githubusercontent.com' + link_text.replace('blob', '')
            data_files.append(url)
    return data_files

def get_covid_file_links_no_bs4():
    import json
    file_path = get_file_path('covid_links.json')
    f = open(file_path, 'r')
    data_files = json.loads(f.read())
    f.close()
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
    print('Downloading any new COVID-19 data files...')
    covid_report_links = get_covid_file_links()
    for url in covid_report_links:
        file_name = url.split('/')[-1]
        file_path = get_file_path(file_name, subdirectory='files')
        
        if file_already_exists(file_path):
            # print('Already exists:', file_path)
            pass
        else:
            print('Retrieving:', url)
            download_remote_file(url, file_path)
            time.sleep(sleep_time)

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

def get_moving_average(points, point, interval=3):
    start = max(len(points) - 1, interval-2)
    end = start - interval + 1
    the_range = list(range(start, end, -1))
    sum_of_points = point
    for i in the_range:
        try:
            sum_of_points += points[i][1]
        except:
            sum_of_points += point
    return sum_of_points / interval


def make_bar_chart(data:dict, title='COVID-19 Data'):
    from tkinter import Canvas, Tk
    import random

    gui = Tk()
    gui.title('Bar Chart')
    w = 1200
    h = 600
    chart_height = h - 100
    canvas = Canvas(gui, width=w, height=h)
    canvas.pack()

    # determine scale factor: How do you represent actual
    # COVID-19 Counts based on a 1200x600 canvas?
    max_val = max(*data.values())
    scale_factor = chart_height / max_val
    x = 2

    counter = 0
    trend_line = []
    labels = []
    days = list(data.keys())[50:] #exclude Jan-Feb
    bar_width = (w - 10) / len(days)
    for key in days:
        bar_height = int(data.get(key) * scale_factor)
        y = h - bar_height
        make_rectangle(canvas, (x, y), bar_width, bar_height)
        tokens = key.split('-')

        # add a label if it's the first of the month:
        if tokens[1] == '01':
            labels.append({
                'position': (x, y),
                'day_text': tokens[0] + '/' + tokens[1],
                'num_cases': data.get(key)
            })
        running_average = get_moving_average(trend_line, y)
        # print('running_average', y, running_average)
        trend_line.append((x, running_average))
        x += bar_width
        counter += 1

    # add final point:
    labels.append({
        'position': (x, y),
        'day_text': tokens[0] + '/' + tokens[1],
        'num_cases': data.get(key)
    })
    running_average = get_moving_average(trend_line, y)
    trend_line.append((x, running_average))

    # draw line: a proxy for trend line, though not the
    # same as a running average.
    # print(trend_line)
    make_line(canvas, trend_line, curvy=True, color='#222222')

    # draw labels:
    for label in labels:
        x, y = label.get('position')
        make_circle(canvas, (x, y), 3, color='black')
        label_text = '{0}:\n{1:,d} cases'.format(
            label.get('day_text'),
            label.get('num_cases')
        )
        label = canvas.create_text(
            (x, y-30), 
            text=label_text,
            font=('Arial', 14),
            anchor='se'
        )
        make_line(canvas, [(x, y, x, h)])
        bbox = canvas.bbox(label)
        # give bbox some padding:
        x1, y1, x2, y2 = bbox
        bbox = (x1 - 2, y1 - 2, x2 + 2, y2 + 2)
        rect = canvas.create_rectangle(bbox, outline="black", fill="white")
        # switch the order:
        canvas.tag_raise(label,rect)

    # chart title:
    canvas.create_text(
        (w/2, 50), 
        text=title,
        font=('Purisa', 40),
        anchor='center'
    )
    canvas.mainloop()