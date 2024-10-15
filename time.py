#David Cardona - October 15, 2024

# Fixed the missing closing parenthesis in the second input statement.
currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait?")

# Fixed variable names to be consistent.
currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

# Calculate final time and print result.
finalTimeInt = currentTimeInt + waitTimeInt
print(finalTimeInt)
