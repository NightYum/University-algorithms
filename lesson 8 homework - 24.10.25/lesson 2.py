student = {"name": "Mikhail", "age": 17, "major": "SE", "grades": [10, 20,30]}

student.update(university="Almau")
student["age"] = 18

print(student)
print(student.get("age"))
