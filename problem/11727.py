import sys

def main():
    n = int(sys.stdin.readline())

    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a*2+b)%10007
    
    print(b)


if __name__ == "__main__":
    main()
