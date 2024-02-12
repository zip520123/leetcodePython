# Design Tic-Tac-Toe
# O(1), O(n)
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.p1Rows = defaultdict(int)
        self.p1Cols = defaultdict(int)
        self.p1Diag = defaultdict(int)
        self.p1AntiDiag = defaultdict(int)
        self.p2Rows = defaultdict(int)
        self.p2Cols = defaultdict(int)
        self.p2Diag = defaultdict(int)
        self.p2AntiDiag = defaultdict(int)

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.p1Rows[row] += 1
            if self.p1Rows[row] == self.n: return 1
            self.p1Cols[col] += 1
            if self.p1Cols[col] == self.n: return 1
            self.p1Diag[row-col] += 1
            if self.p1Diag[row-col] == self.n: return 1
            self.p1AntiDiag[row+col] += 1
            if self.p1AntiDiag[row+col] == self.n: return 1
        else:
            self.p2Rows[row] += 1
            if self.p2Rows[row] == self.n: return 2
            self.p2Cols[col] += 1
            if self.p2Cols[col] == self.n: return 2
            self.p2Diag[row-col] += 1
            if self.p2Diag[row-col] == self.n: return 2
            self.p2AntiDiag[row+col] += 1
            if self.p2AntiDiag[row+col] == self.n: return 2
        return 0
