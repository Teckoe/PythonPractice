StudentName = input("Student Name: ")
ICThwk = int(input("Please enter ICT Homework score: "))
Assessment = int(input("Please enter Assessment score:"))
Exam = int(input("Please enter Exam Score: "))





def total(ICThwk, Assessment, Exam):
    ICT_mark = ICThwk * 4
    Assessment_mark = Assessment * 2
    GrandTotal = (ICT_mark + Assessment_mark + Exam) / 3
    return GrandTotal


def grade(GrandGrandTotal):
    if GrandGrandTotal <= 30:
        return "F"
    elif GrandGrandTotal <= 40:
        return "E"
    elif GrandGrandTotal <= 50:
        return "D"
    elif GrandGrandTotal <= 60:
        return "C"
    elif GrandGrandTotal <= 70:
        return "B"
    elif GrandGrandTotal <= 80:
        return "A"


total2 = total(ICThwk, Assessment, Exam)
print(total2)
grade2 = grade(total2)


print("Final grade for", StudentName, "Is", grade2)
