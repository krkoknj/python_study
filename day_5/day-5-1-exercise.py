student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)

sum = 0
for s in student_heights:
    sum += s

num = 0
for i in student_heights:
    num += 1;



total = sum / num
print(round(total, 2))