def case2_pos_neg_zero(n): return f"The number is {'Zero' if n == 0 else 'Positive' if n > 0 else 'Negative'}"

print("# Case 2 Output")
print(case2_pos_neg_zero(10))   # The number is Positive
print(case2_pos_neg_zero(-5))   # The number is Negative
print(case2_pos_neg_zero(0))    # The number is Zero
print()