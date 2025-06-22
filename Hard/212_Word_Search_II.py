class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

    def addWord(self, word):
        curr = self

        for c in word:
            if(c not in curr.children):
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.endWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        rows, cols = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):
            if(r < 0 or r == rows or
               c < 0 or c == cols or
               (r, c) in visited or
               board[r][c] not in node.children):
               return

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if(node.endWord):
                res.add(word)

            diff = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            for dr, dc in diff:
                dfs(r + dr, c + dc, node, word)

            visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)