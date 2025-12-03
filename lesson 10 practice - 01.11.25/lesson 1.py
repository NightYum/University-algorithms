students_dict = {"Mikhail": [10, 8, 7, 6, 5, 4],
                 "Notebook": [10, 10, 10, 5, 4],
                 "Michael": [10, 2, 3, 5, 4]
                 }

for i in students_dict.keys():
    students_dict[i] = sum(students_dict[i])/len(students_dict[i])

print(max(students_dict, key=students_dict.get))