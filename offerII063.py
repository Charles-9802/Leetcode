# hashset 遍历速度快
class Solution:
    def replaceWords(self, dictionary, sentence: str):
        res = []
        sentence = sentence.split(" ")
        hashset = set(dictionary)
        for ch in sentence:
            res.append(ch)
            for i in range(len(ch)):
                if ch[:i] in hashset:
                    res.pop()
                    res.append(ch[:i])
                    break
        return " ".join(res)


def main():
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    A = Solution()
    print(A.replaceWords(dictionary, sentence))


if __name__== "__main__":
    main()
