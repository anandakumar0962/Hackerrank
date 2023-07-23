'''You are given the current time R in the HH:MM:SS format. You are also given N more time values in an array P, where every element P[i] is less than or equal to R. Write a program to calculate the time difference between P[i] and R and print one of the following messages accordingly: • If the time difference is zero, print now. • If the time difference is in seconds but less than a minute, print X seconds ago. • If the time difference is in minutes but less than an hour, print X minutes ago. Ignore the seconds part of the difference. • If the time difference is in hours, print X hours ago. Ignore the minutes and seconds part of the difference. • If the value of X is 1, print the word second instead of seconds, hour instead of hours and minute instead of minutes.

Input Format

• First line: R (In the HH:MM:SS format) • Second line: N • Next N lines: P[i] (In the HH:MM:SS format, where 0≤i

Constraints

0≤HH≤23 0≤MM≤59 0≤SS≤59 1≤N≤1000

Output Format

For each P[i], print the message indicating the time difference.

Sample Input 0

23:05:38
7
23:05:38
23:05:02
23:04:59
23:04:31
12:36:07
08:59:01
00:00:00
Sample Output 0

now
36 seconds ago
39 seconds ago
1 minute ago
10 hours ago
14 hours ago
23 hours ago '''

from datetime import datetime, timedelta
R = input()
N = int(input())
for _ in range(N):
    p = input()
    t1 = datetime.strptime(R, "%H:%M:%S")
    t2 = datetime.strptime(p, "%H:%M:%S")
    
    diff = t1 - t2
    hours = diff.seconds // 3600
    minutes = (diff.seconds //60) % 60
    seconds = diff.seconds % 60
    
    if hours == 1:
        print("1 hour ago")
        continue
    elif hours != 0:
        print("%s hours ago" %hours)
        continue
    elif minutes == 1:
        print("1 minute ago")
        continue
    elif minutes != 0:
        print("%s minutes ago"%minutes)
        continue
    elif seconds == 1:
        print("1 second ago")
        continue
    elif seconds != 0:
        print("%s seconds ago" %seconds)
        continue
    else:
        print("now")
