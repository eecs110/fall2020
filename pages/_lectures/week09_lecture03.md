---
layout: module
title: Crawling & Analyzing Files
description:
  - Understanding how a web crawler works
type: lecture
draft: 0
num: 24
due_date: 2020-11-13
exercise_url: "lecture24.zip"
videos:
    - url: "https://northwestern.zoom.us/rec/share/8yCWTShFAVuZsEtMIyX9rQpQo_sTnFcLb1-r_ZggRWWpaMLqNDyjvs_d2iCdM2El.J2kyuNR6-86WTo1r?startTime=1605284299000"
      title: "Live Lecture Exercise"
      duration: "56:12"
      live: 1

---

In the next two lectures, we will be doing a COVID-19 data analysis, pulling from a data repository that is organized and maintained by Johns Hopkins university:

<a href="https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports" target="_blank">https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports</a>

## Dependencies
Before you begin, you will need to install the "Beautiful Soup" dependency on the command line:

`pip3 install bs4
`

## Instructions
Open `covid_analysis.py` and `utilities.py` and take a look at them. Then complete the following tasks:

### 1. Download all of the COVID-19 Data Files
Write some code that downloads and saves all of COVID-19 data files (for each day since the outbreak was tracked, worldwide) to your `files` directory.

I have made two functions in the utilities.py module to help you:
1. **utilities.get_covid_file_links()**, which extracts the web addresses of each data file.
2. **utilities.download_remote_file()**, which will save a remote file to your file system.

### 2. Analyze the Data Files
After all of the data files have been downloaded, you are going to:
1. Prompt the user for a state they're interested in analyzing
2. Iterate through each data file in the "files" directory in order to calculate the daily change in covid cases. Use the **utilities.get_files_in_directory()** function to help you. Within this iteration block, you will:
    * Print the date and the daily change in cases to the screen (for every day for which you have data).
    * Create an output CSV file to store your results

### 3. Make a Data Visualization
Finally, use tkinter to make a bar chart of cases by state by modifying the **utilities.make_bar_chart()** function.

