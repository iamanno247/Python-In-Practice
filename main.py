text = input().strip().split()
# Count word frequencies and print each in first-seen order

text_dict = {}

for words in text:
    text_dict[words] = text.count(words)
    
for key, value in text_dict.items():
    print(f"{key} {value}")