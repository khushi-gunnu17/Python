marks = [12, 13, 14, 15, "maths"]
print(marks)
print(marks[0])
print(marks[-1])

print(marks[0:2])

for score in marks :
    print(score)

marks.append(99)
marks.insert(0, 99)
print(marks)

print(99 in marks )

print(len(marks))

i = 0
while i < len(marks) :
    print(marks[i])
    i += 1

marks.clear()
print(marks)