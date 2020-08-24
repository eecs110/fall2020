---
layout: assignment-two-column
title: Make a Creature
abbreviation: HW3
type: homework
due_date: 2020-10-07
ordering: 2
points: 8
draft: 1
---

<a class="nu-button" href="/fall2020/course-files/homework/hw03.zip" target="_blank">
    Homework Starter Files <i class="fas fa-download"></i>
</a> 

{: .blockquote-no-margin}
> **LEARNING OBJECTIVES:** 
> 1. More practice working with built-in functions
> 1. Practice writing your own functions

<img class="creature" src="/fall2020/assets/images/hw02/creature.png" /> In this assignment, you are going to write a program to draw a creature of your own design/choosing using <a href="" target="_blank">tkinter</a>. At the end of this assignment, someone should be able to use your function to draw your creature: anywhere on the screen at any size or color. In other words, your function needs to honor the parameters that are passed into it. If you don't quite know what this means (it's a confusing concept for people just learning to program), ask Sarah during class or ask your TAs during lab / office hours.

## Part 1: Design your creature
On paper, sketch out at least 3 creature ideas — it can be different variations of the same creature or all different ones. You can just implement the head of your creature (similar to the bear at the top) or the whole thing — the choice is up to you. Here are some links to ideas:

* <a href="https://images.squarespace-cdn.com/content/v1/53dd4013e4b05d8340b1c32c/1558819051622-BO3Y418I3RW2B4X2UGY4/ke17ZwdGBToddI8pDm48kJveJ6bDu4t8jo69sot7N517gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1UclebCXK_qWyAU_WdFPQdIW8jKJG7706TR3OFKcgb9BQHrvtV3ieEGBkdu4ICJqedg/a-z.jpg?format=1500w" target="_blank">cute monsters</a>
* <a href="https://www.youtube.com/watch?v=yh_A09CrT68" target="_blank">https://www.youtube.com/watch?v=yh_A09CrT68</a>
* <a href="https://www.shutterstock.com/image-vector/ cute-animals-cartoon-illustrator-flat-design-24766713" target="_blank">https://www.shutterstock.com/image-vector/ cute-animals-cartoon-illustrator-flat-design-247667131</a>
* <a href="https://www.pinterest.com/pin/118782508901992203/" target="_blank">https://www.pinterest.com/pin/118782508901992203/</a>
* <a href="https://goo.gl/hKewyL" target="_blank">https://goo.gl/hKewyL</a>

Feel free to post simple creature drawing ideas on the course Piazza under hw3.
From your 3 sketched ideas, select the one that you would like to use for the assignment and draw the creature bigger on a different piece of paper — ideally graph paper — and label the points that will help you to program your creature. 

{: .blockquote-no-margin}
> **NOTE:** Making a simple creature (e.g using 4-8 shapes) is totally fine. You don’t need to get too detailed unless you want to!

## Part 2: Implement your "make_creature" function
Once you are satisfied with your animal concept, create a `make_creature` function, inside of `creature.py`, using any combination of shapes (points, lines, polygons, rectangles, ovals, etc.). Feel free to use the `make_circle` and `make_oval` functions that you already implemented in homework 2. Also feel free to use any of the code in `warm_up.py`.

**Tips**: 
1. Keep it simple (we recommend anywhere between 4-8 shapes)! You can always add more functionality later.
2. Make only one or two changes at a time and then test out those changes by running your `main.py` file. This makes things easier to debug.

Once your function successfully draws the creature that you sketched (in Part 2), you will start adding positional and keyword parameters. There is already 1 positional parameter, canvas, used in the sample `make_creature` function. You will add to this:

* <span class="hw">ALREADY DONE FOR YOU</span>  A positional (required) parameter, `canvas`, which will be a reference to your canvas object from main.py.
* A positional (required) parameter, `center`, specifying the x-y position of the center of your creature (should be a tuple).
* A keyword (optional) parameter, `primary_color` specifying the primary color of the creature. In the case of the bear, this is the face color. Remember, optional parameters require default values.
* A keyword (optional) parameter, `secondary_color` specifying the secondary color of the creature. In the case of the bear, this is the ear color.
* A keyword (optional) parameter, `size`, specifying the size of the creature.

When you're done, please add at least three calls to the `make_creature` function in your `main.py` file, using different arguments. For instance, after completing the assignment, I used my make_creature function in the following way to produce the drawing below (feel free to use whatever arguments you want for your positional / keyword parameters):

```python
# with a function, you can make slightly different versions of your design, 
# thereby reusing the same code over and over again

make_creature(canvas, (92, 115), size=85, primary_color='#5e6976', secondary_color='#1b324d')
make_creature(canvas, (487, 110), size=101, primary_color='#bfdc65', secondary_color='#abb880')
make_creature(canvas, (454, 423), size=141, primary_color='#aebb83', secondary_color='#227876')
make_creature(canvas, (333, 227), size=99, primary_color='#94ba77', secondary_color='#3f5364')
make_creature(canvas, (117, 314), size=91, primary_color='#648d8e', secondary_color='#afc272')
make_creature(canvas, (199, 469), size=122, primary_color='#3f5364', secondary_color='#bfdc65')

# helper code for making a grid
make_grid(canvas, screen_width, screen_height)
```

<img class="medium frame center" src="/fall2020/assets/images/hw03/creatures.png" />


## What to Submit
Before you submit, please do test your make creature function by invoking the function calls above. If your function is working correctly, all of the input parameters will be honored (i.e. the creature will be drawn at the correct position at (roughly) the specified size, with the specified colors).

When you're done, please create a zip file that includes the following files:

1. A photo / scan of your sketches (PDF or JPG)
1. Your helpers.py file
1. Your creature.py file
1. Your main.py file
