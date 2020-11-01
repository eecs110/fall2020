---
layout: assignment-two-column
title: Tic Tac Toe
abbreviation: HW5
type: homework
files: course-files/assignments/hw05.zip
due_date: 2020-11-13
points: 8
draft: 0
---
<style>
    .bash-small .highlighter-rouge {
        width: 300px;
        margin: auto;
        margin-top: 10px;
    }
</style>

<a class="nu-button" href="/fall2020/course-files/homework/hw05.zip" target="_blank">
    Homework Starter Files <i class="fas fa-download"></i>
</a> 


> **LEARNING OBJECTIVES:** 
> 1. Practice working with loops
> 1. Practice working with sequences
> 1. Practice with logic
> 1. Practice writing more complex programs

In this assignment, you will be making a game of tic tac toe, where a player will be playing the computer (see video below). 
<iframe src="https://northwestern.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=269492eb-30e6-4a0f-ba26-ac660037a06f&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" width="620" height="405" style="padding: 0px; border: 1px solid #464646;" frameborder="0" allowfullscreen="" allow="autoplay"></iframe>


<!-- <iframe src="https://northwestern.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=269492eb-30e6-4a0f-ba26-ac660037a06f&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe> -->


## Your Tasks
Please write a program that accomplishes the following tasks:

{:.bash-small}
1. Ask the user whether they want to be x or o (and ensure your program honors their choice).
1. Ask the user if they want to go first (and ensure your program honors their choice)
Prompt the user for their move (they’ll enter a number from 1-9), which corresponds to where they want to go (as displayed below):
```bash
             7 | 8 | 9 
            ———————————
             4 | 5 | 6 
            ——————————— 
             1 | 2 | 3 
```

   * If the user does not enter a number from 1-9, tell them their entry was invalid and that they should try again (use try/except as well as if/else).
   * If the user enters a valid number that is not empty, tell them that slot is already taken.
1. If it’s the computer’s turn, have the computer randomly select a square, given the available choices (using the random module).
1. After each move, be sure to redraw the game board
1. If there is a win / loss / tie, print an appropriate message and terminate the game


## Caveats
There are many solutions on the Internet for this assignment. DO NOT USE THEM. We know what they are, and can tell if you copied all or parts of them. We want you to invent your own strategy, given what you have learned. Like all things, you will get out of this assignment what you put into it.

## Extra Credit Options (up to 2 points total)
We highly recommend that you pursue these optional enhancements, to encourage you to think about one way (of many) that ‘artificial intelligence’ might work:
1. Make your computer ‘smart’ so that the computer always selects the optimal move. To do this, consider how the computer could:
  * (1 point) Always block the user from winning (when possible)
  * (1 point) If the computer is about to win, make sure it selects the correct square!
  * (1 points): Other enhancements (see strategy discussion): https://www.wikihow.com/Win-at-Tic-Tac-Toe 
2. (1 point) Draw a line through the winning pattern on the game board.

## Checklist Before You Submit
Before you submit, make sure you’ve tested that your program does the following:

{:.checkbox-list}
* Allows the user to select whether they want to be x or o
* Allows the user to indicate whether or not they want to go first
* Program honors the user’s selection (1-9) and places the symbol correctly 
* If the user enters something other than 1-9, the program tells the user what they did wrong and re-prompts them 
   * Note: consider using try/catch + continue (as we did in the beginning of Lecture 13)
* Computer move does not overwrite a slot that is already taken
* User’s move does not overwrite a slot that is already taken
* If the user and / or computer wins, the program ends and tells the user which player won
* If there’s a tie, the program ends and displays a “tie” message

