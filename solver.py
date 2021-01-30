from single_candidate import single_cand
from hidden_singles import hidden_singles
from hidden_pairs_triples_quads import hidden_pairs_triples, hidden_quads
from naked_pairs_triples_quads import naked_pairs_triples, naked_quads
from pointing_pairs import pointing_pairs
from box_line import box_line
from x_wing import x_wing
from y_wing import y_wing
from singles_chains import singles_chains
from xyz_wing import xyz_wing
from swordfish import swordfish
from print_board import print_board
from validation_check import check_valid
from brute_force import Brute_Force
import sys
import numpy as np
import time as time
#%% SOLVER FUNCTION
def solver(board,cands,square_pos):
    #run strategies in listed order as long as the board has empty cells (".")
    if (board==".").any().any():
        single_cand(board,cands,square_pos)
        hidden_singles(board,cands,square_pos)
        naked_pairs_triples(board,cands,square_pos)
        hidden_pairs_triples(board,cands,square_pos)
        pointing_pairs(board,cands,square_pos)
        box_line(board,cands,square_pos)
        naked_quads(board,cands,square_pos)
        hidden_quads(board,cands,square_pos)
        x_wing(board,cands,square_pos)
        y_wing(board,cands,square_pos)
        singles_chains(board,cands,square_pos)
        xyz_wing(board,cands,square_pos)
        swordfish(board,cands,square_pos)
        s = Brute_Force()
        s.load_puzzle_from_file(board)
        get_time = s.solve()
        for i in range(9):
            for j in range(9):
                board.iloc[i,j] = s.puzzle[i*9+j]
    else:
        print("COMPLETE!!!!!\n")
        if check_valid(board):
            board.columns = np.arange(1,10)
            board.index = np.arange(1,10)
            print_board(board)
            print("\n")
            Difficulty = "Easy"
            print(f"{(board == '.').sum().sum()} Missing Elements Left in The Board!\n")
            f = open('Output/log.txt', "r")
            checks = ['Single Candidate', 'Y-Wing', 'XYZ-Wing', 'X-Wing', 'Swordfish', 'Singles-Chains', 'Pointing Pairs',
                    'Naked Pairs', 'Naked Triples', 'Naked Quads', 'Hidden Singles', 'Hidden Pairs', 'Hidden Triples', 'Hidden Quads' , 'Naked Singles']
            counts = {}
            for line in f:
                for i in range(len(checks)):
                    if checks[i] in line:
                        if i in [1,2,3,4]:
                            Difficulty = "Hard"
                        elif i not in [1, 2, 3, 4, 0, 10, 14] and Difficulty != "Hard":
                            Difficulty = "Medium"
                        if checks[i] in counts.keys():
                            counts[checks[i]] += 1
                        else:
                            counts[checks[i]] = 1

            f = open('Output/count.txt', 'a')
            for key in counts.keys():
                f.write(f"{key} has occured {counts[key]} times\n")
            f.write(f"The Difficulty level is {Difficulty}\n")
            t1 = time.time()
            f.write(f"{t1}\n")
            f.close()
        else:
            print_board(board)
            print("Error")
        sys.exit(0)
