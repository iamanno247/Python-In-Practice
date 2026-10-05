n = int(input())
nums = [int(input()) for _ in range(n)]
# Find and print the second largest unique value

unique_num = []

for num in nums:
    if num not in unique_num:
        unique_num.append(num)
        
unique_num.sort()

print(unique_num[-2])