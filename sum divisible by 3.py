N = int(input("Enter N: "))
total = sum(i for i in range(1, N + 1) if i % 3 == 0)
print(f"Sum of multiples of 3 up to {N}: {total}")