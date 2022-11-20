import  random

name_string = input("Give me everybody`s names")
name = name_string.split(", ")

random_name = random.randint(0, len(name) - 1)

print(name[random_name])




