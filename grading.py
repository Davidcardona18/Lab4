#David Cardona - October 15, 2024

# Fixed the input statement to use int and removed extra closing parenthesis.
exam_one = int(input("Input exam grade one: "))

# Fixed the input statement to use int and removed extra closing parenthesis.
exam_two = int(input("Input exam grade two: "))

# Fixed the input statement to use int (it was incorrectly set to str).
exam_three = int(input("Input exam grade three: "))

# Added commas between the variables in the list.
grades = [exam_one, exam_two, exam_three]

# Fixed variable names (for loop was using 'grade' instead of 'grades').
sum = 0
for grade in grades:
    sum += grade  # Fixed the for loop to correctly iterate over the grades.

# Corrected misspelled 'grdes' to 'grades'.
avg = sum / len(grades)

# Added missing colon after the if condition.
if avg >= 90:
    letter_grade = "A"

# Added missing colon after the elif condition.
elif avg >= 80 and avg < 90:
    letter_grade = "B"

# Fixed the condition to check the correct range and corrected mismatched quotes.
elif avg >= 70 and avg < 80:
    letter_grade = "C"

# Fixed condition for 'D' grade and corrected the range.
elif avg >= 60 and avg < 70:
    letter_grade = "D"

# Fixed the final elif to else for failing grade.
else:
    letter_grade = "F"

# Fixed the print statement to display each grade correctly.
for grade in grades:
    print("Exam: " + str(grade))

# Moved print statements outside the loop and fixed them to use parentheses (Python 3).
print("Average: " + str(avg))
print("Grade: " + letter_grade)

# Fixed variable name from 'letter-grade' to 'letter_grade' and corrected the print statement syntax.
if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")