# put your python code here

hour = int(input())
minutes = int(input())
seconds = int(input())

hour_1 = int(input())
minute_1 = int(input())
seconds_1 = int(input())

time = hour * 3600 + minutes * 60 + seconds
time_1 = hour_1 * 3600 + minute_1 * 60 + seconds_1

print(time_1 - time)


