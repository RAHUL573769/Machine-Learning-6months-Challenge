student_data=[
    {

        "name":"Rahul- Rudra",
        "course":"Python"
    }


]

def add_new_student(name,course,courseName):
    newStudent={}
    newStudent["name"]=name
    newStudent["course"]=course
    newStudent["courseName"]=courseName
    student_data.append(newStudent)



add_new_student("Shyam",22,"C++")

print(student_data)