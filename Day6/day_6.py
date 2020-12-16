import re 
with open('input.txt') as f:
    fata = f.read().split('\n\n')
    fata = [list(set(x.replace('\n',''))) for x in fata]
    

print(fata)