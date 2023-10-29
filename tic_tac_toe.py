import random

class TTT_cs170_judge:
    def __init__(self):
        self.board = []

    def create_board(self, n):
        for i in range(n):
            row = []
            for j in range(n):
                row.append('-')
            self.board.append(row)

    def display_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def is_winner(self, player):
        # Check rows
        for row in self.board:
            if all([cell == player for cell in row]):
                return True
        # Check columns
        for col in range(len(self.board)):
            if all([self.board[row][col] == player for row in range(len(self.board))]):
                return True
        # Check diagonals
        if all([self.board[i][i] == player for i in range(len(self.board))]):
            return True
        if all([self.board[i][len(self.board) - i - 1] == player for i in range(len(self.board))]):
            return True
        return False

    def is_board_full(self):
        return all([cell in ['X', 'O'] for row in self.board for cell in row])

class Player_1:
    def __init__(self, judge):
        self.board = judge.board

    def my_play(self):
        while True:
            row, col = map(int, input("Enter the row and column numbers separated by space: ").split())
            if 1 <= row <= len(self.board) and 1 <= col <= len(self.board[0]):
                self.board[row - 1][col - 1] = 'X'
                break
            else:
                print("Wrong coordination!")

class Player_2:
    def __init__(self, judge):
        self.judge = judge
        self.board = judge.board

    def my_play(self):
        if self.judge.is_board_full():
            return  

        best_move = self.minimax(self.board, 0, -float('inf'), float('inf'), True)
        row, col = best_move[1], best_move[2]
        self.board[row][col] = 'O'

    def minimax(self, board, depth, alpha, beta, maximizing):
        if self.judge.is_winner('X'):
            return -1, None, None  
        if self.judge.is_winner('O'):
            return 1, None, None  
        if self.judge.is_board_full():
            return 0, None, None  # tie

        if maximizing:
            best_score = -float('inf')
            best_move = None

            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col] == '-':
                        board[row][col] = 'O'
                        score = self.minimax(board, depth + 1, alpha, beta, False)
                        board[row][col] = '-'

                        if score[0] > best_score:
                            best_score = score[0]
                            best_move = (best_score, row, col)

                        alpha = max(alpha, best_score)

                        if beta <= alpha:
                            break  # Prune the branch

            return best_move
        else:
            best_score = float('inf')
            best_move = None

            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col] == '-':
                        board[row][col] = 'X'
                        score = self.minimax(board, depth + 1, alpha, beta, True)
                        board[row][col] = '-'

                        if score[0] < best_score:
                            best_score = score[0]
                            best_move = (best_score, row, col)

                        beta = min(beta, best_score)

                        if beta <= alpha:
                            break  # Prune the branch

            return best_move

def game_loop():
    n = 3  # Board size
    game = TTT_cs170_judge()
    game.create_board(n)
    player1 = Player_1(game)
    player2 = Player_2(game)
    starter = random.randint(0, 1)
    win = False
    if starter == 0:
        print("Player 1 starts.")
        game.display_board()
        while not win:
            player1.my_play()
            win = game.is_winner('X')
            game.display_board()
            if win:
                print("Player 1 wins!")
                break
            if game.is_board_full():
                print("It's a tie!")
                break
            player2.my_play()
            win = game.is_winner('O')
            game.display_board()
            if win:
                print("Player 2 wins!")
                break
            if game.is_board_full():
                print("It's a tie!")
                break
    else:
        print("Player 2 starts.")
        game.display_board()
        while not win:
            player2.my_play()
            win = game.is_winner('O')
            game.display_board()
            if win:
                print("Player 2 wins!")
                break
            if game.is_board_full():
                print("It's a tie!")
                break
            player1.my_play()
            win = game.is_winner('X')
            game.display_board()
            if win:
                print("Player 1 wins!")
                break
            if game.is_board_full():
                print("It's a tie!")
                break

# Uncomment the following line to play the game
# game_loop()

