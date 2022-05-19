import random

def immediate(self, combo, type):
    count = 0
    x = 0
    zIndex = -1
    #check for immediate wins/losses- two slots with an empty one
    while x < 3:
        if self.ttt_board[combo[x]] == type:
            count += 1
        elif self.ttt_board[combo[x]] == 0:
            count += 100
            zIndex = combo[x]

        x += 1

    if count == 102:
        #print("Made move for three")
        return zIndex
    else:
        return -1

def next_to(self, combo, type):
    zero_indexes = [i for i in range(len(self.ttt_board)) if self.ttt_board[i] == 0]
    next_to_middle = [1, 3, 5, 7]
    corners = [0, 2, 6, 8]

    #[0, 1, 2], [3, 4, 5]
    count = 0
    x = 0
    zIndex = []
    while x < 3:
        if self.ttt_board[combo[x]] == type:
            count += 1
        elif self.ttt_board[combo[x]] == 0:
            count += 100
            #append empty space
            zIndex.append(combo[x])

        x += 1

    if count == 201:
        for item in zIndex:
            #middle spot on the board - prioritize if it hasn't been taken already
            if item == 4:
                #print("Moved in the middle")
                return 4
            #prioritize the corners so you don't get trapped
            elif item in corners:
                #print("In diagonal")
                return item


        #maybe add another check here but for now if it doesn't fit any of the above just return a random
        #between the two

        if len(zero_indexes) == 8:
            #print("Diagonal")
            list_of_options = []
            for i in corners:
                if i in zero_indexes:
                    list_of_options.append(i)

            return random.choice(list_of_options)

        #print("randomly chose")
        return random.choice(zIndex)
    else:
        return -1
