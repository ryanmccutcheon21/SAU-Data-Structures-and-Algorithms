"""
7. Knight’s travails
In this project, we will understand two algorithms in action – BFS and DFS. BFS
stands for Breadth-First Search and utilizes the Queue data structure to find the
shortest path. Whereas, DFS refers to Depth-First Search and traverses Stack data
structures.
For starters, you will need a data structure similar to binary trees. Now, suppose
that you have a standard 8 X 8 chessboard, and you want to show the knight’s
movements in a game. As you may know, a knight’s basic move in chess is two
forward steps and one sidestep. Facing in any direction and given enough turns, it
can move from any square on the board to any other square.
If you want to know the simplest way your knight can move from one square (or
node) to another in a two-dimensional setup, you will first have to build a function
like the one below.
 knight_plays([0,0], [1,2]) == [[0,0], [1,2]]
 knight_plays([0,0], [3,3]) == [[0,0], [1,2], [3,3]]
 knight_plays([3,3], [0,0]) == [[3,3], [1,2], [0,0]]
Furthermore, this project would require the following tasks:
 Creating a script for a board game and a night
 Treating all possible moves of the knight as children in the tree structure
 Ensuring that any move does not go off the board
 Choosing a search algorithm for finding the shortest path in this case
 Applying the appropriate search algorithm to find the best possible move from the
starting square to the ending square.
"""

from collections import deque

class Chessboard:
    def __init__(self):
        self.board_size = 8
        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]

    def is_valid_move(self, x, y):
        return 0 <= x < self.board_size and 0 <= y < self.board_size

    def knight_plays(self, start, end):
        queue = deque()
        queue.append([start])
        visited = set()
        moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

        while queue:
            path = queue.popleft()
            current_position = path[-1]

            if current_position == end:
                return path

            if current_position not in visited:
                visited.add(current_position)

                for move in moves:
                    new_x = current_position[0] + move[0]
                    new_y = current_position[1] + move[1]

                    if self.is_valid_move(new_x, new_y):
                        new_path = list(path)
                        new_path.append((new_x, new_y))
                        queue.append(new_path)

        return None

# Testing the implementation
chessboard = Chessboard()
start = (0, 0)
end = (1, 2)
result = chessboard.knight_plays(start, end)
print(f"Knight's path from {start} to {end}: {result}")
