class Solution:
    def strToInt(self, str: str) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        count = 0
        flag = 1
        i = 0
        str = str.strip()
        if not str:
            return 0
        if str[i] in "-+":
            if str[i] == "-":
                flag = -1
            i += 1
        for j in str[i:]:
            if j not in "0123456789":
                break
            count = count * 10 + int(j)
        count = flag * count
        if count > INT_MAX:
            return INT_MAX
        elif count < INT_MIN:
            return INT_MIN
        else:
            return count


def main():
    str = " "
    A = Solution()
    print(A.strToInt(str))


if __name__ == "__main__":
    main()
