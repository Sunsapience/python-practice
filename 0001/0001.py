# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 20:12:49 2017

"""

import random
import string

forSelect = string.ascii_letters + string.digits

def generate_code(count, length):
    f = open('Activation_code.txt', 'w')
    for x in range(count):
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)
        f.write(Re+'\n')
        print(Re) 
    f.close()

if __name__ == '__main__':
    generate_code(200, 20)
