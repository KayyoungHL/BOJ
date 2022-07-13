import sys

def floydwarshall(n:int, graph:list) -> list:
    """플로이드 와샬 알고리즘을 통한 경로 존재 유무 확인
    1 갈 수 있음 0 못 감

    Args:
        n (int): 노드의 수
        graph (list): 그래프 인접리스트

    Returns:
        graph (list): 결과 그래프 인접 리스트
    """
    # i = 출발지, j = 도착지, k = 경유지
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j]=="1" or (graph[i][k]=="1" and graph[k][j]=="1"):
                    graph[i][j] = "1"
    return graph

def main():
    n = int(sys.stdin.readline())
    admatr = [sys.stdin.readline().split() for _ in range(n)]

    floydwarshall(n, admatr)
    for i in admatr:
        print(" ".join(i))

if __name__ == "__main__":
    main()