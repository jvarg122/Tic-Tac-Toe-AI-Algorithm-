# Project 1 Report: Tic-Tac-Toe AI Algorithm Analysis

## **1. Introduction:**
To begin, all necessary parts were already implemented except the Player 2 class which I was responsible for modifying. The main focus of this project is the implementation of an AI algorithm to simulate an opponent in a game of Tic-Tac-Toe where ‘X’ and ‘O’ are marked vertically, horizontally, or diagonally on a 3x3 board. The importance of integrating AI into the Tic-Tac-Toe framework is to gain a basic understanding of game theory in a strategy-based environment and AI algorithm design (i.e., optimal decision-making). Particularly related to recursion (DFS), trees, and efficient performance.


## **2. Algorithm Description:**
The AI algorithm I have chosen is minimax. Its strengths are that it takes into account all the possible moves that players can take at any given time during the Tic-Tac-Toe game. However, minimax’s weakness is that it is computationally expensive. I was mindful of alpha-beta pruning itself, following the tips provided to decrease the run time of my_play code.
Because of this, I included Alpha Beta Pruning such that changes: 


`def minimax(self, board, depth, alpha, beta, maximizing):`

```
alpha = max(alpha, best_score)
if beta <= alpha:
break  # Prune the branch
```
```
beta = min(beta, best_score)

if beta <= alpha:
break
```
Compared with minimax, this algorithm is extremely beneficial, as it reduces the computation time, improving efficiency.

## **3. Example Scenario:**
In this specific game scenario, the initial board state where player 1 starts is:

```
- - -
- X -
- - -
```
my play() method checks if the game board is full. It either returns or calls minimax. minimax is used to find the best move for the AI. Within the two nested loops, it iterates over each row and column, simulating the AI move. If temporarily places ‘O’ in the empty cell, makes a recursive call to minimax, and then reverts back for future states to be evaluated. The AI evaluates the current board state by employing minimax (recursively) to find the optimal move from all possible moves (“-” on the diagram above).

**minimax takes parameters:**

| Parameter      | Description                                                     |            
| :---           |    :----:                                                       |
| board          | Current board state                                             |
| depth          | Current depth in the game tree. Shows number of moves considered|   
| alpha and beta | For alpha-beta pruning                                          |
| maximizing     | Indicates if AI is maximizing or minimizing                     |

Recursive depth-first search is used and there are three cases to consider. Each node in the tree structure represents a specific game state.

```
  if self.judge.is_winner('X'):
            return -1, None, None  
        if self.judge.is_winner('O'):
            return 1, None, None  
        if self.judge.is_board_full():
            return 0, None, None  # tie
```

-1 (lose), 0 (tie. The board is full), or 1 (win) is assigned based on how advantageous or disadvantageous the outcome of a sequence of moves is. Here, X is human while O is AI. It tries to minimize the possible loss for worst-case scenario (opponent) while maximizing the gain for best-case scenario (AI). After best_move is determined, the tic-tac-toe board is updated. AI’s best_move = (best_score, row, col), updating the tic-tac-toe board with “O”.

```
- - -
- X -
- - O
```
## **4. Conclusion:** 
The minimax algorithm was successfully implemented into the Tic-Tac-Toe AI project. Some key findings were that by comparison, alpha-beta pruning made the game much more optimal, spending less average time, passing all of the performance tests. In short, it provided valuable insights into AI concepts and application (re. optimization techniques). Future directions: Despite solving Tic-Tac-Toe with ease, complex games such as chess pose tougher challenges to adapt to. In designing the AI, it became clear that between the time complexity might be impractical in real-time for larger game boards where more possible moves have to be considered. For further improvements, I will need to explore alternative evaluation methods and can potentially refine the scalability.
