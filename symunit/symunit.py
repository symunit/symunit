"""SymUnit is a main entry
"""

from __future__ import print_function
import sys

class SymUnit(object):
    """
    A class for entry

    Examples
    --------


    """

    def __init__(self):
        print ('TEST')

if __name__ == '__main__':
    try:
        SymUnit()
    except Exception as err:
        print(str(err))
        sys.exit(-1)
