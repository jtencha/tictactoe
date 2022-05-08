from itertools import combinations

# Check if game is over
def gameOver(ttt_board_in):

    winner = 0
    poss_wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    #print(poss_wins,len(poss_wins))

    # Three in a row?
    one_indexes = [i for i in range(len(ttt_board_in)) if ttt_board_in[i] == 1]
    one_combos = list(combinations(one_indexes,3))
    #print([x for x in one_combos])
    for one_combo in one_combos:
        #for poss_win in poss_wins:
            #print(one_combo,poss_win)
            if one_combo in poss_wins:
                print("Winner 1", one_combo)
                #print(ttt_board_in)
                return True, 1, -1

    neg_one_indexes = [i for i in range(len(ttt_board_in)) if ttt_board_in[i] == -1]
    neg_one_combos = list(combinations(neg_one_indexes,3))
    #print([x for x in neg_one_combos])
    for neg_one_combo in neg_one_combos:
        #for poss_win in poss_wins:
            #print(neg_one_combo,poss_win)
            if neg_one_combo in poss_wins:
                print("Winner -1", neg_one_combo)
                #print(ttt_board_in)
                return True, -1, 1

    # Board full but no winner?
    zero_indexes = [i for i in range(len(ttt_board_in)) if ttt_board_in[i] == 0]
    if zero_indexes == []:
        print("Board Full - Tie")
        print(ttt_board_in)
        return True, 0, 0

    return False, 0, 0


def printBoard(ttt_board_in):
    print("\n {0} | {1} | {2}".format(ttt_board_in[0],ttt_board_in[1],ttt_board_in[2]))
    print("-----------")
    print(" {0} | {1} | {2}".format(ttt_board_in[3],ttt_board_in[4],ttt_board_in[5]))
    print("-----------")
    print(" {0} | {1} | {2}\n".format(ttt_board_in[6],ttt_board_in[7],ttt_board_in[8]))
