## tree problem
## read in data
with open('input.txt') as f:
	data = f.read().splitlines()

# get length of each row
for i in data:
    len(i) 
# 31
# 3 right, 1 down
del data[0]
# track position across data
pos = 0
tree = 0
dat = 1
for row in data:
    print(dat)
    print(tree)
    if pos == 30:
        pos = 2
    elif pos == 29:
        pos = 1
    elif pos == 28:
        pos = 0
    else:
        pos += 3
    if row[pos] == '#':
        tree += 1
    
    print(row[pos])
    print(pos)
    print("end")
    dat += 1
    

    
