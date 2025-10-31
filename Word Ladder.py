from collections import deque

def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    
    wordList = set(wordList)
    queue = deque([(beginWord, 1)])
    
    while queue:
        word, steps = queue.popleft()
        if word == endWord:
            return steps
        
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordList:
                    wordList.remove(next_word)
                    queue.append((next_word, steps + 1))
    
    return 0

print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
