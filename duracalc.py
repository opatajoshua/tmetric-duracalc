import csv
from locale import currency
import sys

if(len(sys.argv) <1):
  print('csv file path required a argument')
  quit()
print('===dd', sys.argv)

# configurations
file_path = 'detailed_report.csv'
entry_col_idx = 2
dur_col_idx = 10
amount_per_hour =15
currency ="$"


counter =0

def duration_to_hour(dur_string):
  [hr, min, sec] = dur_string.split(':')
  return int(hr)+(int(min)/60)+(int(sec)/60/60)

tasks_map={}

with open(file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
      if(counter>0):
        task_name = row[entry_col_idx]
        duration_str =row[dur_col_idx]
        hr_dur = duration_to_hour(duration_str)
        tasks_map[task_name] = tasks_map[task_name]+hr_dur if task_name in tasks_map else hr_dur
        # print(task_name+":", duration_str, hr_dur)
      counter+=1

task_list =[]
total = 0
print('\ntask list\n===================')
for key, value in tasks_map.items():
  total+=value
  task_list.append([key, value, value*amount_per_hour])
  print(key,":", value, ":", currency+str(value*amount_per_hour))

print("===================")
print("\ntotal hours: ", total, )
print("\ntotal amount: ", total*amount_per_hour, "\n\n")