#prints the sudoku board
def print_board(board):
    boardprint = board.copy()
    boardprint.columns = range(1,10)
    boardprint.index = ["A","B","C","D","E","F","G","H","I"]
    # sns.heatmap(board,annot=True,linecolor="k")
    print(boardprint)