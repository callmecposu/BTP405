def decorator(numbers):
    print(f'Numbers read: {numbers}')
    print(f'Count: {len(numbers)}')
    print(f'Avg: {sum(numbers) / len(numbers)}')
    print(f'Max: {max(numbers)}')
    print('')

def printStats(t):
    f = open(t, 'r')
    for line in f:
        numbers = []
        for word in line.split():
            numbers.append(int(word))
        decorator(numbers)
        
printStats('q4.txt')