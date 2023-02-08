#Python Dates
#Import the datetime module and display the current date
import datetime

x = datetime.datetime.now()
print(x)


#Date Output
#Return the year and name of weekday
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


#Creating Date Objects
#Create a date object
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)


#The strftime() Method
#Display the name of the month
import datetime

x = datetime.datetime(2018, 6, 1)

print("Display the name of the month",x.strftime("%B"))


#different formate
print(x.strftime("%a")) # Weekday, short version----> wed
print(x.strftime("%A")) # Weekday, full version--->Wednesday
print(x.strftime("%w")) # Weekday as a number 0-6, 0 is Sunday--->3
print(x.strftime("%d")) # Day of month 01-31--->31 
print(x.strftime("%b")) # Month name, short version--->Dec	
print(x.strftime("%B")) # Month name, full version--->December
print(x.strftime("%m")) # Month as a number 01-12--->12	
print(x.strftime("%y")) # Year, short version, without century--->18
print(x.strftime("%Y")) # Year, full version--->2018
print(x.strftime("%H")) # Hour 00-23---->17
print(x.strftime("%I")) # Hour 00-12---->05
print(x.strftime("%p")) # AM/PM---->PM	
print(x.strftime("%M")) # Minute 00-59---->	41
print(x.strftime("%S")) # Second 00-59---->	08
print(x.strftime("%f")) # Microsecond 000000-999999---->548513		
print(x.strftime("%z")) # UTC offset---->	+0100
print(x.strftime("%Z")) # Timezone---->	CST
print(x.strftime("%j")) # Day number of year 001-366---->	365
print(x.strftime("%U")) # Week number of year, Sunday as the first day of week, 00-53---->	52		
print(x.strftime("%W")) # Week number of year, Monday as the first day of week, 00-53---->	52
print(x.strftime("%c")) # Local version of date and time---->	Mon Dec 31 17:41:00 2018	
print(x.strftime("%C")) # Century---->	20
print(x.strftime("%x")) # Local version of date---->12/31/18
print(x.strftime("%X")) # Local version of time---->17:41:00
print(x.strftime("%%")) # A % character---->%
print(x.strftime("%G")) # ISO 8601 year---->2018	
print(x.strftime("%u")) # ISO 8601 weekday (1-7)---->1
print(x.strftime("%V")) # ISO 8601 weeknumber (01-53)---->01