import sys


# def main():
#     n = int(sys.stdin.readline())
    
#     # table = {}
#     # times = []
#     # for _ in range(n):
#         # k, v = map(int,sys.stdin.readline().split())
#         # if k == v:
#             # times.append((k,v))
#         # else:
#         #     if k in table:
#         #         if table[k] > v:
#         #             table[k] = v
#         #     else:
#         #         table[k] = v
#     # times.extend(list(table.items()))

#     times = [tuple(map(int,sys.stdin.readline().split())) for _ in range(n)]
#     times.sort(key=lambda x:(x[0],x[1]))

#     ln = len(times)
#     ans = [0]*ln
#     for i in range(ln):
#         x = 0
#         for j in range(i, -1, -1):
#             if times[j][1] <= times[i][0]:
#                 if ans[j] > x:
#                     x = ans[j]
#                     break
#         ans[i] = x + 1
#     # print(times)
#     # print(ans)
#     print(ans[-1])
    
def main():
    n = int(sys.stdin.readline())
    times = [tuple(map(int,sys.stdin.readline().split())) for _ in range(n)]
    times.sort(key=lambda x:(x[1],x[0]))

    cnt = 1
    endtime = times[0][1]
    for i in range(1,n):
        if times[i][0] >= endtime:
            endtime = times[i][1]
            cnt += 1
    
    print(cnt)

if __name__ == "__main__":
    main()

"""
11
1 1
1 5
3 3
4 4
4 4
4 4
4 5
5 6
6 10
7 7
8 8

17
2 9
3 11
5 12
4 54
9 52
4 63
26 43
8 73
3 87
2 91
51 51
32 82
45 83
38 91
60 94
68 94
84 93
"""