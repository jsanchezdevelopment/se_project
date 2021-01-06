#!/usr/bin/python

class FindTextError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'FindTextError, {0} '.format(self.message)
        else:
            return 'FindTextError has been raised'
