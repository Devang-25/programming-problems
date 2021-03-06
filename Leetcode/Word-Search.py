class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board == [] or board == None:
            if word == "" or word == None:
                return True
            else:
                return False
            
        self.visited = set()
        
        def is_valid_space(grid, row, col):
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0 or (row, col) in self.visited:
                return False
            else:
                return True
            
        def search(grid, row, col, word, index):
            if not is_valid_space(grid, row, col):
                return False
            if index == len(word) - 1 and word[index] == grid[row][col]:
                return True
            if word[index] != grid[row][col]:
                return False
            
            self.visited.add((row, col))
            
            left = search(grid, row, col - 1, word, index + 1)
            right = search(grid, row, col + 1, word, index + 1)
            down = search(grid, row + 1, col, word, index + 1)
            up = search(grid, row - 1, col, word, index + 1)
            found = left or right or down or up
            if not found:
                self.visited.remove((row, col))
            return found
        
        
        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if board[row][col] == word[0] and search(board, row, col, word, 0):
                    return True
        return False
        
