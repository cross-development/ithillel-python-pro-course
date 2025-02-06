"""
This module runs doctests for the functions defined in the `numbers` module.
"""

import doctest

from hw_7.hw_7_4 import numbers

if __name__ == "__main__":
    doctest.testmod(numbers, verbose=True)
