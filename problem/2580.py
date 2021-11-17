# https://www.acmicpc.net/problem/2580
import sys

def problem_make (n = []) : 
    rows = [[True] * 9 for _ in range(9)]
    columns = [[True] * 9 for _ in range(9)]
    boxes = [[[True] * 9 for _ in range(3)] for _ in range(3)]
    zero_pos = []
    for i in range(9) :
        n.append(list(map(int,sys.stdin.readline().split())))
        for j, value in enumerate(n[i]) :
            if value == 0 : zero_pos.append((i,j))
            else :
                rows[i][value-1] = False
                columns[j][value-1] = False
                boxes[i//3][j//3][value-1] = False
    
    return rows, columns, boxes, n, zero_pos

# def find_answer(rows, columns, boxes, n) :
    # while(True) :
    #     count = 0
    #     for i in range(9) :
    #         for j in range(9) :
    #             if n[i][j] == 0 :
    #                 temp = [rows[i][k]&columns[j][k]&boxes[i//3][j//3][k] for k in range(9)]
    #                 if sum(temp) == 1 :
    #                     n[i][j] = temp.index(True) + 1
    #                     rows[i][n[i][j]-1] = False
    #                     columns[j][n[i][j]-1] = False
    #                     boxes[i//3][j//3][n[i][j]-1] = False
    #                 else : count += 1
    #     if count == 0 : return rows, columns, boxes, n

def find_answer1(rows, columns, boxes, n, zero_pos) :
    while(len(zero_pos)) :
        c_zero_pos = zero_pos.copy()
        for (i, j) in c_zero_pos :
            temp = []
            for k in range(9) :
                if rows[i][k]&columns[j][k]&boxes[i//3][j//3][k] == True : temp.append(k)
            if len(temp) == 1 :
                n[i][j] = temp[0] + 1
                rows[i][temp[0]] = columns[j][temp[0]] = boxes[i//3][j//3][temp[0]] = False
                zero_pos.remove((i,j))
        if len(zero_pos) == len(c_zero_pos) :
            break

    return rows, columns, boxes, n, zero_pos

def find_backtracking(rows, columns, boxes, n, zero_pos) :
    c_zero_pos = zero_pos.copy()
    (i, j) = c_zero_pos[0]
    temp = []
    for k in range(9) :
        if rows[i][k]&columns[j][k]&boxes[i//3][j//3][k] == True : temp.append(k)
    if len(temp) == 0 : return rows, columns, boxes, n, False
    for k in temp :
        n[i][j] = k + 1
        rows[i][k] = columns[j][k] = boxes[i//3][j//3][k] = False            
        zero_pos.remove((i,j))
        # print(zero_pos)
        if len(zero_pos) == 0 : return rows, columns, boxes, n, True
        else : rows, columns, boxes, n, tf = find_backtracking(rows, columns, boxes, n, zero_pos)
        if tf == True : return rows, columns, boxes, n, True
        zero_pos = c_zero_pos.copy()
        n[i][j] = 0
        rows[i][k] = columns[j][k] = boxes[i//3][j//3][k] = True
    return rows, columns, boxes, n, False

def main() :
    rows, columns, boxes, n, zero_pos = problem_make()
    rows, columns, boxes, n, zero_pos = find_answer1(rows, columns, boxes, n, zero_pos)
    if not len(zero_pos) == 0 :
        rows, columns, boxes, n, tf = find_backtracking(rows, columns, boxes, n, zero_pos)
    
    for i in n :
        sys.stdout.write(" ".join(map(str,i))+"\n")

if __name__=="__main__" :
    main()