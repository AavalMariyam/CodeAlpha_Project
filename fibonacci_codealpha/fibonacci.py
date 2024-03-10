def generate_fibonacci(limit):
    fib_sequence = [0, 1]  
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]  
        if next_fib <= limit: 
            fib_sequence.append(next_fib)  
        else:
            break  
    return fib_sequence

limit = int(input("Enter the limit to generate Fibonacci sequence: "))
fib_sequence = generate_fibonacci(limit)
print("Fibonacci sequence up to", limit, ":", fib_sequence)
