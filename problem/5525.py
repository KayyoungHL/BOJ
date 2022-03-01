import sys

# def main():
#     k = int(sys.stdin.readline())
#     n = int(sys.stdin.readline())
#     string = sys.stdin.readline().strip()

#     stack = ["0"]
#     iostack = 0
#     ans = 0
#     for i in string:
#         if i == "I":
#             if stack[-1] == "I":
#                 stack = ["0", "I"]
#                 ans += iostack - k + 1 if iostack >= k else 0
#                 iostack = 0
#             elif stack[-1] == "0":
#                 stack.append(i)
#             else:
#                 stack.append(i)
#                 iostack += 1
#         else:
#             if stack[-1] == "I":
#                 stack.append(i)
#             else:
#                 stack = ["0"]
#                 ans += iostack - k + 1 if iostack >= k else 0
#                 iostack = 0
#         # print(stack, iostack, ans)
    
#     ans += iostack - k + 1 if iostack >= k else 0
#     print(ans)

# def main():
#     k = int(sys.stdin.readline())
#     n = int(sys.stdin.readline())
#     string = sys.stdin.readline().strip().replace("IO", "X")
#     # print(string)
#     xstack = 0
#     ans = 0
#     for i in string:
#         if i == "X":
#             xstack += 1
#         elif i == "I":
#             ans += xstack - k + 1 if xstack >= k else 0
#             xstack = 0
#         else:
#             ans += xstack - k if xstack-1 >= k else 0
#             xstack = 0
    
#     ans += xstack - k if xstack-1 >= k else 0
#     print(ans)

def main():
    k = int(sys.stdin.readline())-1
    _ = int(sys.stdin.readline())
    strings = [len(i)-1 for i in sys.stdin.readline().strip().replace("IO", "X").replace("XI","XXO").replace("I","O").split("O") if i != ""]
    ans = 0
    for i in strings:
        ans += i-k if i > k else 0
    print(ans)

if __name__ == "__main__":
    main()