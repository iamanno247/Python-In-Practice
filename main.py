n = int(input())
nums = [int(input()) for _ in range(n)]
# Use a comprehension to filter the evens and double each

result = [x * 2 for x in nums if x % 2 ==0]

for num in result:
    print(num)