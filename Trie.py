def build_trie(*words):
    sortedWords2 = sorted(words, key=len)
    sortedWords = sortedWords2[::-1]
    trie = {}
    for i in range(len(sortedWords)):
        trie2 = trie
        for j in range(1,len(sortedWords[i])+1):
            if j == len(sortedWords[i]):
                trie2 = trie2.setdefault(sortedWords[i][0:j], None)
            else:
                trie2 = trie2.setdefault(sortedWords[i][0:j], {})
    return trie

print(build_trie("true", "trust"))