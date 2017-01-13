# -*- coding: utf-8 -*-
import sys
import math
from datetime import date, timedelta, datetime

###
#counting day of week
def what_day(day, month, year):
  days = ["воскресенье", "понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
  a = (14 - month) / 12
  y = year - a
  m = month + 12 * a - 2
  res = (7000 + (day + y + y / 4 - y / 100 + y / 400 + (31 + m) / 12)) % 7
  return days[res] 

def days_in_month(month, year):
  out = 28 + ((month + math.floor(month / 8)) % 2) + 2 % month + math.floor((1 + (1 - (year % 4 + 2) % (year % 4 + 1)) * ((year % 100 + 2) % (year % 100 + 1)) + (1 - (year % 400 + 2) % (year % 400 + 1))) / month) + math.floor(1/month) - math.floor(((1 - (year % 4 + 2) % (year % 4 + 1)) * ((year % 100 + 2) % (year % 100 + 1)) + (1 - (year % 400 + 2) % (year % 400 + 1)))/month)
  return int(out)

def sort_by_ordinal(input_date):
  return input_date.toordinal()

def dates_days(year):
  days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
  dates_dict = {}
  day = date(year, 1, 1)
  while day != date(year+1, 2, 1):
    dates_dict[day] = days[day.weekday()]
    day += timedelta(days = 1)
#  for month in range(1, 13):
#    for day in range(1, days_in_month(month, year)+1):
#      if len(day) < 2:       
#        date_full = "0" + str(day) + "."
#      else:
#        date_full = str(day) + "."
#      if len(month) < 2:
#        date_full += "0" + str(month) + "."
#      else:
#        date_full += str(month) + "."
#        + "." + str(month) + "." + str(year)
#      dates_dict[date_full] = what_day(day, month, year) 
  return dates_dict

def print_diary(year, filename):
  holidays_list = []
  holidays_file = open("holidays.txt", 'rU')
  for line in holidays_file:
    holidays_list.append(datetime.strptime(line.strip(), "%d.%m.%Y").date())
  holidays_file.close()
  file = open(filename, 'w')
  dates_dict = dates_days(year)
  for day in sorted(dates_dict, key=sort_by_ordinal):
    message = ""
    if dates_dict[day] in ["суббота", "воскресенье"] or day in holidays_list:
      message = "Выходной день"
    else:
      message = "<li>Приём посетителей 13:00-17:00</li>"
    file.write(day.strftime("%d.%m.%Y") + "\t" + dates_dict[day] +"\t" + message + "\n")
  file.close()
  pass

def main():
  if len(sys.argv) != 2:
    print 'usage: ./diary.py year' 
    sys.exit(1)

  year = int(sys.argv[1])
  filename = 'diary.txt'
  f = open(filename, 'w')
  f.close()
  print_diary(year, filename)
  pass

if __name__ == '__main__':
  main()