student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(student_scores)

max_num = student_scores[0];
for n in range(1, len(student_scores)):
    if max_num < student_scores[n]:
        max_num = student_scores[n]
print(max_num)

highest_scores = 0
for score in student_scores:
    if highest_scores < score:
        highest_scores = score
print(highest_scores)


