import ast

def add_time(start, duration, *starting_day):

    def getDay(num, c, days):
        for i in c:
            what_day = i
        what_day = what_day.lower().capitalize()

        if num < 1:
            num = days.get(what_day)

        elif num > 0 and num <= 7:

            if (num + days.get(what_day)) >= 7:
                total = 7 - days.get(what_day)
                num = num - total
            else:
                num = num + days.get(what_day)

        elif num > 7:
            while (num - 7) > 1:
                num -= 7
            total = 7 - days.get(what_day)
            num = num - total

        for key, value in days.items():
            if value == num:
                return key

    day = 0
    days = {'Sunday': 1, 'Monday': 2, 'Tuesday': 3, 'Wednesday': 4, 'Thursday': 5, 'Friday': 6, 'Saturday': 7}
    time_hour = 0
    time_min = 0
    time_format = ''
    c = ''
    isNextDay = False
    start_time = start.split(':')
    start_hour = start_time[0]
    min_format = start_time[1].split()
    start_min = min_format[0]
    start_format = min_format[1]

    duration_time = duration.split(':')
    duration_hour = duration_time[0]
    duration_min = duration_time[1]

    result_hour = int(start_hour) + int(duration_hour)
    result_min = int(start_min) + int(duration_min)

    if result_min >= 60:
        while result_min - 60 > 0:
            result_min -= 60
            result_hour += 1
    if result_min < 60:
        time_min = result_min
    if result_hour >= 24:
        while result_hour - 24 >= 0:
            result_hour -= 24
            day += 1
    if result_hour > 12:
        result_hour -= 12
        if start_format == 'PM':
            start_format = 'AM'
            day += 1
            if day == 1:
                isNextDay = True
        else:
            start_format = 'PM'
    if result_hour < 13:
      time_hour = result_hour
      if result_hour == 12:
        if start_format == 'PM':
            start_format = 'AM'
            day += 1
        else:
            start_format = 'PM'
      time_format = start_format
      if day == 1:
          isNextDay = True

    if starting_day:
        c = getDay(day, starting_day, days)+" "
    if len(str(time_hour)) == 1 and len(str(time_min)) == 1:
      if isNextDay:
        new_time = f'0{time_hour}:0{time_min} {time_format} {c}(next day)'
      elif day > 1:
          new_time = f'0{time_hour}:0{time_min} {time_format} {c}({day} days later)'
      else:
        new_time = f'0{time_hour}:0{time_min} {c}{time_format}'
    elif len(str(time_hour)) == 2 and len(str(time_min)) == 1:
      if isNextDay:
        new_time = f'{time_hour}:0{time_min} {time_format} {c}(next day)'
      elif day > 1:
          new_time = f'{time_hour}:0{time_min} {time_format} {c}({day} days later)'
      else:
        new_time = f'{time_hour}:0{time_min} {time_format} {c}'
    elif len(str(time_hour)) == 1 and len(str(time_min)) == 2:
      if isNextDay:
        new_time = f'0{time_hour}:{time_min} {time_format} {c}(next day)'
      elif day > 1:
          new_time = f'0{time_hour}:{time_min} {time_format} {c}({day} days later)'
      else:
        new_time = f'0{time_hour}:{time_min} {time_format} {c}'
    else:
        new_time = f'{time_hour}:{time_min} {time_format} {c}'

    return new_time

print(add_time("3:30 PM", "2:12"))
print(add_time("11:55 AM", "3:12"))
print(add_time("9:15 PM", "5:30"))
print(add_time("11:40 AM", "0:25"))
print(add_time("2:59 AM", "24:00"))
print(add_time("8:16 PM", "466:02"))
print(add_time("11:59 PM", "24:05"))
print(add_time("5:01 AM", "0:00"))
print(add_time("3:30 PM", "2:12", "Monday"))
print(add_time("2:59 AM", "24:00", "saturDay"))
print(add_time("11:59 PM", "24:05", "Wednesday"))