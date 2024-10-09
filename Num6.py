def main():
    n = 10  # Example initialization of n; from the questions

    #Doubling n
    n = n * 2
    print(f"After doubling, n = {n}")

    #Loop from n to 0
    for a in range(n, 0, -1):  # Looping from n down to 1
        if a == n:
            a = a / 2  # This assignment doesn't affect the loop control variable
        
        # Debug output to show the value of a in each iteration
        print(f"Current value of a: {a}")

# Run the main function
if __name__ == "__main__":
    main()
