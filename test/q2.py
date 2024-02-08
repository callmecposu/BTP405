import matplotlib.pyplot as plt

dict = {"0-10": 0, "11-20":0, "21-30":0, "31-40":0, "41-50":0}

def readFile(t):
    f = open(t, 'r')
    for line in f:
        line = int(line)
        if line >= 0 and line <= 10:
            dict["0-10"]+=1
        elif line <= 20:
            dict["11-20"]+=1
        elif line <= 30:
            dict["21-30"]+=1
        elif  line <= 40:
            dict["31-40"]+=1
        elif line <= 50:
            dict["41-50"]+=1


def graphSnowfall(t):
    readFile(t)
    plt.bar(dict.keys(), list(dict.values()), width=0.8)
    plt.xlabel('Snow Height')
    plt.ylabel('Number of Records')
    plt.title('Snowfall Graph')
    plt.savefig('snowfall.png')

graphSnowfall('q2.txt')