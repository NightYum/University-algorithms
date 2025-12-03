student = {'name': 'Aruzhan', 'age': 20, 'grade': 'A'}

key = "email"

if key in student:
    print(student.get(key))
else:
    print("No such key")