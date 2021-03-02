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
main = open("Inputs\\sudoku-3m.csv")
i = 2
c = 0
for single in main:
    
    if str(i)!=sys.argv[1]:
        i+=1
        continue

    n = open("Inputs\\input.txt", "w")

    single = single.split(",")[1]

    for ind in range(9):
        for j in range(9):
            if(single[ind*9+j] != '.'):
                n.write(single[ind*9+j])
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
