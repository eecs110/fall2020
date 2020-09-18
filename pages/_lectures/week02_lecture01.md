---
layout: module
title: The Building Blocks
type: lecture
draft: 0
num: 3
show_schedule: 1
description:
  - Variables, operators, and data types
  - Installing Python3 & VS Code
due_date: 2020-09-21
# slides:
#   - url: https://docs.google.com/presentation/d/1iDpJk0b8hVmI9IDBkmCdehQ_l_F3FYY1FvNWpThB13U/edit?usp=sharing
#     title: The Building Blocks of Programming
#   - url: https://docs.google.com/presentation/d/1vG9sooc19rLiRMlqdjC3U_OlGrg7kd13hEJQkYvEgRQ/edit?usp=sharing
#     title: Supplementary Slides for Live Lecture
# videos:
#    - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=a06db80a-e42d-4f4e-9559-ab96012be392
#      duration: |
#         06:22
#      title: Using the Lecture Files
#    - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=41a588ed-e8f9-4a02-a183-ab96012e0753
#      duration: |
#         14:03
#      title: Data Types & Variables
#    - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=74153def-e372-483c-a37b-ab96013411e8
#      title: Operators
#      duration: |
#         08:36
#    - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=2930cea4-4821-41a0-ab70-ab960136b2f4
#      title: Built-in Functions
#      duration: |
#         13:31
#    - url: https://northwestern.zoom.us/rec/share/7MVeBuHq9XFLfpX_2mjuZoQxG978X6a803cfqKJYy0k7ifhtnsf_MpUsQuT4Dck3
#      live: 1
#      title: Practice with variables, constants, & operators
#      duration: |
#         01:23:07

readings:
  - title: "Ch2: Variables"
    author: "Severance"
    url: https://www.py4e.com/html3/02-variables
    video_url: https://www.py4e.com/lessons/memory
  - title: "Ch2: Variables"
    author: "Heinold"
    url: https://www.brianheinold.net/python/A_Practical_Introduction_to_Python_Programming_Heinold.pdf

extras:
  - title: "Tutorial Signups"
    comments: "You MUST sign up for a tutorial session"
    url: "https://docs.google.com/spreadsheets/d/1twZ2NDfyu0jVgvb4SMS2Cd9KEwwcPN0BZvLg0XMJuh8/edit"
    external: 1

exercise_url: "lecture03.zip"
---

<img class="module-image" src="/fall2020/assets/images/lectures/lecture_02_blocks.jpg" />Python (and all programmming languages) are made up of very small "words" (like nouns and verbs) that can be composed into meaningful "sentances" (i.e. code blocks that do something useful). Today we are going to review some of the basic building blocks of code, including data types, operators, and variables.<br><br>In addition to the lectures and videos, there are also some sample python files that you will need to download and run (using IDLE). If, for any reason, you are having trouble installing IDLE (instructions can be found in the first part of [homework 1](../assignments/hw1)), reach out to your TA or sign-up for an office hours session. Please keep your files organized (as explained in hw01). I recommend a folder structure like this:

```
cs110
    |-- homework
    │   |-- hw01
    │   |-- hw02
    |   ...
    |
    |-- lectures
        |-- lecture01
        |-- lecture02
        ...
```