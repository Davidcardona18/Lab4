#daid cardona - October 15, 2024

# Fixed typo in the input prompt ("nours" to "hours").
str_time = input("What time is it now?")
str_wait_time = input("What is the number of hours to wait?")

# Fixed the typo in variable names (wai_time to wait_time).
time = int(str_time)
wait_time = int(str_wait_time)

# Fixed the variable reference for wait_time.
time_when_alarm_go_off = time + wait_time

# Print the time when the alarm will go off.
print(time_when_alarm_go_off)
