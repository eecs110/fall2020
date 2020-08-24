---
layout: assignment-two-column
title: Animations & Landscapes
abbreviation: HW4
type: homework
files: course-files/assignments/hw05.zip
due_date: 2020-10-20
points: 8
draft: 1
---


<a class="nu-button" href="/fall2020/course-files/homework/hw04.zip" target="_blank">
    Homework Starter Files <i class="fas fa-download"></i>
</a> 

One of our peer mentors, Katherine, has also created a <a href="https://www.youtube.com/watch?v=RftT-A5vzH8&feature=youtu.be" target="_blank">get started video</a> to get you oriented with the assignment.

{: .blockquote-no-margin}
> **LEARNING OBJECTIVES:** 
> 1. Practice working with loops
> 1. Practice working with if statements
> 1. Practice working with the random module

## Part 1: Landscapes
<img class="large frame" src="/fall2020/assets/images/hw04/bubbles.png" /> 
<img class="large frame" src="/fall2020/assets/images/hw04/stars.png" /> 

In `landscapes.py`, replace the code on lines 23-32 (which is repetitive) with a loop (any kind of loop you want) that makes 1,000 stars that fill the entire canvas. Hints:

1. Use a loop
1. Use the random module, and in particular the random.uniform function to give each star (or bubble if you choose) a random (x, y) position (given the dimensions of the screen) and a random width (so that it renders stars of different sizes).

### Optional enhancements
1. Draw a constellation (Orion's Belt, Big Dipper, etc.)
1. Make your stars twinkle
1. Animate your bubbles

## Part 2: Animation
<div>
    <p>Please open the cars.py file and make the following changes:</p>
    <img class="cars" src="/fall2020/assets/images/hw04/cars.gif" /> 
    <ol>
        <li>Animate the car so that it moves across the screen.</li>
        <li>If the car gets to the end of the screen, it should seamlessly be moved to the beginning of the screen.</li>
        <li>Create a second car using the helpers.make_car function. Be sure to give your new car a unique tag.</li>
        <li>Make the second car move in the opposite direction, and also loop back around when it gets to the end of the screen (see the animated gif).</li>
    </ol>
</div>


### Optional enhancements
The more you practice, the better you'll get!

1. Make the cars accelerate over time (start off slow and gradually move faster)
1. Add your creature to your animation:
    * Inside `helpers.py`:
      * Add your `make_creature` function definition (adapt from Homework 3). 
      * Modify your `make_creature` function so that each constituent shape of your creature gets assigned a tag (study the `make_car` function and do the same thing).
    * In `cars.py`: animate your creature
1. Use loops and the random module to make many moving cars.


## What to Submit
When you’re done with the assignment, please submit a zip file called `hw04.zip` that contains the files below named exactly as they appear:
1. helpers.py
2. cars.py
3. landscape.py

> **IMPORTANT**: YOU MUST TURN IN THE FILES — BOTH THE  ZIP FILE AND THE PYTHON FILES — NAMED EXACTLY AS SPECIFIED ABOVE. OTHERWISE, OUR GRADING SCRIPTS WILL NOT WORK.


