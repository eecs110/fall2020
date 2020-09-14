---
layout: assignment-two-column
title: |
    Installation & Introductory Exercises
abbreviation: HW1
type: homework
due_date: 2020-09-24
ordering: 1
draft: 0
points: 8
---

<style>
    .screenshot {
        width: 100%;
        border: solid 1px #ccc;
        padding: 6px;
        border-radius: 5px;
    }
</style>

## Part 1: Install Python and IDLE

{: .blockquote-no-margin}
> **NOTE:** If you have any issues installing Python or IDLE, contact your assigned peer mentor. You are also welcome to attend any of the course office hours to get help.

We will use the Python 3 programming language and **IDLE**, which is Python's Integrated Development and Learning Environment.

Download the latest version (3.8.2) of python here: <a href="https://www.python.org/downloads/" target="_blank">https://www.python.org/downloads/</a>

After going through the installation process, navigate to the folder on your machine where Python was installed. For me, on a Mac, my IDLE was saved to Applications > Python 3.8 (or you can also search for it). For Windows users, it will likely be in a folder inside of Program Files (which you can also search for).

Inside, the Python 3.8 folder, you'll find a file called **IDLE** - this is the IDLE executable. Double click on that file to run it. You should then see something like:

<img class="screenshot" src="/fall2020/assets/images/hw01/idle1.png" />

I recommend keeping IDLE in your dock (on a Mac) or making a Desktop Shortcut to IDLE (on Windows).

At the **&gt;&gt;&gt;** prompt, you can type any valid python command. For example, type `print("hello world!")` and hit enter. You should see something like this:

<img class="screenshot" src="/fall2020/assets/images/hw01/idle2.png" />


## Part 2: Complete the Programming Exercises
In the section above, you wrote a single line of python at the **&gt;&gt;&gt;** prompt. For instance: 

`print("hello world!")`

However, in this class, you'll be writing larger programs that are stored in files that end with the "**.py**" extension. You will then run all of the code in the file all at once. To try this out, we will practice writing a Python file in this week's homework. Please follow the steps outlined below, and then complete the exercises.

### Step 1: Organize yourself!
File management and organization are an essential part of programming. As such, we suggest the following system:
1. Create a course folder: **cs110**
2. Create a **homework** folder inside of the cs110 folder.
3. Create a **hw01** folder inside of your homework folder.

Sample file structure (there will be course lecture files as well):

```
cs110
    |-- homework
    │   |-- hw01
    │   |-- hw02
    |   ...
    |
    |-- lectures
        |-- lecture_01
        |-- lecture_02
        |-- lecture_03
        ...
```

It may seem trivial, but take some time now to organize yourself. It will save you time in the long run!

### Step 2: Complete the following exercises
Download the [main.py](../course-files/homework/hw01/main.py) starter file and save it in your hw01 folder. To edit **main.py** using IDLE:

1. Right click on the **main.py** file that you just saved in your **hw01 folder** and open it with IDLE. 
2. You should now see some python code. Click anywhere inside that file so that your cursor is now in that window. 
3. Hit F5 (if you're on a MAC with a touchbar, hit the **fn** key and then **F5**). As an alternative to F5, you can also go to the Run menu and select **Run Module**. Your code will then be executed by the Python interpreter.

When you're done, please complete the following 9 exercises by editing the **main.py** file using IDLE. 

#### 1. Print a box like the one below:
```
*******************
*******************
******************* 
******************* 
```

#### 2. Print a box like the one below:
```
*******************
*                 * 
*                 * 
******************* 
```

#### 3. Print a triangle like the one below:
```
*
**
***
****
```

#### 4. Write a program that computes and prints the result of: 
<img src="/fall2020/assets/images/hw01/equation.png" style="width: 100px;"/>

(The answer is roughly 0.1017).

#### 5. User input
Ask the user to enter a number. Convert it to an int, and print out the square of the number, but use the end optional argument to print it out in a full sentence that ends in a period (e.g. “The square of 5 is 25.”).
Sample output is shown below: 

```python
Enter a number: 5 	     # prompts the user for a number (not necessarily 5)
The square of 5 is 25.
```

#### 6. Practice with the "sep" optional parameter
Ask the user to enter a number x. Use the sep optional argument to print out x, 2x, 3x, 4x, and 5x, each separated by three dashes, like below:

```python
Enter a number: 7         # prompts the user for a number (not necessarily 7)
7---14---21---28---35 
```

#### 7. Math Practice
Write a program that asks the user for a weight in kilograms and converts it to pounds. There are 2.2 pounds in a kilogram. 

```python
Enter weight in kg: 5         # prompts the user for a weight in kg
5 kilograms is 11.0 pounds. 
```

#### 8. Calculate Average
Write a program that asks the user to enter three numbers (use three separate input statements). Create variables called total and average that hold the sum and average of the three numbers and print out the values of total and average. 


#### 9. Tip Calculator
Write a tip calculator. Ask the user for the price of the meal and the percent tip they want to leave. Then print both the tip amount and the total bill with the tip included.


## What to Submit
Please submit your main.py file, that includes code that successfully implements the nine exercises listed above (which come from the Heinold book). Before each exercise, use comments (or keep the existing ones) to indicate the number of the exercise that your code corresponds to.
