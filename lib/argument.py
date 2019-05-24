class Argument:
    def get_argument(self):
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument('function', help=('start or stop'))
        args = parser.parse_args()
        return args
