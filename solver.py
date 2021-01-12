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
    else:
        print("COMPLETE!!!!!\n")
        if check_valid(board):
            board.columns = np.arange(1,10)
            board.index = np.arange(1,10)
            print_board(board)
            print("\n")
            print(f"{(board == '.').sum().sum()} Missing Elements Left in The Board!\n")
            f = open('Output/log.txt', "r")
            checks = ['Single Candidate', 'Y-Wing', 'XYZ-Wing', 'X-Wing', 'Swordfish', 'Singles-Chains', 'Pointing Pairs',
                    'Naked Pairs', 'Naked Triples', 'Naked Quads', 'Hidden Singles', 'Hidden Pairs', 'Hidden Triples', 'Hidden Quads']
            counts = {}
            for line in f:
                for check in checks:
                    if check in line:
                        if check in counts.keys():
                            counts[check] += 1
                        else:
                            counts[check] = 1

            f = open('Output/count.txt', 'w')
            for key in counts.keys():
                f.write(f"{key} has occured {counts[key]} times\n")
        else:
            print_board(board)
            print("Error")
        sys.exit(0)
