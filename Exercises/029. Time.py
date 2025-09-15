# exploration of the time module
import time

print(time.time()) # current time in seconds since epoch (1970-01-01 00:00:00 UTC)
print(time.localtime()) # current local time as a struct_time object
print(time.ctime(time.time())) # convert a time in seconds since epoch to a readable string

local_time = time.localtime() # get the current local time as a struct_time object
year = local_time.tm_year # extract the year from the struct_time object
month = local_time.tm_mon # extract the month from the struct_time object
day = local_time.tm_mday # extract the day from the struct_time object
hour = local_time.tm_hour # extract the hour from the struct_time object
minute = local_time.tm_min # extract the minute from the struct_time object
second = local_time.tm_sec # extract the second from the struct_time object

print("Date: {}/{}/{}".format(day, month, year)) # print the date in DD/MM/YYYY format
print("Time: {}:{}:{}".format(hour, minute, second)) # print the time in HH:MM:SS format