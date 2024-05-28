class Trie:

    def __init__(self):
        self.next = [None for i in range(26)]
        self.end = False

    def insert(self, word: str) -> None:
        if word:
            if not self.next[ord(word[0])-97]:
                self.next[ord(word[0])-97] = Trie()
            self.next[ord(word[0])-97].insert(word[1:])
        else:
            self.end = True

    def search(self, word: str) -> bool:
        if word:
            if self.next[ord(word[0])-97]:
                return self.next[ord(word[0])-97].search(word[1:])
            else:
                return False
        else:
            return self.end

    def startsWith(self, prefix: str) -> bool:
        if prefix:
            if self.next[ord(prefix[0])-97]:
                return self.next[ord(prefix[0])-97].startsWith(prefix[1:])
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)