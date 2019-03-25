import platform, os

from spell_checker import search
from trie import Trie

WORDS_PATH = "/usr/share/dict/words"

if platform.system().lower() in 'linux':
    WORDS = os.path.abspath(WORDS_PATH)
else:
    raise SystemError("linux devices only")

def create_tree(words: str=WORDS_PATH):
    tree = Trie()
    file = open(words, 'r')
    list(map(lambda w: tree.insert(w), file.readlines()[:5000]))
    file.close()
    return tree


if __name__ == "__main__":
    tree = create_tree()

    word = input("type the word:")

    results = search(tree, word)
    print(results)
