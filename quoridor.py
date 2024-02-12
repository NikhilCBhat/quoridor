import os
import getch

class Tile:
    def __init__(self, is_square=False, has_wall=False):
        self.is_square = is_square
        self.has_wall = has_wall

class GameBoard:
    def __init__(self, size=13):
        self.board = [[Tile(j % 2 == 0 and i % 2 == 0) for i in range(size)] for j in range(size)]
        self.size = size

class View:

    def draw_board(self, board: GameBoard, player_positions, clear=True):
        if clear:
            os.system('clear')
        view = [["" for _ in range(board.size)] for _ in range(board.size)]
        for i, row in enumerate(board.board):
            for j, tile in enumerate(row):
                view[i][j] = self.draw_tile(tile)
    
        for (i, j), c in zip(player_positions, ("P", "Q")):
            view[i][j] = c

        print("Quoridor:")
        for row in view:
            print("".join(row))
        print()

    def draw_tile(self, tile: Tile):
        if tile.has_wall:
            return "W"
        if tile.is_square:
            return "S"
        return "X"

class Controller:

    char_to_delta = {
        "a": (0, -2),
        "d": (0, 2),
        "w": (-2, 0),
        "s": (2, 0)
    }

    def __init__(self) -> None:
        self.board = GameBoard()
        self.view = View()
        self.player_positions = [[0, 6], [12, 6]]
        self.player_turn = 0
    
    def draw(self):
        self.view.draw_board(self.board, self.player_positions)
    
    def play(self):
        while True:
            for player_turn in (0, 1):
                self.draw()
                move = self.get_move(player_turn)
                self.apply_move(move, player_turn)
    
    def get_move(self, player_turn):
        print(f"Player {player_turn} enter your move (wasd)")
        return getch.getch()
    
    def apply_move(self, move, turn):
        dx, dy = self.char_to_delta[move]
        cx, cy = self.player_positions[turn]
        nx, ny = dx + cx, dy + cy
        if 0 <= nx < 13 and 0 <= ny < 13:
            self.player_positions[turn] = (nx, ny) 
    
c = Controller()
c.play()
        
