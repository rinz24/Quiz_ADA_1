import time
import psutil
import os
import sys
import tkinter as tk
from tkinter import ttk

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
    results_list = []

    for n in n_values:
        # Measure time and memory for both methods
        results = measure_time_and_memory(n)

        # Store results
        results_list.append({
            'n': n,
            'iterative_time': results['iterative_time'],
            'iterative_memory': results['iterative_memory'],
            'recursive_time': results['recursive_time'],
            'recursive_memory': results['recursive_memory'],
        })

    return results_list

# Function to display results in the GUI
def display_results():
    # Clear the tree
    for row in tree.get_children():
        tree.delete(row)

    # Get results and insert into the table
    results = find_max_survival(n_values)
    for result in results:
        tree.insert("", "end", values=(result['n'],
                                        f"{result['iterative_time']:.6f}" if result['iterative_time'] is not None else "Failed",
                                        f"{result['iterative_memory']:.6f}" if result['iterative_memory'] is not None else "Failed",
                                        f"{result['recursive_time']:.6f}" if result['recursive_time'] is not None else "Failed",
                                        f"{result['recursive_memory']:.6f}" if result['recursive_memory'] is not None else "Failed"))

# List of n values to test
n_values = [10, 100, 150, 200, 250, 500, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

# Create the main window
root = tk.Tk()
root.title("Factorial Time and Memory Usage")

# Create a treeview to display results in a form of Table
tree = ttk.Treeview(root, columns=("n", "Iterative Time (s)", "Iterative Memory (MB)", "Recursive Time (s)", "Recursive Memory (MB)"), show='headings')
tree.heading("n", text="n")
tree.heading("Iterative Time (s)", text="Iterative Time (s)")
tree.heading("Iterative Memory (MB)", text="Iterative Memory (MB)")
tree.heading("Recursive Time (s)", text="Recursive Time (s)")
tree.heading("Recursive Memory (MB)", text="Recursive Memory (MB)")
tree.pack(fill=tk.BOTH, expand=True)

# Add a button to start the calculation
button = tk.Button(root, text="Calculate", command=display_results)
button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
