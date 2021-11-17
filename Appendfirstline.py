import os
import re

def main() :
    curr_path = os.path.dirname(os.path.abspath(__file__))
    file_list = os.listdir(curr_path)
    print(curr_path)
    print(file_list)
    for i in file_list :
        if i[-2:] != "py" : 
            continue ################## 새로 넣은 문구. 확인 후 돌릴 것!
        with open(i, 'r+', encoding='utf-8') as fp :
            file_text = fp.read()
            if file_text.startswith("# https://www.acmicpc.net/problem/") : continue
            else :
                fp.seek(0)
                try:
                    fp.write("# https://www.acmicpc.net/problem/"+re.findall(r'\d+',i)[0] + '\n' + file_text)
                except:
                    continue

if __name__=="__main__" :
    main()