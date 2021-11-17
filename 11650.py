# https://www.acmicpc.net/problem/11650
import sys

# def half_search(lst, x) :
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

    # x, y = map(int,sys.stdin.readline().split())
    # x += 100000
    # y += 100000
    # x = str(x).zfill(6)
    # y = str(y).zfill(6)
    # lst = [int(x+y)]
    # for _ in range(n-1) :
    #     x, y = map(int,sys.stdin.readline().split())
    #     x += 100000
    #     y += 100000
    #     x = str(x).zfill(6)
    #     y = str(y).zfill(6)
    #     xy = int(x+y)
    #     lst = half_search(lst, xy)

    # for i in range(n) :
    #     l = str(lst[i]).zfill(12)
    #     sys.stdout.write(str(int(l[:-6])-100000)+" "+str(int(l[6:])-100000)+"\n")

def main() :
    n = int(sys.stdin.readline())
    lst = []
    for _ in range(n) :
        lst.append(list(map(int,sys.stdin.readline().split())))

    lst = sorted(lst,key=lambda x : (x[0],x[1]))
    for i in lst :
        sys.stdout.write(str(i[0])+" "+str(i[1])+"\n")

if __name__=="__main__" :
    main()