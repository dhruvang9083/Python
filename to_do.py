import sys
from datetime import datetime
present = datetime.now()
present_year = present.year
present_month = present.month
present_day = present.day
present_hour = present.hour 
present_min = present.minute

current_time = datetime(present_year,present_month,present_day,present_hour,present_min)

task_list = []
task = []

number_of_tasks = input("Enter num of tasks")
i = 0
while(i<int(number_of_tasks)):
    task=[]
    task_name = input("Enter task name")
    task.append(task_name) # task name
    task_year = input("Enter task year")
    task.append(task_year) # task year
    task_month = input("Enter task month")
    task.append(task_month) # task month
    task_day = input("Enter task date")
    task.append(task_day) # task date
    task_hour = input("Enter task hour")
    task.append(task_hour) # task hour
    task_minute = input("Enter task min")
    task.append(task_minute) # task min
    i+=1
    task_list.append(task)

print(task_list)
for x in range(0,len(number_of_tasks)):        
    task = task_list[x]
    print(number_of_tasks[x])
    task_name = task[0]
    task_year = task[1]
    task_month = task[2]
    task_date = task[3]
    task_hour = task[4]
    task_min = task[5]

    task_datetime = datetime(int(task_year), int(task_month), int(task_date), int(task_hour), int(task_minute))

    if(task_datetime<current_time):
        print("past due "+task_name)
    if(task_datetime>current_time):
        print("pending "+task_name)
    if(task_datetime==current_time):
        print("remind" + task_name)    
