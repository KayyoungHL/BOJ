# https://www.acmicpc.net/problem/1110
def main() :
    a = input()
    count = 1
    if len(a) == 1 :
        a = "0"+a
    b = "00"
    b = a[1] + str((int(a[0]) + int(a[1]))%10) # ex) "48" -> 12 -> "8" + "2"
    while b != a :
        c = b[1] # ex) "48" -> c = "8"
        b = c + str((int(b[0]) + int(b[1]))%10) # ex) "48" -> 12 -> "2" => "82"
        count += 1
    print(count)

if __name__=="__main__" :
    main()