'''
------------
Installation
------------
You need to install the "Beautiful Soup" dependency
in order for this exercise to work:

      pip3 install bs4

------------
Instructions
------------
1. Download all of the COVID-19 Data Files that Johns Hopkins
   makes available here...
   
   https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports

   ...into the "files" directory using the following functions:
      a) utilities.get_covid_file_links (extracts the addresses of each data file)
      b) utilities.download_remote_file (saves a remote file to disk)

2. Once downloaded...
      a) Prompt the user for a state
      b) Iterate through each data file in the "files" directory,
         using the utilities.get_files_in_directory function, in
         order to calculate the daily change in covid cases.
      c) print the data and the daily change in cases to the screen.
      d) create an output CSV file to store your results

3. Finally, use tkinter to make a bar chart of cases by state
   by modifying the utilities.make_bar_chart function.
'''

import utilities


# Part 1: download the first covid-19 data file and 
#         save it to the "files" directory:
covid_report_links = utilities.get_covid_file_links()
print(covid_report_links)

# downloading one file...
local_path = utilities.get_file_path('test_file.csv', subdirectory='files')
utilities.download_remote_file(covid_report_links[0], local_path)

# Part 2:  Open all files in the 'files' directory and analyze them:
files_directory = utilities.get_file_path('files')
local_file_paths = utilities.get_files_in_directory(files_directory)
print(local_file_paths)


# Part 3: after you've analyzed the data, make a bar chart:
utilities.make_bar_chart()