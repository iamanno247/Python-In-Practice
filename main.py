from collections import defaultdict

num = int(input())
groups = defaultdict(list)

for _ in range(num):
    student, group = input().strip().split()
    groups[group].append(student)
    
for group , students in groups.items():
    print(f"{group}: {', '.join(students)}")