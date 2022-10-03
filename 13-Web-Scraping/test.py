tags = ['a', 'a', 'b', 'c', 'c', 'c']
unique_tags = {}

for tag in tags:
    if tag in unique_tags:
        unique_tags[tag]  += 1 
    else:
        unique_tags[tag] = 1
print(unique_tags)
unique_tags = dict(sorted(unique_tags.items(), key=lambda item: item[1])[::-1])
print(unique_tags)
for key,value in unique_tags.items():
    print (key, value)
