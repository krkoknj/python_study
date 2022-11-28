# n = int(input("Check this number : "))



def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"prime number {number}")


for i in range(1, 101):
    prime_checker(i)