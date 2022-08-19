class Node:

    def __init__(self):
        self.is_word = False
        self.children = [None for _ in range(26)]


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not node.children[index]:
                node.children[index] = Node()

            node = node.children[index]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.find(word)
        return node is not None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) is not None

    def find(self, word: str) -> Node:
        node = self.root
        for ch in word:
            index = ord(ch) - ord("a")
            if not node.children[index]:
                return None
            node = node.children[index]
        return node



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)