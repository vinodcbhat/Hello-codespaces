print ("Hello from Github codespaces")
print (" You have succesfully run your first program")

def fibonacci_iterative(n):
    """Generates the first n Fibonacci numbers using iteration."""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

    # Example usage:
num_terms = 10
print(f"Fibonacci series of the first {num_terms} terms:{fibonacci_iterative(num_terms)}")