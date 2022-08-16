from csv import reader
from distutils.log import error
import sqlite3
import os
import shutil

class Database(object):
    ring = [0, 10, 25, 50, 2500]
    face = [0, 1, 2, 4]
    stack = [0, 1, 3, 5]

    def __init__(self, database_path):
        self.__path = os.path.abspath(database_path)
        try:
            self.__connect = sqlite3.connect(self.__path)
        except:
            Warning("Cannot access main database. Attempting to load backup database")
        try:
            self.__path = "backup/" + os.path.basename(self.__path)
            self.__connect = sqlite3.connect(self.__path)
        except:
            raise "Failed to load database"
        
        self.__cursor = self.__connect.cursor()

    def __del__(self):
        # Close the database
        self.__connect.close()

    def push(self):
        self.__connect.commit()
        print('Database Updated')

    def backup(self):
        db_pth = self.__path
        _, path = os.path.splitdrive(db_pth)
        path, filename = os.path.split(path)
        cwd = os.getcwd()

        src = db_pth
        dst = cwd + '\\backup\\' + filename
        shutil.copyfile(src, dst)

    def record_game(self, game_ID, player_list, lead, winner, tosses_list):
        if game_ID == 'next':
            new_ID_1 = self.search_one("SELECT MAX(game_id) FROM Games")[0]
            new_ID_2 = self.search_one("SELECT MAX(game_id) FROM Throws")[0]
            new_ID_3 = self.search_one("SELECT MAX(game_id) FROM Scores")[0]
            if new_ID_1 is new_ID_2 is new_ID_3:
                game_ID = new_ID_1+1
            else:
                raise Exception("Game ID mismatch: Please resolve first")
        for player, toss in zip(player_list, tosses_list):
            self.add_score(game_ID, player, toss)
        self.add_game(game_ID, lead, winner)

    def add_table(self, table):
        self.__cursor.execute(table)

    def add_score(self, game_ID, name, tosses):
        tosses = [int(a) for a in tosses]
        assert len(tosses) == int(3*9), "Player 1 data entry: Improper size"
        assert not any([p > 4 for p in tosses]), "Player 1 data entry: Improper values"
        score = self._score(tosses)
        self.__cursor.execute('SELECT player_ID FROM Players WHERE player_name="{0}";'.format(name.lower()))
        player_ID = self.__cursor.fetchone()
        if player_ID is None:
            self.add_player(name)
            self.__cursor.execute('SELECT player_ID FROM Players WHERE player_name="{0}";'.format(name.lower()))
            player_ID = self.__cursor.fetchone()[0]
        else:
            player_ID = player_ID[0]
        throwing_table = "INSERT INTO Throws VALUES (?,?,?,?,?,?,?);"
        score_table = "INSERT INTO Scores VALUES (?,?,?,?,?,?);"
        # Input into tables
        score_data = (game_ID, player_ID,) + (score[0]+score[1]+score[2], score[3]+score[4]+score[5], score[6]+score[7]+score[8], sum(score))
        for i, j in enumerate(range(0, 27, 3)):
            self.__cursor.execute(throwing_table, (game_ID, player_ID, i+1, tosses[j], tosses[j+1], tosses[j+2], score[i]))
        self.__cursor.execute(score_table, score_data)

    def add_game(self, game_ID, lead, winner):
        game_table = "INSERT INTO Games VALUES (?,?,?);"
        self.__cursor.execute('SELECT player_ID FROM Players WHERE player_name="{0}";'.format(winner.lower()))
        winner_ID = self.__cursor.fetchone()[0]
        self.__cursor.execute('SELECT player_ID FROM Players WHERE player_name="{0}";'.format(lead.lower()))
        lead_ID = self.__cursor.fetchone()[0]
        self.__cursor.execute(game_table, (game_ID, lead_ID, winner_ID))

    def remove_game(self, game_id):
        self.__cursor.execute(f'''DELETE FROM Games WHERE game_id = {game_id};''')
        self.__cursor.execute(f'''DELETE FROM Scores WHERE game_id = {game_id};''')
        self.__cursor.execute(f'''DELETE FROM Throws WHERE game_id = {game_id};''')
        self.push()

    def add_player(self, player_name):
        self.__cursor.execute('''SELECT max(player_ID) FROM Players''')
        max_ID = self.__cursor.fetchone()
        max_ID = max_ID[0]
        if max_ID is None:
            max_ID = 0
        self.__cursor.execute('''INSERT INTO Players VALUES (?,?);''', (int(max_ID+1), player_name.lower()))
    
    def add_row(self, query, data):
        self.__cursor.execute(query, data)

    def search(self, query):
        self.__cursor.execute(query)
        return self.__cursor.fetchall()
    
    def search_one(self, query):
        self.__cursor.execute(query)
        return self.__cursor.fetchone()

    def execute(self, command, inputs=()):
        self.__cursor.execute(command, inputs)

    def _score(self, tosses):
        score = []
        for i in range(0, 3*9, 3):
            score.append(self.ring[int(tosses[i])]*self.face[int(tosses[i+1])]*self.stack[int(tosses[i+2])])
        return score