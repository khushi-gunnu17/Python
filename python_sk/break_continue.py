students = ["khushi", "mansi", "himanshi", "karan", "ayush"]

for student in students :
    if student == "karan" :
        break

    if student == "khushi" :
        continue
    print(student)

print()

i = 0
while i< len(students) :
    print(students[i])
    i += 1