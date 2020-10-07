---
layout: lecture-two-column
title: |
    Quiz Review: Expressions
type: lecture
draft: 0
num: 10
description:
  - Operators & Data Types
  - Functions
  - Variables & Variable Scope
  - Lists & Tuples
  - Modules
due_date: 2020-10-07

---

Today, we're going to field questions from the class and go over them. We're also going to make sure we understand how to do these two problems:

## Exercise 1
```python
# Given the following two lists...
first_names = ['Kim', 'Brenda', 'Karlo']
last_names = ['Jones', 'Jauregui', 'Imper']

# Write a program that combines the two lists by creating a third list,
# where each entry is the full name of the person. You can assume that 
# first names and last names of the same person are located in the same slot of
# their respective lists (e.g. Kim Jones, Brenda Jauregui, Karlo Imper).
```

## Exercise 2
Write a function that shifts a list of three coordinate pairs by some horizontal amount and some vertical amount. The function should return the new/updated list.

```python

# here is how I would call your function...
#
# print(shift_coordinates([(20, 20), (30, 30), (40, 40)], x_units=100, y_units=200))
# print(shift_coordinates([(40, 40), (100, 100), (200, 200)], x_units=50, y_units=100))
# print(shift_coordinates([(40, 40), (100, 100), (200, 200)]))

# ...and here's what would print to the screen...
#
# [(120, 20), (130, 30), (140, 40)]
# [(90, 140), (150, 200), (250, 100)]
# [(40, 40), (100, 100), (200, 200)]
```
