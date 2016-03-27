import os

files = []

for f in os.listdir("./wordbank"):
    if f.endswith(".txt"):
        print "loading " + f
        files.append("./wordbank/"+f)

words = []

i = 0;
for filename in files:
    f = open(filename, 'r')
    for line in f:
        words.append(line.rstrip())
        i = i+1
    f.close()


for w in words:
    print w
