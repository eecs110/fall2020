---
layout: assignment
title: Covid-19 Simulation (Optional)
abbreviation: EC1
type: extra credit
due_date: 2020-05-31
ordering: 1
draft: 1
points: 5
---
<a class="nu-button" href="/fall2020/course-files/homework/ec01.zip" target="_blank">
    Extra Credit Starter Files <i class="fas fa-download"></i>
</a> 

> **Important**: This assignment is **OPTIONAL**, and can be completed for 5 points extra credit.

## Covid-19: A Real-World Learning Opportunity for Programming
<img class="medium frame" src="/fall2020/assets/images/ec01/simulation.png" />

Given the Covid-19 pandemic, in this activity, Peter Zhong, one of our peer mentors, has created an extra credit (optional) lab that walks you through how a data scientist might model the progression of diseases with the aid of computer technologies such as Python. In fact, an effective (though somewhat simplified) model can be built using only CS 110 concepts to simulate the different parameters governing a real-world outbreak. 

The computer can simulate the spread of disease by modeling people as particles in random motion. Of course, this model is by no mean sophisticated sufficiently for real-world applications but should suffice for this purpose. The disease can spread to people at some distance to it, at some probability. The probability and distance jointly model how the disease spreads and the precaution people can take to minimise exposure(washing hands for instance). After a period of time, a person is removed. This could be interpreted in several ways: the person could have recovered, been isolated or died, removing them from the equation completely.

### Basic Programming Concepts You'll Need
* Append to a list and use a list to keep track of people
* While loops and for loops to process the list of people and make appropriate modifications
* Nested loops
* If statements 
* Draw, change colour and move Tkinker objects
* Tkinker tags

### Takeaways
With just 100 lines, you can simulate how how herd immunity, social distancing, and taking precautions affect the spread of disease.

## Your Task
1. Download the starter files
1. Install pillow (if you haven't already): `pip3 install pillow`
1. Watch Peter's <a href="https://northwestern.zoom.us/rec/play/65Mofr2orWo3HNTD4gSDVPd8W43uKKmshylM-KUKyR7hU3ELNVCuNecRZ-GFRYpMqTlnAdxJVO4hT5tl?startTime=1589338064000" target="_blank">video walkthrough</a> and code along
1. Submit a working version of the simulation, starting from the `starter.py` file
1. Write 1-2 paragraphs explaining how the code works in your own words
1. Submit your working code via a zip file

