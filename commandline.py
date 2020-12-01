import sys

from paginator import Paginator
from reader import read


def last_page(paginator):
    return paginator.get_last_page()


def first_page(paginator):
    return paginator.get_first_page()


def next_page(paginator):
    return paginator.get_next_page()


def pevious_page(paginator):
    return paginator.get_previous_page()


def jump_to_page(paginator, page_index):
    return paginator.jump_to_page(page_index)


commands = {'l': last_page, 'f': first_page, 'n': next_page, 'p': pevious_page, 'e': sys.exit, 'j': jump_to_page}


class Commandline:

    def __init__(self, file_name):
        header, rows = read(file_name)
        self.paginator = Paginator(header=header, rows=rows)

    def start(self):
        return self.paginator.get_first_page()

    def execute(self, param):
        command = param.lower()
        if command in commands:
            if command == 'j':
                return self._jump_to_page()
            else:
                return commands[command](self.paginator)
        raise AttributeError("unknown command entered")

    def _jump_to_page(self):
        print("Input page index:")
        user_input = str(input())
        return commands['j'](self.paginator, int(user_input) - 1)
