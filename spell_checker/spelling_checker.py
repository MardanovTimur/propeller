import os

from typing import Type

from trie.trie_module import Trie


UPPER_POINT = 1


def search(tree: Type[Trie],
           word: str,
           upperPoint: int=UPPER_POINT):
    distance = range(len(word) + 1)
    results = []
    for w in tree.childrens.keys():
        tree_search(tree.childrens[w], w, word, distance, results)
    return results


def tree_search(node: Type[Trie],
                letter: str,
                word: str,
                p_distance: [list, tuple],
                results: list):

    columns = len(word) + 1
    distance = [p_distance[0] + 1]

    # ~ Levenshtein
    for column in range(1, columns):
        insert_cost = distance[column - 1] + 1
        delete_cost = p_distance[column] + 1
        replace_cost = p_distance[column - 1] if word[column - 1] == letter \
            else p_distance[column - 1] + 1
        distance.append(min(insert_cost, delete_cost, replace_cost))

    if distance[-1] <= UPPER_POINT and node.word is not None:
        results.append((node.word, distance[-1]))

    if min(distance) <= UPPER_POINT:
        for letter in node.childrens:
            tree_search(node.childrens[letter], letter, word,
                            distance, results)
