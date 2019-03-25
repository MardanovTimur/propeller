
class Trie:
    childrens: dict = {}
    word: str = None

    def insert(self, word: str):
        sub_trie = self
        for l in word:
            if l not in sub_trie.childrens:
                sub_trie.childrens[l] = Trie()
            sub_trie = sub_trie.childrens[l]
        # save word in the last element of trie
        sub_trie.word = word
