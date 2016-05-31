import os
import argparse

from django.core.management import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Command to import chess games from file to database"

    def add_arguments(self, parser):
        parser.add_argument('--dirname', type=str)

    def handle(self, *args, **options):
        dir_name = options['dirname']
        if dir_name == None :
            raise CommandError("Option `--dirname=...` must be specified.")

        # make sure file path resolves
        if not os.path.isdir(dir_name) :
            raise CommandError("Directory does not exist at the specified path.")
        elif not os.listdir(dir_name):
            raise CommandError("No files found in given Directory :" + dir_name)
        else:
            for pgnfile in os.listdir(dir_name):
                if not pgnfile.endswith('.pgn'):
                    raise CommandError("Not a pgn file :" + pgnfile)


