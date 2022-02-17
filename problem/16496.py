def main():
    n = input()
    ans = "".join(
        sorted(
            input().split(),
            key=lambda x:(x*9)[:10],
            reverse=True
        )
    )
    return "0" if ans[0] == "0" else ans

if __name__ == "__main__":
    print(main())