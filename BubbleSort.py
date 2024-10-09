def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            # Show the array after each comparison
            print(f"Pass {i+1}, Comparison {j+1}: {arr}")
        
        # If no two elements were swapped in the inner loop, then break
        if not swapped:
            break
    
    return arr

# List of values
arr = [3, 41, 52, 26, 38, 57, 9, 29]

# Sorting the list using bubble sort
sorted_arr = bubble_sort(arr)

# Final sorted array
print("Sorted array:", sorted_arr)
