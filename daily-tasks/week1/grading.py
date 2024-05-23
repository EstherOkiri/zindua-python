name = "Esther"
score = int(input("Enter student score : "))

if(score >= 90):
    grade = "A"
elif(score >=80) & (score <=79):
    grade = "B"
elif(score >=70) & (score<=79):
    grade = "C"
elif(score >=60) & (score <=69):
    grade = "D"
else:
    grade = "F"

#output

print(f"Student score is {score}")
print(f"Student grade is {grade}")

