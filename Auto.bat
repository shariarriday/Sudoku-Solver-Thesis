FOR /L %%A IN (1,6,3000000) DO (
  C:/Users/User/.conda/envs/ml-tf-prac/python.exe "g:/Actual Shits/Thesis/Sudoku Solver/sudoku_solver.py" %%A
  copy Output\count.txt Output\count%%A.txt
  copy Output\log.txt Output\log%%A.txt
)
pause