marks = {"ankit" : 100, "vrishti": 90, "rahul" : 85, "sonam" : 80, "sachin" : 70, "anurag" : 60}

name = input("Enter the name of the student: ")
if name.lower() in marks:
    print(f"{name} marks: {marks[name]}")
else:
    print("Student not found")