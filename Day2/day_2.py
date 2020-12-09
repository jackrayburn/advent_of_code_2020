## first item is number of times the second item can appear
## so 1-3 a: abcde:
## abcde must contain at least 1 a and no more than 3


## part 1 
## how many are valid?
## imports
import re

# reading data
with open('input.txt') as f:
	data = f.read().splitlines()


# testing
# test1 = re.split(r' ', data[1])
# test_range = re.split('-', test1[0])
# for i in range(0, len(test_range)):
#     test_range[i] = int(test_range[i])
# test3 = re.split(':',test1[1])
# test3 = test3[0]
# print(test1)
# print(test_range)
# print(test3)
# finaltest = re.findall(test3, test1[2])
# working statement
# if len(finaltest) >= test_range[0] and len(finaltest) <= test_range[1]:
#     print(True)
# else:
#     print(False)
# print(finaltest)

# now the whole list -- test stuff above kinda messed up final solution
def solve():
    result = 0
    for i in range(0, len(data)):
        main = re.split(r' ', data[i])
        rang = re.split('-', main[0])
        for x in range(0, len(rang)):
            rang[x] = int(rang[x])
        letter = re.split(':',main[1])
        letter = letter[0]
        final = re.findall(letter, main[2])
        if len(final) >= rang[0] and len(final) <= rang[1]:
            result += 1
        else:
            continue
    return result
print(solve())

## part 2 
## the range must contain the letter exactly once
## 1-3 a: abcde is valid bc a is in 1 and not in 3
# very similar, just final needs to be altered

def part_2():
    res = 0
    for i in range(0, len(data)):
        mainb = re.split(r' ', data[i])
        rang_2 = re.split('-', mainb[0])
        for x in range(0, len(rang_2)):
            rang_2[x] = int(rang_2[x])
        letterb = re.split(':',mainb[1])
        letterb = letterb[0]
        passb = mainb[2]
        rang_a = rang_2[0]
        rang_b = rang_2[1]
        finalb = []
        if len(passb) < rang_a:
            break
        elif len(passb) >= rang_a and len(passb) >= rang_b:
            finalb.append(passb[rang_2[0]-1])
            finalb.append(passb[rang_2[1]-1])
        elif len(passb) >= rang_a:
            finalb.append(passb[rang_2[0]-1])
        elif len(passb) >= rang_b:
            finalb.append(passb[rang_2[1]-1])
        if finalb[0] == letterb and finalb[1] != letterb:
            res += 1
        elif finalb[1] == letterb and finalb[0] != letterb:
            res += 1
    return res
print(part_2())

# little long but works