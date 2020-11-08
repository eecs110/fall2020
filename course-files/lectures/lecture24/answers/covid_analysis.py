# pip3 install bs4
import utilities
from csv import reader


# Step 1: Download all data files from Johns Hopkins GitHub
# Note: this function only downloads a day's COVID-19 file 
#       if it hasn't been downloaded already.
utilities.download_all_data_files()

# Step 2: Analyze all data pertaining to state over time...
state = 'California'
county = 'Monterey'
headers = ['Day', 'State', 'Total', 'Daily Total', 'Direction']
if county:
    file_name = state.lower() + '_' + county.lower() + '.csv'
else:
    file_name = state.lower() + '.csv'
out_file_path = utilities.get_file_path(file_name, subdirectory='files')
out_file = open(out_file_path, 'w')
out_file.write(','.join(headers) + '\n')

# Step 3: initialize grouping and summing variables
data = {}
yesterdays_count = 0
todays_change = 0
yesterdays_change = 0

# Step 4: open each file in the directory and process it:
file_names = utilities.get_files_in_directory('files')
print('Analyzing', len(file_names), 'files (Jan - Nov, 2020) and extracting all data pertaining to', state, end='.\n')
for file_name in file_names:
    file_path = utilities.get_file_path(file_name, subdirectory='files')
    f = open(file_path, 'r', encoding='utf8', errors='ignore')
    file_data = list(reader(f))
    try:
        headers = file_data[0]
        idx = headers.index('Confirmed')
    except:
        print('File does not conform to the format:', file_path)
        continue

    count = 0
    for row in file_data:
        if row[2] == state and (row[1] == county or county is None):
            try:
                count += int(row[idx])
            except:
                print('Error:', row[idx])

    # calculate today's change based on yesterday's count:
    todays_change = count - yesterdays_count
    
    if yesterdays_change < todays_change:
        symbol = '+'    # increased
    elif yesterdays_change > todays_change:
        symbol = '-'    # decreased
    else:
        symbol = ''     # stayed the same

    day = file_name.split('.')[0]
    row = [
        day, state, str(count), str(todays_change), symbol
    ]
    out_file.write(','.join(row) + '\n')
    
    # update counters and aggregators
    data[day] = todays_change
    yesterdays_count = count
    yesterdays_change = todays_change

out_file.close()
chart_title = 'COVID-19 Data: ' + state
if county:
    chart_title += ' (' + county + ' County)'
utilities.make_bar_chart(data, title=chart_title)