import random

word_list = ["ardvark", "baboon", "camel"]
random_word = random.choice(word_list)
random_word_blank = []

print(f"Pssst, the solution is {random_word}")
for i in range(0, len(random_word)):
    random_word_blank.append("_")

flag = False
count = 5
print(f"You have {count}")
while not flag:

    user_choice = input("Choose word: ")

    for r in range(0, len(random_word)):
        letter = random_word[r]
        if letter == user_choice:
            random_word_blank[r] = letter

    print(random_word_blank)

    if user_choice not in random_word:
        count -= 1
        print(f"You have {count}")

    if count == 0:
        print("You Lose")
        flag = True

    if "_" not in random_word_blank:
        flag = True
        print("Win")
