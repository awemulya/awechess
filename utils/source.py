import os


class SourcePath(object):

    def get_source_path(self):
        source_dir = os.path.join(os.getcwd(), 'source', 'source.txt')
        with open(source_dir) as source:
            source = source.read()
        return source



