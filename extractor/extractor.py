import os
from utils.source import SourcePath


class Extractor(object):

    def extract_files(self):
        sp = SourcePath()
        files = [os.path.join(sp.get_source_path(), filename) for filename in os.listdir(sp.get_source_path())]
        return files


    def alter(self,value):
        return False if value else True

    def save_game(self, game_list, move_list):
        print game_list , move_list

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

