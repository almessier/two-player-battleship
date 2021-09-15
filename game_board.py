
class GameBoard:
    def __init__(self):
        self.name = 'game_board'
        self.length = 20
        self.width = 20
        self.grid = self.create_grid()

    def create_grid(self):
        grid = [
            ['[]' for x in range(self.width)]
            for y in range(self.length)]
        return grid

    def print_grid(self, grid):
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                print(grid[x][y], end='  ')
            print()
