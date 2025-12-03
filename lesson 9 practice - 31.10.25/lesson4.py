def student_profile(name, age, country):
    return f"Hello, {name}! You are {age} years old. I'm from {country}."

print(student_profile("Mikhail", 18, "Almaty"))
print(student_profile(age=18, name="Mikhail", country="US"))