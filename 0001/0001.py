# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 20:12:49 2017

"""

import random
import string

forSelect = string.ascii_letters + string.digits


def generate_code(count, length):
    for x in range(count):
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)
        print(Re)

if __name__ == '__main__':

    generate_code(200, 20)
