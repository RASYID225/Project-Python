def case4_factorial(n):
    return 1 if n == 0 else n * case4_factorial(n - 1)

print("# Case 4 Output")
print(case4_factorial(5))  # 120
print(case4_factorial(0))  # 1
print()
