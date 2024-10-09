# NUMBERS

# Find pi to the Nth Digit

# Enter a number and the program will generate Pi up to that many decimal places. Keep a limit.
import math

limit = 50

def pi_gen():
    generate = int(input("How many decimal points of PI would you like to see?\n"))

    if generate > limit:
        print(f"You tried to generate more than {limit} decimal points. Try again.")
        pi_gen()
    else:
        print(f"{math.pi:.{generate}}")

pi_gen()




