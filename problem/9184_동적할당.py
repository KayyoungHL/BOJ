# https://www.acmicpc.net/problem/9184
import sys
import copy
"""
if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
"""

# def w (a,b,c) :
#     if (a <= 0) or (b <= 0) or (c <= 0) : return 1
#     elif (a > 20) or (b > 20) or (c > 20) : return 1048576
#     elif (b==1) and (c==1) : return a+1
#     elif (a <= b) or (a < c) : return 2**a
#     elif a<b<c : return w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
#     else : return w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)

def main() : 
    x = [1]*21
    y = [copy.deepcopy(x) for _ in range(21)]
    d_list = [copy.deepcopy(y) for _ in range(21)]
    
    for a in range(1,21) :
        for b in range(1,21) :
            for c in range(1,21) :
                d_list[a][b][c] = d_list[a-1][b][c]+d_list[a-1][b-1][c]+d_list[a-1][b][c-1]-d_list[a-1][b-1][c-1]
    
    while True :
        a, b, c = list(map(int, sys.stdin.readline().split()))
        if (a, b, c) == (-1,-1,-1) : break
        
        if (a <= 0) or (b <= 0) or (c <= 0) :
            print(f"w({a}, {b}, {c}) = 1")
            continue
        elif (a > 20) or (b > 20) or (c > 20) :
            print(f"w({a}, {b}, {c}) = 1048576")
            continue
        else : print(f"w({a}, {b}, {c}) = {d_list[a][b][c]}")

if __name__=="__main__" :
    main()