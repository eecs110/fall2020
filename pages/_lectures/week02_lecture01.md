---
layout: module
title: The Building Blocks
type: lecture
draft: 0
num: 3
show_schedule: 1
description:
  - Variables, operators, data types, and built-in functions
due_date: 2020-09-21
quiz_url: https://canvas.northwestern.edu/courses/120087/quizzes/122779
slides:
  - url: https://docs.google.com/presentation/d/1CyzjjjCYtUxCPWFem1hgkgK2Zdv1losXs1A6DzWfD-8/edit?usp=sharing
    title: The Building Blocks of Programming
  - url: https://docs.google.com/presentation/d/1Qsthtvr5hL4A0QG4RV3lqa_CNjp0r3ctFBaj1A5TaEQ/edit?usp=sharing
    title: Supplementary Slides for Live Lecture
videos:
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=270174ec-2451-4c8d-a279-ac3a002e0a1a
     duration: |
        10:51
     title: Using the Lecture Files
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=6fa0d8d0-2741-4897-a770-ac3a00386656
     duration: |
        17:04
     title: Data Types & Variables
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=e405208f-6a48-44d5-8431-ac3a0041daca
     title: Operators
     duration: |
        08:36
   - url: https://northwestern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=521b28fc-4c28-4255-89ca-ac3a0041d9a9
     title: Built-in Functions
     duration: |
        13:31
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
    |-- lectures
    │   -- lecture01
    │   -- lecture02
    │   ...
    |-- tutorials
        |-- tutorial01
        |-- tutorial02
        ...
```