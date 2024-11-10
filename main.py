d={'a':12, 'b':13, 'c':12, 'e':13, 'f':2}
count=0
for c in d.values():
    if c==2:
        count+=1
print('Frequency of 2: ',count)