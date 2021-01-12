
from candidate_handler import candidates_update
#interdependent modules, it has to be imported like below,otherwise it wont work
import solver as solver

#%% SINGLE CANDIDATES
def single_cand(board,cands,square_pos):
    ischanged = 0
    for row in range(9):
        for col in range(9):
            if board.iloc[row,col] == ".":
                cand = cands.iloc[row,col]
                # cand = int(cands.iloc[row,col][0])
                try:
                    lenx = len(cand)
                    if lenx == 1:
                        ischanged = 1
                        f = open('Output/log.txt','a')
                        f.write(f"R{row+1}C{col+1}={cand[0]} : Single Candidate\n")
                        print(f"R{row+1}C{col+1}={cand[0]} : Single Candidate")
                        f.close()
                        board.iloc[row,col] = cand[0]
                        cands = candidates_update(cands,row,col,cand[0],square_pos)
                except:
                    ischanged = 1
                    f = open('Output/log.txt','a')
                    f.write(f"R{row+1}C{col+1}={cand} : Single Candidate (except)\n")
                    print(f"R{row+1}C{col+1}={cand} : Single Candidate (except)")
                    f.close()
                    board.iloc[row,col] = cand
                    cands = candidates_update(cands,row,col,cand,square_pos)
    if ischanged:
        solver.solver(board,cands,square_pos)                 
    