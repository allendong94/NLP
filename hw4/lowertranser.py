f = open('dev.trees', 'r')
f2 = open('dev.lower.trees', 'w')
for line in f:
    x = line.lower()
    f2.write(x)
f.close()
f2.close()