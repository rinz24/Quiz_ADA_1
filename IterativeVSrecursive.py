import tkinter as tk
from tkinter import ttk
import time
import psutil
import os
import sys

# Set recursion limit to handle higher values in recursion
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
    return process.memory_info().rss / 1024 / 1024  # Return memory in MB

# Function to measure time and memory for both methods for a given n
def measure_time_and_memory(n):
    results = {}

    # Iterative method
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

    # Recursive method
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

# Function to find maximum n for both methods
def find_max_survival(n_values):
    max_iterative_n = None
    max_recursive_n = None
    for n in n_values:
        results = measure_time_and_memory(n)

        if results['iterative_time'] is not None:
            max_iterative_n = n
        if results['recursive_time'] is not None:
            max_recursive_n = n
        update_table(n, results)
    
    # Display maximum n values for both methods
    result_text.set(f"Max Iterative n: {max_iterative_n}, Max Recursive n: {max_recursive_n}")

# Update the table with results for each n
def update_table(n, results):
    tree.insert("", "end", values=(n, 
                                f"{results['iterative_time']:.6f}" if results['iterative_time'] else "N/A", 
                                f"{results['recursive_time']:.6f}" if results['recursive_time'] else "N/A", 
                                f"{results['iterative_memory']:.6f}" if results['iterative_memory'] else "N/A", 
                                f"{results['recursive_memory']:.6f}" if results['recursive_memory'] else "N/A"))

# Start the comparison based on user input
def start_comparison():
    tree.delete(*tree.get_children())  # Clear previous results
    n_values = [int(x) for x in entry.get().split(",")]  # Get n values from entry field
    find_max_survival(n_values)

# GUI code using Tkinter to display the results in a table
def create_gui():
    global root, entry, tree, result_text

    root = tk.Tk()
    root.title("Factorial Comparison (Iterative vs Recursive)")

    # Entry for input n values
    entry_label = tk.Label(root, text="Enter n values (comma separated):")
    entry_label.pack(pady=5)
    entry = tk.Entry(root, width=50)
    entry.pack(pady=5)
    # you can enter any number of values in the table 
    entry.insert(0, "10, 100, 150, 200, 250, 500, 1000, 1500, 2000, 3000, 4000, 5000, 6000")

    # Button to start comparison
    start_button = tk.Button(root, text="Start Comparison", command=start_comparison)
    start_button.pack(pady=10)

    # Table to display results
    tree = ttk.Treeview(root, columns=("n", "Iterative Time", "Recursive Time", "Iterative Memory", "Recursive Memory"), show="headings")
    tree.heading("n", text="n")
    tree.heading("Iterative Time", text="Iterative Time (s)")
    tree.heading("Recursive Time", text="Recursive Time (s)")
    tree.heading("Iterative Memory", text="Iterative Memory (MB)")
    tree.heading("Recursive Memory", text="Recursive Memory (MB)")
    tree.pack(fill=tk.BOTH, expand=True)

    # Result label to display max n values
    result_text = tk.StringVar()
    result_label = tk.Label(root, textvariable=result_text)
    result_label.pack(pady=10)

    # Start the GUI event loop
    root.mainloop()

# Run the GUI
create_gui()
