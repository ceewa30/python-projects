# nlist = [1, 2, 3]

# result = [(i * 5) for i in nlist if i == 3]
# print(result)

nums = [1, 2, 3, 4]
fruit = ['apple', 'peaches', 'pears', 'bananas']
for i in nums:
    if i > 1:
      if i !=3:
        for f in fruit:
            print(i, f)

result = [ (i,f) for i in nums for f in fruit if i > 1 if i != 3]
print(result)


for i in nums:
    if i > 1 and i !=3:
        for f in fruit:
            print(i, f)
