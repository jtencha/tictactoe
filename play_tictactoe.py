from TTTPlayer import TTTPlayer
from board_operations import gameOver, printBoard
from db_operations import savetoDB

# Start game
def play_tictactoe(p1,p2,quiet=False,training=False,num_games=1):

    for num_game in range(num_games):
        # Make new board as 9 dimension vector
        ttt_board = [0]*9
        #print(ttt_board)

        player1 = TTTPlayer(p1)
        player2 = TTTPlayer(p2)
        player1_history = []
        player2_history = []

        turn = 0
        while True:

            #Player 1 makes a move
            if turn % 2 == 0:
                # Determine move
                current_move = player1.makeMove()
                #print("Player One made move at --> " + str(current_move))
                player1.ttt_board[current_move] = 1
                player2.ttt_board[current_move] = -1
                # Keep official board up to date
                ttt_board[current_move] = 1
                printBoard(ttt_board)
            #Player 2 makes a move
            else:
                current_move = player2.makeMove()
                #print("Player Two made move at --> " + str(current_move))
                player2.ttt_board[current_move] = 1
                player1.ttt_board[current_move] = -1
                # Keep official board up to date
                ttt_board[current_move] = -1
                printBoard(ttt_board)

            if training:
                # Keep board history for later AI training
                player1_history.append(list(player1.ttt_board))
                player2_history.append(list(player2.ttt_board))

            #Check the results
            isOver, p1_result, p2_result = gameOver(ttt_board)
            if isOver:
                print("Turns:",turn+1)
                printBoard(ttt_board)
                #print(player1_history)
                #print(player2_history)

                # Record results in database for future AI training
                savetoDB([(p1,p1_result, player1_history),(p2, p2_result, player2_history)])
                # Game is over
                break
            else:
                turn += 1



# Do command line options to set players
# Run this when called from CLI
if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--P1", help="Type of Player 1 (0=Random, 1=Rules, 2=AI, 3=USER)",type=int, default=1)
    parser.add_argument("--P2", help="Type of Player 2 (0=Random, 1=Rules, 2=AI, 3=USER)",type=int, default=1)
    parser.add_argument("--quiet", help="Used when running similation games",action="store_true", default=False)
    parser.add_argument("--training", help="Used when running similation games",action="store_true", default=False)
    parser.add_argument("--num_games", help="Number of games to run",type=int, default=1)

    args = parser.parse_args()
    play_tictactoe(args.P1, args.P2, args.quiet, args.training, args.num_games)
