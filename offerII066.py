class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def insert(self, key: str, val: int) -> None:
        self.dic[key] = val

    def sum(self, prefix: str) -> int:
        n = len(prefix)
        count = 0
        for ch in self.dic.keys():
            if ch[0:n] == prefix:
                count += self.dic[ch]
        return count


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)