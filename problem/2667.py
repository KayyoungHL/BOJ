import sys

def main():
    n = int(sys.stdin.readline())

    table = [list(sys.stdin.readline().strip()) for _ in range(n)]
    nodes = {(i,j):n*i+j for i in range(n) for j in range(n) if table[i][j] == "1"}
    nets = {n*i+j:[(i,j)] for i in range(n) for j in range(n) if table[i][j] == "1"}

    for i,j in nodes:
        a = nodes[(i, j)]
        for ni, nj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if (ni,nj) in nodes:
                b = nodes[(ni, nj)]
                if a != b:
                    low = a
                    high = b
                    if low > high:
                        low, high = high, low
                    for i in nets[high]:
                        nodes[i] = low
                        nets[low].append(i)
                    del nets[high]

    print(len(nets))
    for x in sorted([len(i) for i in nets.values()]):
        print(x)
    

if __name__ == "__main__":
    main()

