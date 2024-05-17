import random
import itertools
import collections
import time

N = 3

def getInvCount(arr):
    arr1 = []
    for y in arr:
        for x in y:
            arr1.append(x)
    arr = arr1
    inv_count = 0
    for i in range(N * N - 1):
        for j in range(i + 1, N * N):
            if (arr[j] and arr[i] and arr[i] > arr[j]):
                inv_count += 1
    return inv_count

def findXPosition(puzzle):
    # start from top-left corner of matrix
    for i in range(N):
        for j in range(N):
            if (puzzle[i][j] == 0):
                return i + 1

def isSolvable(puzzle):
    invCount = getInvCount(puzzle)
    if (N & 1):
        return not (invCount & 1)
    else:  # grid is even
        pos = findXPosition(puzzle)
        return not (invCount & 1) if (pos & 1) else (invCount & 1)

class Node:
    def __init__(self, puzzle, parent=None, action=None):
        self.puzzle = puzzle
        self.parent = parent
        self.action = action
        if self.parent is not None:
            self.g = parent.g + 1
        else:
            self.g = 0

    @property
    def score(self):
        return (self.g + self.h)

    @property
    def state(self):
        return str(self)

    @property
    def path(self):
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)

    @property
    def solved(self):
        return self.puzzle.solved

    @property
    def actions(self):
        return self.puzzle.actions

    @property
    def h(self):
        return self.puzzle.manhattan

    @property
    def f(self):
        return self.h + self.g

    def __str__(self):
        return str(self.puzzle)

class Solver:
    def __init__(self, start):
        self.start = start

    def solve(self):
        queue = collections.deque([Node(self.start)])
        seen = set()
        seen.add(queue[0].state)
        while queue:
            queue = collections.deque(sorted(list(queue), key=lambda node: node.f))
            node = queue.popleft()
            if node.solved:
                return node.path

            for move, action in node.actions:
                child = Node(move(), node, action)

                if child.state not in seen:
                    queue.appendleft(child)
                    seen.add(child.state)

class Puzzle:
    def __init__(self, board):
        self.width = len(board[0])
        self.board = board

    @property
    def solved(self):
        N = self.width * self.width
        return str(self) == ''.join(map(str, range(1, N))) + '0'

    @property
    def actions(self):
        def create_move(at, to):
            return lambda: self._move(at, to)

        moves = []
        for i, j in itertools.product(range(self.width), range(self.width)):
            direcs = {'R': (i, j - 1),
                      'L': (i, j + 1),
                      'D': (i - 1, j),
                      'U': (i + 1, j)}

            for action, (r, c) in direcs.items():
                if (
                    r >= 0
                    and c >= 0
                    and r < self.width
                    and c < self.width
                    and self.board[r][c] == 0
                ):
                    move = create_move((i, j), (r, c)), action
                    moves.append(move)
        return moves

    @property
    def manhattan(self):
        distance = 0
        for i in range(self.width):
            for j in range(self.width):
                if self.board[i][j] != 0:
                    x, y = divmod(self.board[i][j] - 1, self.width)
                    distance += abs(x - i) + abs(y - j)
        return distance

    def copy(self):
        board = [row[:] for row in self.board]
        return Puzzle(board)

    def _move(self, at, to):
        copy = self.copy()
        i, j = at
        r, c = to
        copy.board[i][j], copy.board[r][c] = copy.board[r][c], copy.board[i][j]
        return copy

    def pprint(self):
        for row in self.board:
            print(row)
        print()

    def __str__(self):
        return ''.join(map(str, self))

    def __iter__(self):
        for row in self.board:
            yield from row

# Example of use
board = [[0,3,8], [4,1,7], [2,6,5]]
if isSolvable(board):
    print("Solvable")
else:
    print("Not Solvable")
    print("Need to shuffle the board or enter a new board...")
    exit()
puzzle = Puzzle(board)
s = Solver(puzzle)
tic = time.perf_counter()
p = s.solve()
toc = time.perf_counter()

steps = 0
for node in p:
    print(node.action)
    node.puzzle.pprint()
    steps += 1

print("Total number of steps: " + str(steps))
print("Total amount of time in search: " + str(toc - tic) + " second(s)")
