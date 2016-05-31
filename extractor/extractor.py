import os

# from game.models import GameData, Moves
from datetime import datetime
from utils.source import SourcePath


def make_game(game_list):
    event = game_list[0][8:-3]
    site = game_list[1][7:-3]
    date = datetime.strptime(game_list[2][7:-3], '%Y.%m.%d').date()
    game_round = game_list[3][8:-3]
    white = game_list[4][8:-3]
    black = game_list[5][8:-3]
    result = game_list[6][9:-3]
    white_elo = game_list[7][11:-3]
    black_elo = game_list[8][11:-3]
    eco = game_list[9][6:-3]
    event_date = datetime.strptime(game_list[10][12:-3], '%Y.%m.%d').date()


def save_moves(game, moves):
    pass


class Extractor(object):

    def extract_files(self):
        sp = SourcePath()
        files = [os.path.join(sp.get_source_path(), filename) for filename in os.listdir(sp.get_source_path())]
        return files


    def alter(self,value):
        return False if value else True

    def save_game(self, game_list, move_list):
        game = make_game(game_list)
        save_moves(game, move_list)

    def run(self):
        is_game_desc = True
        test_file = self.extract_files()[-1]
        with open(test_file) as data_file:
            game_list = []
            moves_list = []
            for line in data_file:
                if line in ['\n', '\r\n']:
                    if game_list and moves_list and not is_game_desc:
                        self.save_game(game_list, moves_list)
                        game_list , moves_list = [] , []
                    is_game_desc = self.alter(is_game_desc)
                else:
                    if is_game_desc:
                        game_list.append(line)
                    else:
                        moves_list.append(line)

