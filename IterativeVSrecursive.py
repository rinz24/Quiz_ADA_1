import time
import psutil
import os
import sys

# Increase recursion limit for testing higher n values with recursion
sys.setrecursionlimit(10000)

# Function to calculate factorial iteratively
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Function to calculate factorial recursively
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Function to measure memory usage
def memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024  # Return memory usage in MB

# Function to measure time and memory for both methods for a given n
def measure_time_and_memory(n):
    results = {}

    # Iterative Method
    start_time_iterative = time.time()
    initial_memory_iterative = memory_usage()
    try:
        factorial_iterative(n)
        iterative_time = time.time() - start_time_iterative
        final_memory_iterative = memory_usage()
        iterative_memory = final_memory_iterative - initial_memory_iterative
        results['iterative_time'] = iterative_time
        results['iterative_memory'] = iterative_memory
    except Exception as e:
        results['iterative_time'], results['iterative_memory'] = None, None
    
    # Recursive Method
    start_time_recursive = time.time()
    initial_memory_recursive = memory_usage()
    try:
        factorial_recursive(n)
        recursive_time = time.time() - start_time_recursive
        final_memory_recursive = memory_usage()
        recursive_memory = final_memory_recursive - initial_memory_recursive
        results['recursive_time'] = recursive_time
        results['recursive_memory'] = recursive_memory
    except (RecursionError, Exception) as e:
        results['recursive_time'], results['recursive_memory'] = None, None
    
    return results

# Function to find the maximum n where both methods can process
def find_max_survival(n_values):
    max_iterative_n = None
    max_recursive_n = None

    for n in n_values:
        print(f"Testing n={n}...")

        # Measure time and memory for both methods
        results = measure_time_and_memory(n)

        # Check if iterative method was successful
        if results['iterative_time'] is not None:
            max_iterative_n = n
            print(f"Iterative: n={n}, Time: {results['iterative_time']:.6f} s, Memory: {results['iterative_memory']:.6f} MB")
        else:
            print(f"Iterative method failed for n={n}")

        # Check if recursive method was successful
        if results['recursive_time'] is not None:
            max_recursive_n = n
            print(f"Recursive: n={n}, Time: {results['recursive_time']:.6f} s, Memory: {results['recursive_memory']:.6f} MB")
        else:
            print(f"Recursive method failed for n={n}")
        
        print("-" * 50)

    return max_iterative_n, max_recursive_n

# List of n values to test
n_values = [10, 100, 150, 200, 250, 500, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

# Start testing
max_iterative, max_recursive = find_max_survival(n_values)

# Display final results
print(f"Maximum n for Iterative Method: {max_iterative}")
print(f"Maximum n for Recursive Method: {max_recursive}")
