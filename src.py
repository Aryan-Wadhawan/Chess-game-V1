# Board
# Pieces
# Turns
# movement

Board = [0] * 8

for i in range(len(Board)):
    Board[i] = ["__"] * 8


def print_board(Board):
    for i, row in enumerate(Board):
        print(8 - i, end = ":  ")
        for i, col in enumerate(row):
            print(col, end = " ")
        print("\n")
    print("    " + "a" + "  " + "b" + "  " + "c" + "  " + "d" + "  " + "e" + "  " + "f" + "  " + "g" + "  " + "h" + "  " )

print_board(Board)

white_pieces_map = {
    "wP": [(6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7)],
    "wH": [(7,1), (7,6)],
    "wB": [(7,2), (7,5)],
    "wR": [(7,0), (7,7)],
    "wQ": [(7,3)],
    "wK": [(7,4)]
}

black_pieces_map = {
    "bP": [(1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7)],
    "bH": [(0,1), (0,6)],
    "bB": [(0,2), (0,5)],
    "bR": [(0,0), (0,7)],
    "bQ": [(0,3)],
    "bK": [(0,4)]
}

# (0,0) -> a8
col_map = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7
}

def put_pieces(Board):
    # White pieces
    for piece, squares in white_pieces_map.items():
        for square in squares:
            x, y = square[0], square[1]
            Board[x][y] = piece

    # Black Pieces
    for piece, squares in black_pieces_map.items():
        for square in squares:
            x, y = square[0], square[1]
            Board[x][y] = piece

put_pieces(Board)
current_turn = 1

while(True):
    print_board(Board)
    print("")

    current_player = ""
    if current_turn % 2 == 1:
        current_player = "White"
    else:
        current_player = "Black"

    current_turn += 1

    print(current_player + " to move!")
    print("")

    starting_squares = input("Entre the square whole piece you'd like to move: ")
    start_x, start_y = starting_squares[0], starting_squares[1]
    start_x = col_map[start_x]
    start_y = 8 - int(start_y)
    start_x, start_y = start_y, start_x

    ending_square = input("Entre the square where  you'd like to move the piece to: ")
    end_x, end_y = ending_square[0], ending_square[1]
    end_x = col_map[end_x]
    end_y = 8 - int(end_y)
    end_x, end_y = end_y, end_x

    temp = Board[start_x][start_y]
    Board[start_x][start_y] = "  "
    Board[end_x][end_y] = temp