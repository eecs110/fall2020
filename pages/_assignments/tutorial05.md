---
layout: assignment-two-column
title: |
    For Loops Activity
description:
    - practice with for loops
    - practice with iterating through a tuple
    - practice writing functions
type: tutorial
abbreviation: Tutorial 5
points: 3
draft: 0
num: 5
due_date: 2020-10-21
    
---

<a class="nu-button" href="/fall2020/course-files/tutorials/tutorial05.zip" target="_blank">
    Lab Starter Files <i class="fas fa-download"></i>
</a> 

<img class="module-image" src="/fall2020/assets/images/tutorial04/heart.png" />In this lab, you are going to design a customizable function that creates an image of **any** pixel art that can be represented as rows and columns of integers. The data structure that we will use to store these rows and columns of integers will be a "tuple of tuples" (see below). The purpose of this exercise is to help you feel a little bit more comfortable with tuples (and sequences in general), iteration, and functions. In addition to pixel art, many different kinds of entities can also be expressed using similar data formats (JPEG images, songs, DNA sequences, whatever).

## Introduction: New Data Representations
Below are two examples of two "tuple of tuples" that represent pixel art specifications. Note that "Frank" is made up of 11 rows and 9 columns, and the heart is 14 rows and 19 columns. Each number in the tuple represents a distinct color. 0 indicates that no color should be used (an empty pixel), but you get to pick which colors to use to represent 1, 2, and 3.

```python
# Frank
frank = (
    (0, 0, 1, 1, 1, 1, 1, 0, 0),
    (0, 0, 2, 2, 2, 2, 2, 0, 0),
    (0, 0, 2, 2, 2, 2, 2, 0, 0),
    (0, 0, 2, 1, 2, 1, 2, 0, 0),
    (0, 0, 2, 2, 2, 2, 2, 0, 0),
    (0, 2, 3, 3, 3, 3, 3, 2, 0),
    (0, 2, 2, 2, 2, 2, 2, 2, 0),
    (0, 2, 2, 2, 2, 2, 2, 2, 0),
    (0, 0, 1, 1, 1, 1, 1, 0, 0),
    (0, 0, 1, 1, 1, 1, 1, 0, 0),
    (0, 0, 2, 2, 0, 2, 2, 0, 0)
)

# Heart w/smiley face
heart = (
    (0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0),
    (0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 2, 2, 3, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 1, 1, 1),
    (1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1),
    (1, 1, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 1, 2, 2, 2, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0),
    (0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0),
    (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),
    (0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0)
)
```


## Step 1: Update the "draw_row" function
Open `starter.py` and take a look at it. Then run it using IDLE (or a code editor of your choice). You should see the first 6 rows of pixels for each
pixel art object (Frank and the heart). However, everything is being drawn
as a grey square. In other words, the color distinctions aren't being honored (see image below).

<img class="small frame" src="/fall2020/assets/images/tutorial04/before.png" />

For your first task, you will modify the "draw_row" function -- in any way you can think of -- so that the function honors the color distinctions. Remember: a zero means that you shouldn't draw anything in that cell, but the 1, 2, and 3 can be any color that you choose (see image below).

<img class="small frame" src="/fall2020/assets/images/tutorial04/partial.png" />

{:.blockquote-no-margin}
> **If you get stuck**: After you've given it a shot, take a look at `hints/hint1a.py` and `hints/hint1b.py` to consider a few approaches that you might have tried (but of course, there are others).

## Step 2: Replace the repetitive draw_row function calls
Next, you will simplify the repetitive "draw_row" function calls (pictured below) with a "for loop." 

```python
# first 6 rows of frank
draw_row(canvas, frank[0], (10, 50), pixel=20)
draw_row(canvas, frank[1], (10, 70), pixel=20)
draw_row(canvas, frank[2], (10, 90), pixel=20)
...

# first 6 rows of the heart
draw_row(canvas, heart[0], (250, 250), pixel=10)
draw_row(canvas, heart[1], (250, 260), pixel=10)
draw_row(canvas, heart[2], (250, 270), pixel=10)
...
```
You will use 2 "for loops" -- one for `frank` and one for the `heart`. When you're done, the entirety of Frank and the heart should be drawn (see image below).

<img class="small frame" src="/fall2020/assets/images/tutorial04/step2.png" />

{:.blockquote-no-margin}
> **If you get stuck**: After you've given it a shot, take a look at `hints/hint2.py` to get a sense of how you might use a for loop to complete this task. Frank has been done for you. You try doing the heart.

## Step 3: Create a draw_pixel_art function
Now, create a `draw_pixel_art` function, with a function definition that looks like this:

```python
def draw_pixel_art(canvas:Canvas, top_left:tuple, grid:tuple, pixel:int=10):
    # your function body here
    pass
```

If the function is invoked as follows...

```python
draw_pixel_art(canvas, (0, 20), heart)
draw_pixel_art(canvas, (120, 220), frank, pixel=12)
draw_pixel_art(canvas, (420, 250), heart, pixel=8)
draw_pixel_art(canvas, (55, 415), heart, pixel=6)
draw_pixel_art(canvas, (350, 115), heart, pixel=5)
draw_pixel_art(canvas, (315, 380), frank, pixel=15)
draw_pixel_art(canvas, (420, 10), frank, pixel=10)
```

...it will generate the image pictured below.

<img class="medium frame" src="/fall2020/assets/images/tutorial04/step3.png" />

Note that the (x,y) position refers to the top-left corner of where the pixel art will be drawn.

{:.blockquote-no-margin}
> **If you get stuck**: After you've given it a shot, take a look at `hints/hint3.py` to get a sense of how you might implement your `draw_pixel_art` function body.

## Step 4: Enhancements
If you have time (or are turning this assignment in for credit in lieu of attendance), please complete the following enhancements:
1. Modify your function in a way that allows you to customize the color palette. In other words, the user should be able to choose which three colors to use for 1, 2, and 3 (see image below w/different hearts).
2. Create a third "tuple of tuples" to represent a new pixel art drawing. To get ideas, Google "pixel art simple."

<img class="medium frame" src="/fall2020/assets/images/tutorial04/hearts.png" />


## What to turn in (same deal as always)
Please turn in your completed tutorial exercise(s) ON CANVAS by Wednesday night at midnight. To do this, first zip your entire `tutorial05` folder (with your edited files inside), and then upload your zip file to Canvas. Please ensure that your zip file includes **YOUR CODE**.  