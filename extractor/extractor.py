import re

from game.models import GameData, Player, Move
from datetime import datetime


def make_game(game_list):

    game = GameData()
    game.event = game_list[0][8:-3]
    game.site = game_list[1][7:-3]
    game.date = datetime.strptime(game_list[2][7:-3], '%Y.%m.%d').date()
    game.round = game_list[3][8:-3]
    white, created = Player.objects.get_or_create(name=game_list[4][8:-3])
    game.white = white
    black, created = Player.objects.get_or_create(name=game_list[5][8:-3])

    game.black = black
    game.result = game_list[6][9:-3]
    game.white_elo = game_list[7][11:-3]
    game.black_elo = game_list[8][11:-3]
    game.event_date = datetime.strptime(game_list[10][12:-3], '%Y.%m.%d').date()
    game.eco = game_list[9][6:-3]
    game.save()
    return game


def save_moves(game, moves_list):
    moves = []
    for moverow in moves_list:
        moverow = moverow.replace('\n', '')
        moveitem = moverow.split(" ")
        for move in moveitem:
            if '.' in move:
                if re.search('[a-zA-Z]', move):moves.append(move.split('.')[1])
            else:
                if re.search('[a-zA-Z]', move):moves.append(move)
    for count, mv in enumerate(moves):
        move = Move(game=game,move_no=count,move=mv)
        move.save()


class Extractor(object):
    if isinstance(object, basestring):
        raise TypeError(" Not a List of files")

    def __init__(self, files):
        self.files = files

    def alter(self,value):
        return False if value else True

    def save_game(self, game_list, move_list):
        game = make_game(game_list)
        save_moves(game, move_list)

    def run(self):
        is_game_desc = True
        test_file = self.files[0]
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


