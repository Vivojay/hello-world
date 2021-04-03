import time

lychrelCandidates = []

def revnadd(n, threshold = 1000):
    global lychrelCandidates
    a = n
    count=0
    while (not str(n) == str(n)[::-1] and count < threshold):
        n += int(str(n)[::-1])
        count += 1
        
    if not count >= threshold:
        return (a, n, count)
    else:
        lychrelCandidates.append(a)
        return (a, False, count)

def iterateLychrels(N, thresh = 1000, start = 1):
    global lychrelCandidates
    lychrelCandidates = []
    
    start = int(start)
    if start <= 0:
        start = 1
        print (start)
    return [revnadd(i, thresh) for i in range(start, N+1)]

'''    
    try:
        start = int(start)
        if start <= 0:
            start = 1
            print (start)
        return [revnadd(i, thresh) for i in range(start, N+1)]
    except:
        print('Invalid start value')
'''

def startCalc(NUM, start = 1, thresh = 1000): #NUM = final/end value
    global lychrelCandidates, values, iterlist, longestIterLength, numbersWithLargestIterations

    start = time.time()

    lychrelCandidates = []
    values = iterateLychrels(NUM, thresh, start)
    iterlist = [i[2] for i in values]
    if not max(iterlist) == thresh:
        longestIterLength = max(iterlist)
    else:
        longestIterLength = list(set(iterlist))
        longestIterLength.remove(thresh)
        longestIterLength = max(longestIterLength)
    numbersWithLargestIterations = [i+1 for i, x in enumerate(iterlist) if x == longestIterLength]
    stop = time.time()

    duration = stop - start
    print('Time taken:', duration)

