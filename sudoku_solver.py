import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import time
import sys
from print_board import print_board
from validation_check import check_valid
from candidate_handler import candidates, candidates_update
from cells_seen import cells_seen
from solver import solver
from init_board import init_board

#file_name = input("Please enter the file location: ")
grid = ""
#enter input location
main = open("Inputs\\main.txt")
i = 1
c = 0
for single in main:
    
    if str(i)!=sys.argv[1]:
        i+=1
        continue
    
    symtest = np.zeros((9,9))

    n = open("Inputs\\input.txt", "w")
    for ind in range(9):
        for j in range(9):
            if(single[ind*9+j] != '.'):
                n.write(single[ind*9+j])
                symtest[ind][j] = 1
                c+=1
                n.write('|')
            else:
                n.write('0')
                n.write('|')
    n.close()

    f = open("Inputs\\input.txt", "r")
    for line in f:
        for num in line.split('|')[:-1]:
            if(int(num) < 10):
                grid+=str(num)
    
    t1 = time.time()
    board,square_pos = init_board(grid)
    print_board(board)
    
    f = open('Output/count.txt'.format(i), 'w')
    f.write(f"The Count is {c}\n")
    f.write(f"{t1}\n")

    print(symtest)
    print(np.rot90(symtest))

    if np.array_equal(symtest, np.rot90(symtest)):
        f.write(f"The Input is 90 Degree Symmetric.\n")

    if np.array_equal(symtest, np.rot90(np.rot90(symtest))):
        f.write(f"The Input is 180 Degree Symmetric.\n")

    f.close()
    f = open('Output/log.txt'.format(i), 'w')
    f.write('Log Start\n')
    f.close()
    #check validity before solving it
    if check_valid(board):
        cands = candidates(board)
        print(cands)
        solver(board,cands,square_pos)
    else:
        print("The board is not valid!")
    
    break
