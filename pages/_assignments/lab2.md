---
layout: assignment-two-column
title: Practice with Functions
type: tutorial
abbreviation: Tutorial 2
draft: 1
points: 3
num: 2
description: 
    - Practice creating custom functions
    - Intro to Tkinter
due_date: 2020-09-30
---

<a class="nu-button" href="/fall2020/course-files/labs/lab01.zip" target="_blank">
    Lab Starter Files <i class="fas fa-download"></i>
</a> 

This lab is based on content that is reviewed in Lessons 1-4, and is intended to prepare you for [HW2](../assignments/hw2). Please download the starter files and complete the instructions outlined below. PLEASE ASK LOTS OF QUESTIONS in your lab section. If you've never done this before, there are a lot of little typing / logic / conceptual mistakes that **everyone** makes. Lab is your time to allow yourself to make all of those mistakes so that you can learn from them. 

{: .blockquote-no-margin}
> **LEARNING OBJECTIVES:** 
> In order to prepare you for this week's homework, we wanted to use this lab session to go over a couple of important logistical and conceptual ideas.
>
> 1. Making sure that TKinter is successfully running on your machine
> 1. Creating functions
> 1. Working with parameters & arguments
> 1. Translating specifications into smaller steps that a computer can perform

## Required: Square Challenge
Please open `square_challenge.py` in IDLE, which is located in the `lab01` folder. Take a look at it and then run it. You should see something like this:

<img class="small frame" src="/fall2020/assets/images/lab01/before1.png" />

### A. Create a "make_square" function
In the `square_challenge.py` file, write a function called `make_square` that accepts the following arguments:

1. **canvas** *(Canvas)*: a tkinter Canvas object where you want the square to be drawn.
1. **top_left** *(tuple)*: a tuple -- an point, an (x, y) coordinate -- that defines the top-left position of the square. The first element in the tuple refers to the x-coordinate and the second element in the tuple refers to the y-coordinate.
1. **width** *(int)*: an int that specifies the width (and also height) of the square.
1. **fill_color** *(str, optional)*: a string that represents the color of the square, defaults to a light blue: `#84A9C0`.

In other words, if I invoked your `make_square` function as follows...

`make_square(canvas, (100, 100), 100, fill_color='#84A9C0')`

...your function would draw a 100x100 blue square with its top-left coordinate at position (100, 100), as pictured above.

### B. Use your "make_square" function to create the drawing pictured below
When you've finished with your `make_square` function, create the pattern pictured below by calling your function with the following arguments (below). Copy the following code and pasting it ***below*** your function definition, but ***above*** the helpers.make_grid(...) function:

```python
# center blue block
make_square(canvas, (100, 100), 100)

# dark green blocks
make_square(canvas, (0, 0), 100, fill_color='#5B9279')
make_square(canvas, (200, 0), 100, fill_color='#5B9279')
make_square(canvas, (0, 200), 100, fill_color='#5B9279')
make_square(canvas, (200, 200), 100, fill_color='#5B9279')

# light green blocks
make_square(canvas, (50, 200), 50, fill_color='#8FCB9B')
make_square(canvas, (200, 200), 50, fill_color='#8FCB9B')
make_square(canvas, (50, 50), 50, fill_color='#8FCB9B')
make_square(canvas, (200, 50), 50, fill_color='#8FCB9B')
```

<img class="small frame" src="/fall2020/assets/images/lab01/after1.png" />

### C. Use your "make_square" function to create your own drawing

Now, alter the code above to make your own drawing (anything that you can compose with squares). Feel free to alter the colors, positions, and sizes of your squares. Here is a <a href="https://coolors.co/app" target="_blank">link to a color generator</a> (to browse different hexidecimal color codes, press the spacebar).


## More Practice (If Time): Triangle Challenge
Please open `triangle_challenge.py` in IDLE (also located in the `lab01` folder). Take a look at it and then run it. You should see something like this:

<img class="medium frame" src="/fall2020/assets/images/lab01/before2.png" />

### A. Create a "make_triangle_left" function
In the `triangle_challenge.py` file, create a function called `make_triangle_left` that draws a 45-45-90-degree right triangle, where the right angle is positioned at the bottom-left corner (as pictured above). It accepts the following arguments:

1. **canvas** *(Canvas)*: a tkinter Canvas object where you want the triangle to be drawn.
1. **bottom_left** *(tuple)*: a tuple -- an point, an (x, y) coordinate -- that defines the bottom-left position of the triangle. The first element in the tuple refers to the x-coordinate and the second element in the tuple refers to the y-coordinate.
1. **height** *(int)*: an int that specifies the height / length of the triangle.
1. **fill_color** *(str, optional)*: a string that represents the color of the triangle, defaults to a light blue: `#84A9C0`.


### B. Create a "make_triangle_right" function
Below the make_triangle_left function that you just made, create a function called `make_triangle_right` that draws a 45-45-90-degree right triangle, where the right angle is positioned at the bottom-right corner. 

It accepts the following arguments:

1. **canvas** *(Canvas)*: a tkinter Canvas object where you want the triangle to be drawn.
1. **bottom_right** *(tuple)*: a tuple -- an point, an (x, y) coordinate -- that defines the bottom-left position of the triangle. The first element in the tuple refers to the x-coordinate and the second element in the tuple refers to the y-coordinate.
1. **height** *(int)*: an int that specifies the height / length of the triangle.
1. **fill_color** *(str, optional)*: a string that represents the color of the triangle, defaults to a light blue: `#84A9C0`.

### C. Use your "make_triangle_left" and "make_triangle_right" functions to create a drawing
When you've finished making your `make_triangle_left` and `make_triangle_right` functions, invoke these functions to create the pattern pictured below by copying the following code and pasting it ***below*** your function definition, but ***above*** the helpers.make_grid(...) function:

```python
# row 1
make_triangle_right(canvas, (100, 100), 100, fill_color='#5B9279')
make_triangle_left(canvas, (100, 100), 100, fill_color='#5B9279')
make_triangle_right(canvas, (300, 100), 100, fill_color='#5B9279')
make_triangle_left(canvas, (300, 100), 100, fill_color='#5B9279')
make_triangle_right(canvas, (500, 100), 100, fill_color='#5B9279')

# row 2
make_triangle_left(canvas, (0, 200), 100)
make_triangle_right(canvas, (200, 200), 100)
make_triangle_left(canvas, (200, 200), 100)
make_triangle_right(canvas, (400, 200), 100)
make_triangle_left(canvas, (400, 200), 100)

# row 3
make_triangle_right(canvas, (100, 300), 100, fill_color='#8FCB9B')
make_triangle_left(canvas, (100, 300), 100, fill_color='#8FCB9B')
make_triangle_right(canvas, (300, 300), 100, fill_color='#8FCB9B')
make_triangle_left(canvas, (300, 300), 100, fill_color='#8FCB9B')
make_triangle_right(canvas, (500, 300), 100, fill_color='#8FCB9B')
```

<img class="medium frame" src="/fall2020/assets/images/lab01/after2.png" />

## What to Turn In
As described in the syllabus, there are two ways to earn full participation credit in each lab session:

1. By attending them (synchronously), working through the exercises, and asking questions (as they arise).
2. By turning in the lab exercise(s) ON CANVAS **before** the lab session. Lab exercises will be posted at the beginning of the week (at least 48 hours in advance). 

Whichever option you choose, you will be expected to know the material reviewed in the lab for the exam, and are encouraged to fully complete and submit the lab assignments (though this is not required if you attended the lab).

## Warning for Mac users: The TKinter bug
{% capture my_include %}{% include tkinter_bug_mac.md %}{% endcapture %}
{{ my_include | markdownify }}
