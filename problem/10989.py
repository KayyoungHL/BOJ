# https://www.acmicpc.net/problem/10989
import sys

# def half_search(lst, x) :
    # idx = int(len(lst)/2)
    # if lst[0]>x : return [x] + lst
    # elif lst[-1]<=x : return lst + [x]

    # if x == lst[idx] : return lst[:idx]+[x]+lst[idx:]
    # elif x > lst[idx] : 
    #     if x < lst[idx+1] : return lst[:idx+1]+[x]+lst[idx+1:]
    #     else : return lst[:idx+1] + half_search(lst[idx+1:],x)
    # elif x < lst[idx] :
    #     if x > lst[idx-1] : return lst[:idx]+[x]+lst[idx:]
    #     else : return half_search(lst[:idx],x) + lst[idx:]

# def half_search2(lst, x) :
    # idx = int(len(lst)/2)
    # if lst[0]>x : return [x] + lst
    # elif lst[-1]<=x : return lst + [x]

    # fixed_idx = idx
    # while True :
    #     if x == lst[idx] : return lst[:idx]+[x]+lst[idx:]
    #     elif x > lst[idx] : 
    #         if x <= lst[idx+1] : return lst[:idx+1]+[x]+lst[idx+1:]
    #         else : 
    #             fixed_idx = round(fixed_idx/2)
    #             idx = idx + fixed_idx
    #     elif x < lst[idx] :
    #         if x >= lst[idx-1] : return lst[:idx]+[x]+lst[idx:]
    #         else : 
    #             fixed_idx = round(fixed_idx/2)
    #             idx = idx - fixed_idx

# def main() : 
    # n = int(sys.stdin.readline())
    
    # counts = {}
    # for _ in range(n) :
    #     x = int(sys.stdin.readline())
    #     counts[x] = counts.get(x, 0) + 1

    # k = sorted(counts.items())
    # for i in range(len(k)) :
    #     for _ in range(k[i][1]) :
    #         sys.stdout.write(str(k[i][0])+"\n")

def main2() : 
    n = int(sys.stdin.readline())
    
    lst = [0]*10001
    for i in range(n) :
        lst[int(sys.stdin.readline())] += 1

    for i in range(1, 10001) :
        for _ in range(lst[i]) :
            sys.stdout.write(str(i)+"\n")


if __name__=="__main__" :
    main2()