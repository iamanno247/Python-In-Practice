n = int(input())
nums = [int(input()) for _ in range(n)]

# Hint: write a function that returns a tuple (min, max),
# then unpack and print each on its own line.

def min_max(numbers):
    return min(nums), max(nums)

min, max = min_max(nums)

print(min)
print(max)