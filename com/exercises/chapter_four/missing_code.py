# 4.5 (Fill in the Missing Code?) Replace the ***s in the seconds_since_midnight function
# so that it returns the number of seconds since midnight. The function should receive
# three integers representing the current time of day. Assume that the hour is a value from
# 0 (midnight) through 23 (11 PM) and that the minute and second are values from 0 to 59.
# Test your function with actual times. For example, if you call the function for 1:30:45 PM
# by passing 13, 30 and 45, the function should return 48645.

def seconds_since_midnight(hour, minute, seconds):
    hour_in_seconds = 0
    if hour < 12:
        answer = input(print("AM or PM?"))
        if answer.casefold() == "am":
            hour_in_seconds = 3600 * hour
        elif answer.casefold() == "pm":
            hour_in_seconds = 3600 * (hour + 12)
    else:
        hour_in_seconds = 3600 * hour

    minute_in_seconds = 60 * minute
    return hour_in_seconds + minute_in_seconds + seconds


print(seconds_since_midnight(2, 24, 45))
