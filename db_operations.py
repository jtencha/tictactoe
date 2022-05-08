'''
This module should be run once to initialize a new sqlite3 database file for the mathquiz program.
WARNING - Running this module will result in the loss of an existing mathquiz database of the same name.

Execute this file on a python command line by supplying the full path to a new database file.
---
python initialize_sqlite_db.py /full/path/to/db/file.db
---
'''

import sqlite3
import sys
import os
import time
from datetime import date
import time

DB_NAME = "tictactoe.db"

# Set up database
def initialize_db(db_name):
    # Create and connect to database
    print("Creating database...")

    try:
        # Open db connection
        with sqlite3.connect(db_name) as sqlite_connection:
            # Set up connection cursor
            sqlite_cursor = sqlite_connection.cursor()

            # Create COUNTRY table
            sqlite_cursor.execute("DROP TABLE IF EXISTS RESULTS")
            sqlite_connection.commit()
            sqlite_cursor.execute("CREATE TABLE RESULTS (RecordID integer PRIMARY KEY AUTOINCREMENT, \
                                GameID text, PlayerID text, BoardStatus text, PlayerType integer, TurnNumber integer, Winner integer, RunDate date)")
            sqlite_connection.commit()
            print("Created RESULTS table")
            return True

    except:
        print("Fatal Error:", sys.exc_info())
        quit()


#Write saved game board states to database with win/loss/tie labels
def savetoDB(player_histories, db_name=DB_NAME):

    print("Writing game results to database...")
    gameID = time.time()
    for player_bundle in player_histories:
        player_type, player_result, boards = player_bundle
        playerID = time.time()
        turn = 1
        for board in boards:
            try:
                # Open db connection
                with sqlite3.connect(db_name) as sqlite_connection:
                    # Set up connection cursor
                    sqlite_cursor = sqlite_connection.cursor()
                    # Insert game board
                    insert_sql = "INSERT INTO RESULTS (GameID,PlayerID,BoardStatus,PlayerType,TurnNumber,Winner,RunDate) VALUES ({0},{1},'{2}',{3},{4},{5},'{6}')".format(gameID,playerID,board,player_type,turn,player_result,date.today())
                    sqlite_cursor.execute(insert_sql)
                    sqlite_connection.commit()
                    #print("Added record to RESULTS table")

            except:
                print("Fatal Error:", sys.exc_info())
                quit()
            turn += 1

    return True


# Run this when called from CLI
if __name__ == "__main__":

    initialize_db(DB_NAME)
    print("Done!")
