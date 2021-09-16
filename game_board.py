
class GameBoard:
    def __init__(self):
        self.name = 'game_board'
        self.side_length = 20
        self.grid = self.create_grid()

    def create_grid(self):
        grid = [
            ['[ ]' for i in range(self.side_length)]
            for i in range(self.side_length)]
        return grid

    def print_grid(self, grid):
        print('     ', end='')
        alphabet = 'ABCDEFGHIJKLMNOPQRST'
        for letter in alphabet:
            print('', letter, end='   ')
        print()
        num = 1
        for y in range(len(grid)):
            if(len(str(num)) == 1):
                print('  ', num, end=' ')
            else:
                print(' ', num, end=' ')
            num += 1
            for x in range(len(grid[y])):
                print(grid[y][x], end='  ')
            print()
