# Calculating Grades (ok, let me think about this one)
#new comment
# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int((input("Input exam grade three: ")))



summ=int(exam_one)+int(exam_two)+int(exam_three)
avg=float(summ)/int(3)


if int(avg)>= 90:
    letter_grade="A"
elif int(avg) < 90 and int(avg)>=80:
    letter_grade= "B"
elif int(avg)>=70 and int(avg) <=79:
    letter_grade="C"
elif int(avg)>= 60 and int(avg) <= 69:
    letter_grade="D"
else:
    letter_grade="F"

print(exam_one,exam_two,exam_three)
print("Average: " + str(int(avg)))
print("Grade: " + letter_grade)

if letter_grade=="F":
    print( "Student is failing.")
else:
    print ("Student is passing.")
