## tree problem
## read in data
with open('input.txt') as f:
	data = f.read().splitlines()

# get length of each row
for i in data:
    len(i) 
# 31
# 3 right, 1 down

# track position across data
pos = 0
for row in data:
    tree = []
    pos += 3
    if row[pos] == '#':
        tree.append(1)
        print(tree)
    else:
        continue


    
