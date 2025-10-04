def case6_is_armstrong(n):
    s = str(n)
    p = len(s)
    return sum(int(d) ** p for d in s) == n

print("# Case 6 Output")
print(case6_is_armstrong(153))  # True
print(case6_is_armstrong(370))  # True
print(case6_is_armstrong(123))  # False
print()