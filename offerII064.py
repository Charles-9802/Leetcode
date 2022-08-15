class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map =[]

    def buildDict(self, dictionary) -> None:
        self.map.append(dictionary)

    def search(self, searchWord: str) -> bool:
        def bijiao(ch, searchWord):
            if len(ch) != len(searchWord):
                return 0
            else:
                count = 0
                for i in range(len(ch)):
                    if ch[i] != searchWord[i]:
                        count += 1
                if count == 1:
                    return 1
                else:
                    return 0

        res = []
        for ch in self.map[0]:
            temp = bijiao(ch, searchWord)
            res.append(temp)
        if 1 in res:
            return True
        else:
            return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)