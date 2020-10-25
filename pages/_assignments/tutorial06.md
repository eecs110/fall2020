---
layout: assignment-two-column
title: Event Handlers
type: tutorial
abbreviation: Tutorial 6
draft: 0
num: 4
points: 3
due_date: 2020-10-28
    
---

<a class="nu-button" href="/fall2020/course-files/tutorials/tutorial06.zip" target="_blank">
    Tutorial Starter Files <i class="fas fa-download"></i>
</a> 

The goal of this tutorial is to get you more comfortable with event handlers, and in particular the click, drag, and keyboard event handlers. Please complete the following exercises:

## 1. Add a creature when you click on the canvas
Open `01_click_to_add_creature.py` and complete the following tasks:
1. modify the `add_new_creature` function so that it adds a new creature wherever the user clicks. Make the size and color of the creature random.
2. When you're done, add the following line to your program right below your MOUSE_CLICK event handler:<br><br>**`canvas.bind(MOUSE_DRAG, add_new_creature)`** <br><br>Now run your program again, and notice that your `add_new_creature` function is invoked when you either click or drag.
3. Finally, replace the smiley face `make_creature` function with *your creature. To do this, copy your creature function (and any relevant helper functions) into `creature.py` and then make any necessary modifications to the `add_new_creature` function.


## 2. Move your creature when you press the i, j, k, and m keys
Open `02_move_creature_with_keyboard.py` and complete the following tasks:
1. When the user presses the i-key, move the creature **up** 10 pixels.
2. When the user presses the j-key, move the creature to the **left** 10 pixels. 
3. When the user presses the k-key, move the creature to the **right** 10 pixels. 
4. When the user presses the m-key, move the creature **down** 10 pixels. 

{:.blockquote-no-margin}
> **NOTES:**
> 1. In order for your Canvas to listen for keyboard events, you must invoke the **`canvas.focus_set()`** method after you invoke `canvas.pack()` (at the top of your program). Without **`canvas.focus_set()`**, your keyboard events will not fire. 
> 2. Also, the keyboard bindings for a Mac and a Windows are different. So in order for your program to work, you'll need to make sure that you learn what the correct keyboard codes are for your operating system. Do do this, simply run your program, press a key, and see which code prints to the screen. 

## 3. Select which creature to move with the keyboard
In the third exercise, you are going to use a global variable to track which creature your keyboard will control. To do this, you will combine the use of the click event handler and the keyboard event handlers.

Open `03_select_which_creature_to_move_with_keyboard.py` and do the following:

1. Replace your `move_creature` function with the solution you came up with in exercise #2.
2. Create a global variable called **`active_tag`** and initialize it to 'creature_1'.
3. Update your `move_creature` functionality so that instead of always moving 'creature_1', you reference the **`active_tag`** variable instead.
4. Modify the **`select_creature`** function so that it sets the **`active_tag`** variable based on creature on which the user clicks. Hint: use the **`global`** keyword.
5. Test your code by making sure that when you click on a different creature, the keyboard moves the correct one.

## What to turn in (same deal as always)
Please turn in your completed tutorial exercise(s) ON CANVAS by Wednesday night at midnight. To do this, first zip your entire `tutorial06` folder (with your edited files inside), and then upload your zip file to Canvas. Please ensure that your zip file includes **YOUR CODE**.  