def greet():
    print("greet")
    print("greet")
    print("greet")


greet()

                   #parameter
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

                #argument
greet_with_name("angela")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


greet_with("Jack Bauer", "Nowhere")
