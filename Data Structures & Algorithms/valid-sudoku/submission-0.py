class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cs=[set() for _ in range(9)]
        rs=[set() for _ in range(9)]
        bs=[set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                ch=board[r][c]
                if ch=='.':
                    continue
                bn=3*(r//3)+ c//3
                if ch in rs[r] or ch in cs[c] or ch in bs[bn]:
                    return False
                rs[r].add(ch)
                cs[c].add(ch)
                bs[bn].add(ch)
        return True