def case3_is_anagram(s1, s2):
    return ''.join(sorted(s1)) == ''.join(sorted(s2))

print("# Case 3 Output")
print(case3_is_anagram("listen", "silent"))  # True
print(case3_is_anagram("hello", "world"))    # False
print()
