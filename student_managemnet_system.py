#Student management system
#Run data analysis on student marks
#Find the highest score in each subject
#Print the name of the highest scorer


student_1 = {
    "Name" : "Thanmay",
    "Maths" : 20,
    "science" : 45,
    "social" : 800 }


student_2 = {
    "Name" : "Deeraj",
    "Maths" : 30,
    "science" :50,
    "social" : 100 }

student_3 = {
    "Name" : "Sooraj",
    "Maths" : 40,
    "science" :10,
    "social" : 120 }

students = [student_1,student_2,student_3]


highest_score_in_science = 0
highest_score_in_social = 0



def student_maths(students):
    highest_scorer_name_in_maths = ""
    highest_score_in_math = 0
    for every_student in students :
        if(every_student.get("Maths") > highest_score_in_math):
          highest_score_in_math = every_student.get("Maths")
          highest_scorer_name_in_maths = every_student.get("Name")



    print(f"{highest_scorer_name_in_maths} scored the highest in maths ,with the score of {highest_score_in_math}")


def student_science(students):
    highest_scorer_name_in_science = ""
    highest_score_in_science = 0
    for every_student in students :
        if(every_student.get("science") > highest_score_in_science):
            highest_score_in_science = every_student.get("science")
            highest_scorer_name_in_science = every_student.get("Name")



    print(f"{highest_scorer_name_in_science} scored the highest in science ,with the score of {highest_score_in_science}")


def student_social(students):
    highest_scorer_name_in_social = ""
    highest_score_in_social = 0
    for every_student in students :
        if(every_student.get("social") > highest_score_in_social):
            highest_score_in_social = every_student.get("social")
            highest_scorer_name_in_social = every_student.get("Name")



    print(f"{highest_scorer_name_in_social} scored the highest in social ,with the score of {highest_score_in_social}")

student_maths(students)
student_science(students)
student_social(students)
