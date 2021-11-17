# https://www.acmicpc.net/problem/1904
import sys

# import numpy as np
# def combination(higher,lower) :
#         if lower == 0 :
#             return 1
#         answer = higher/lower
#         for i in range(1,lower) :
#             answer = answer*(higher-i)/(lower-i)
#         return round(answer)

# def matrix (n) :
    # matrix = []

    # for i in range(n) :
    #     temp = []
    #     for j in range(n) :
    #         if (i == 0) or (j == 0) : temp.append(1)
    #         else : temp.append((matrix[i-1][j]+temp[j-1])%15746)
    #     matrix.append(temp)
    # return matrix

# def main() : 
#     # n = int(sys.stdin.readline())
#     a = []
#     for n in range(100) :    
#         num_00s = (n//2)

#         answer = 0
    
#         for num_00 in range(num_00s+1) :
#             num_1 = (n-num_00*2)

#             if num_1 > num_00 : low = num_00
#             else : low = num_1
#             # print(f"{num_1+num_00}C{num_00} =", combination((num_1+num_00),low))
#             answer += combination(num_1+num_00,low)

#         a.append(answer%15746)
#         print(n,":",answer%15746)
    

def main() :
    n = int(sys.stdin.readline())

    pre = 0
    cur = 1
    for _ in range(n) :
        pre, cur = cur, (pre+cur)%15746
    
    print(cur)

if __name__=="__main__" :
    main()