'''You are given the current time R in the HH:MM:SS format. You are also given N more time values in an array P, where every element P[i] is less than or equal to R. Write a program to calculate the time difference between P[i] and R and print one of the following messages accordingly: • If the time difference is zero, print now. • If the time difference is in seconds but less than a minute, print X seconds ago. • If the time difference is in minutes but less than an hour, print X minutes ago. Ignore the seconds part of the difference. • If the time difference is in hours, print X hours ago. Ignore the minutes and seconds part of the difference. • If the value of X is 1, print the word second instead of seconds, hour instead of hours and minute instead of minutes.

Input Format

• First line: R (In the HH:MM:SS format) • Second line: N • Next N lines: P[i] (In the HH:MM:SS format, where 0≤i

Constraints

0≤HH≤23 0≤MM≤59 0≤SS≤59 1≤N≤1000

Output Format

For each P[i], print the message indicating the time difference.'''


import datetime


time = input() 
time_inputs = int(input())   
time_list = []
for i in range(time_inputs):
    different_times = input()
    time_list.append(different_times)

t1 = datetime.datetime(
    2022, 12, 12, int(timr[0:2]), int(time[3:5]), int(time[6:8]))

for i in time_list:
    t2 = datetime.datetime(
        2022, 12, 12, int(i[0:2]), int(i[3:5]), int(i[6:8]))

    delta = t1 - t2
    str_delta = str(delta)

    t_hours, t_minutes, t_seconds = 0, 0, 0

    if len(str_delta) == 7:
        t_hours = int(str_delta[0])
        t_minutes = int(str_delta[2:4])
        t_seconds = int(str_delta[5:7])

    if len(str_delta) == 8:
        t_hours = int(str_delta[0:2])
        t_minutes = int(str_delta[3:5])
        t_seconds = int(str_delta[6:8])

    if t_hours >= 1:
        if t_hours == 1:
            print(f'{t_hours} hour ago')
        else:
            print(f'{t_hours} hours ago')

    if t_hours == 0 and t_minutes >= 1:
        if t_minutes == 1:
            print(f'{t_minutes} minute ago')
        else:
            print(f'{t_minutes} minutes ago')

    if t_hours == 0 and t_minutes == 0 and t_seconds >= 0:
        if t_seconds == 1:
            print(f'{t_seconds} second ago')
        if t_seconds == 0:
            print(f'now')
        else:
            print(f'{t_seconds} seconds ago')