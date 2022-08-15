class Solution:
    def minimumLengthEncoding(self, words):
        hashset = set()
        for word in words:
            hashset.add(word)
        for i in range(len(words)):
            for j in range(1, len(words[i])):
                if words[i][j:] in hashset:
                    hashset.remove(words[i][j:])
        ans = 0
        for ch in hashset:
            ans += len(ch) + 1
        return ans


A = Solution()
print(A.minimumLengthEncoding(words=["time", "me", "bell"]))
print(A.minimumLengthEncoding(["me", "time"]))
print(A.minimumLengthEncoding(["ctxdic", "c"]))
