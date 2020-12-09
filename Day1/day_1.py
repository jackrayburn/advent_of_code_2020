## find 2 entries that sum to 2020 from input.txt
## final answer is product of 2 entries

# reading input
arr = []
f =open("input.txt","r")
for line in f:
    arr.append(int(line.strip()))
f.close()

# iterating through array

def part_1():
    totez = []
    x = arr
    for i in arr:
        for item in x:
            if i + item == 2020:
                totez.append(i)
                totez.append(item)
                break
            else:
                continue
    return totez
total = part_1()
final = total[0] * total[1]
print(final)

## part two 
## 3 entries that equal 2020
## product of these
def part_2():
    too = 0
    x = arr 
    y = arr
    numbs = []
    
    for i in arr:
        for xi in x:
            for yi in y:
                too = i + xi + yi
                if too == 2020:
                    numbs.append(i)
                    numbs.append(xi)
                    numbs.append(yi)
                    break
                else:
                    continue
                    
    return numbs

total2 = part_2()
final2 = total2[0] * total2[1] * total2[2]
print(final2)
# not the best but it works