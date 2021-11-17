# https://www.acmicpc.net/problem/17626
import sys

def main():
    n = int(sys.stdin.readline())

    k = int(n**0.5)
    if k**2==n: return print(1)
    for k2 in range(k,int(k**0.5)-1,-1):
        l = int((n - k2**2)**0.5)
        if n == l**2+k2**2:
            return print(2)
    for k2 in range(k,int(k**0.5)-1,-1):
        l = int((n - k2**2)**0.5)
        for k3 in range(l,int(l**0.5)-1,-1):
            m = int((n - k2**2-k3**2)**0.5)
            if n == m**2+k3**2+k2**2:
                return print(3)
    print(4)
    # for k2 in range(k,int(k**0.5),-1):
    #     l = int((n - k2**2)**0.5)
    #     for k3 in range(l,int(l**0.5),-1):
    #         m = int((n - k2**2-k3**2)**0.5)
    #         for k4 in range(m,int(m**0.5),-1):
    #             b = int((n - k2**2-k3**2-k4**2))
    #             if n == b**2+k4**2+k3**2+k2**2:
    #                 print(k2,k3,k4,b)
    #                 return print(4)


if __name__ == "__main__":
    main()

