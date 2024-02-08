def wordCount(t):
    # get the keys for the dict
    f = open(t, 'r')
    dict = {word: [] for word in set(f.read().split())}
    f.close()
    # get the values for the dict
    f = open(t, 'r')
    lineNum = 1
    for line in f:
        for word in line.split():
            dict[word].append(lineNum)
        lineNum+=1
    print(dict)

wordCount('q3.txt')