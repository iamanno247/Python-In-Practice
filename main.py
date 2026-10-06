a = set(input().split())
b = set(input().split())
# Find common elements, sort them, print space-separated
and_sorted = sorted(a & b)

print(f"{' '.join(and_sorted)}")