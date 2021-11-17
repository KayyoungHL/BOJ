# https://www.acmicpc.net/problem/2108
import sys

def main() : 
    n = int(sys.stdin.readline())
    
    x = list()
    counts = {}
    for _ in range(n) :
        t = int(sys.stdin.readline())
        x.append(t)
        counts[t] = counts.get(t, 0) + 1
    x.sort()
    print(round(sum(x)/n))
    print(x[int(n/2)])

    k = sorted(counts.items(), key=lambda t: t[1], reverse=True)
    counts = {}
    for i in k :
        counts[i[1]] = counts.get(i[1], [])
        counts[i[1]].append(i[0])
    if len(counts[k[0][1]]) >= 2 : print(sorted(counts[k[0][1]])[1])
    else : print(sorted(counts[k[0][1]])[0])

    print(x[-1]-x[0])

if __name__=="__main__" :
    main()