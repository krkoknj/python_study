import random

word_list = ["ardvark", "baboon", "camel"]
random_word = random.choice(word_list)
random_word_blank = []

print(f"Pssst, the solution is {random_word}")
for i in range(0, len(random_word)):
    random_word_blank.append("_")

flag = False
count = 6
print(f"You have {count}")

user_choice_check_list = []
while not flag:

    user_choice = input("Choose word: ")

    if user_choice not in user_choice_check_list:
        user_choice_check_list += user_choice
    else:
        print(f"You already guessed {user_choice}")
        continue

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
