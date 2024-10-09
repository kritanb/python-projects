# NUMBERS

# Fibonacci Sequence

# Returns the fibonacci number in the particular index that user inputs

def fibonacci_gen(num_gen):
    if num_gen == 0:
        return 0
    elif num_gen == 1:
        return 1
    
    fibonacci_sequence = [0, 1]
    
    for _ in range(2, num_gen):
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fib)
    
    return fibonacci_sequence[-1]

if __name__ == "__main__":
    num_gen = int(input("Which Fibonacci number do you want? "))
    print(fibonacci_gen(num_gen))
