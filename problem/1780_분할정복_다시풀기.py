import sys


# def div_con(table, ans):
#     n = len(table)
#     total = set()
#     for i in table:
#         total|= set(i)
#         if len(total) > 1:
#             break
#     if len(total) == 1:
#         if "-1" in total:
#             ans[0] += 1
#             return
#         elif "0" in total:
#             ans[1] += 1
#             return
#         else:
#             ans[2] += 1
#             return
#     div = n//3
#     for i in range(3):
#         for j in range(3):
#             div_con([x[j*div:(j+1)*div] for x in table[i*div:(i+1)*div]], ans)


# def main():
#     n = int(sys.stdin.readline())
#     table = [sys.stdin.readline().split() for _ in range(n)]

#     ans = [0,0,0]
#     div_con(table, ans)
#     print("\n".join(map(str,ans)))


def hashable(func):
    hashs = {}
    def wrapper(*args):
        if args[0] not in hashs:
            hashs[args[0]] = func(*args)
        return hashs[args[0]]
    return wrapper

@hashable
def div_con(table, ans, n):
    div = n//3
    tables = tuple(tuple(tuple(x[j*div:(j+1)*div]) for x in table[i*div:(i+1)*div]) for j in range(3) for i in range(3))
    x = set(tables)
    while len(x) == 1:
        if "-1" in x:
            return [1, 0, 0]
        elif "0" in x:
            return [0, 1, 0]
        elif "1" in x:
            return [0, 0, 1]
        x = set(*x)
    
    for i in tables:
        if len(i) != 1:
            x = div_con(i, [0,0,0], div)
            ans[0] += x[0]
            ans[1] += x[1]
            ans[2] += x[2]
        else:
            i = i[0][0]
            if i == "-1":
                ans[0] += 1
            elif i == "0":
                ans[1] += 1
            elif i == "1":
                ans[2] += 1
    
    return ans

def main():
    n = int(sys.stdin.readline())
    table = tuple(tuple(sys.stdin.readline().split()) for _ in range(n))

    ans = div_con(table, [0,0,0], n)
    print("\n".join(map(str,ans)))

if __name__ == "__main__":
    main()