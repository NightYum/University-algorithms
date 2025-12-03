def student_info(name, age, **subjects):
    if not subjects:
        print("Данных об этом пользователе нет")

    avg = sum(subjects.values()) / len(subjects)
    print(name, age,avg)

student_info("Mikhail", 17, math=90, english=20, history=100)