students = {
    "John":[86,72,75,60,95],
    "Lee":[80,84,66,78,70],
    "Lacey":[90,85,70,82,92]
}

for student,grades in students.items():
    total_marks = 0
    number_of_marks = len(grades)
    for grade in grades:
        total_marks = total_marks + grade
    average = total_marks / number_of_marks
    print(f"{student} Average : {average}")
    highest_average = 0
    if average > highest_average :
        highest_average = average
print(f"Highest Student: {student} Highest Average: {average} ")