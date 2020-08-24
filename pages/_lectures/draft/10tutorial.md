---
layout: two-column
title: |
    Loops and Conditionals
type: lab
draft: 1
points: 4
num: 3
description:
  - Using if / elif / else
  - Using while loops
due_date: 2020-10-16
    
---

<a class="nu-button" href="/fall2020/course-files/labs/lab03.zip" target="_blank">
    Lab Starter Files <i class="fas fa-download"></i>
</a> 

The goal of this lab is to get you comfortable with if/else statements and while loops. Both of these types of statements are very powerful, so getting comfortable with them is essential (and will help you with [HW4](../assignments/hw4)). If you have a lab earlier in the week, then you have not yet reviewed **while loops**. Here are <a href="https://docs.google.com/presentation/d/1BUOFXuJSwFgolQP_lTR_cDl9LHy3t5AjdfRsiQDF8Cw/edit?usp=sharing" target="_blank">some slides</a> to explain the rules of while loops.

## Part 1: Number Guessing Game
Open the `01_number_game.py` file and write a program for a number guessing game. The game already does the following:

* Picks a number between 1 and 100 using the random module [already done]
* Prompts the user to guess a number between 1 and 100: [already done]

Your job is to finish the game by implementing the following features:
1. If the number is too low, it tells the user the number is too low and that they should guess again
2. If the number is too high, it tells the user the number is too high and that they should guess again
3. If they guess the number correctly:
  * Tell them that they guess correctly
  * Tell them the number of guesses it took to guess correctly
  * Exit the program

### Hints
1. You will need a variable to track the number of guesses
1. You will need a variable to store the user’s guess
1. You will need a while loop that keeps prompting the user for their guess (until they win)
1. You will need some combination of if, elif, and/or else statements to check whether the user’s guess is too low or too high. There are many ways to do this.


## Part 2: Simplify the vertical circles program
1. Open `02_vertical_circles.py` 
2. See if you can use a while loop to recreate this functionality, where there is only one make_circle function call that is repeated within a while loop.

<img class="frame" style="width: 100px;" src="/fall2020/assets/images/lab03/vertical_circles.png" />

### Hints
1. You will need to initialize a counter
2. You will need to make use of the counter to position the y-coordinate of the circle


## Extra Challenges: Drawing with Loops
Practice creating the following shapes using a while loop. The first three shapes are recommended for everyone. The last two (spirograph ones) are optional. If you pursue the latter two, see if you can get implementation ideas here (or using some other source).

<img class="med-lg center frame" src="/fall2020/assets/images/lab03/shapes.png" />

## Hints
1. Q: What do you want to repeat?
  * A: Calling the circle function
2. Q: How long to you want to repeat?
  * A: until all of the circles in the picture are drawn
3. What changes each time?
  * A: Varies (depending on the drawing)


## What to turn in (same deal as always)
As described in the syllabus, there are two ways to earn full participation credit in each lab session:

1. By attending them (synchronously), working through the exercises, and asking questions (as they arise).
2. By turning in the lab exercise(s) ON CANVAS **before** the lab session. Lab exercises will be posted at the beginning of the week (at least 48 hours in advance). 

Whichever option you choose, you will be expected to know the material reviewed in the lab for the exam, and are encouraged to fully complete and submit the lab assignments (though this is not required if you attended the lab).