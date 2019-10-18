time_in_sec = int(input("Enter a number in the range of 1 to 86,400: "))


if time_in_sec >= 1 & time_in_sec <= 86400:
    hours = time_in_sec // 3600
    diff = hours * 3600
    time_in_sec -= diff

    minute = time_in_sec // 60
    diff = minute * 60
    
    seconds = time_in_sec - diff
    print("Current time is: ", hours, "hours", \
         minute, "minutes", seconds, "seconds")
else:
    print("Invalid input")
    
    
