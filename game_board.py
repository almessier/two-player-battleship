
class GameBoard:
    def __init__(self):
        self.name = 'game_board'
        self.length = 20
        self.width = 20
        self.grid = self.create_grid()

    def create_grid(self):
        grid = [
            [0 for x in range(self.width)]
            for y in range(self.length)]

        counter = 1
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                grid[x][y] += counter
                counter += 1
        return grid

    def print_grid(self, grid):
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if(len(str(grid[x][y])) == 1):
                    print(grid[x][y], end='    ')
                elif(len(str(grid[x][y])) == 2):
                    print(grid[x][y], end='   ')
                else:
                    print(grid[x][y], end='  ')
            print()
