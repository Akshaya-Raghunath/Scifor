Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first

class Solution(object):
    def tictactoe(self, moves):
            win = [
            [(0,0),(0,1),(0,2)], [(0,0),(1,0),(2,0)],
            [(1,0),(1,1),(1,2)], [(0,1),(1,1),(2,1)],
            [(2,0),(2,1),(2,2)], [(0,2),(1,2),(2,2)],
            [(0,0),(1,1),(2,2)], [(0,2),(1,1),(2,0)]
        ]
      
            A = set(tuple(step) for step in moves[::2])
            B = set(tuple(step) for step in moves[1::2])
              
            for win_case in win:
                if win_case[0] in A and win_case[1] in A and win_case[2] in A: return "A"
                if win_case[0] in B and win_case[1] in B and win_case[2] in B: return "B"
                  
            if len(moves) == 9: return "Draw"
            else: return "Pending"
