#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 19:28:33 2017

@author: Anderson Banihirwe
"""

import sys
import os
import random
import pygame
sys.path.append(os.path.join("utils"))
import SudokuSquare
from assets import *

digits = '123456789'
rows = 'ABCDEFGHI'

def play(values_list):
    pygame.init()


    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)

    background_image = pygame.image.load("./images/sudoku-board-bare.jpg").convert()

    clock = pygame.time.Clock()

    # The puzzleNumber sets a seed so either generate
    # a random number to fill in here or accept user
    # input for a duplicatable puzzle.

    for values in values_list:
        pygame.event.pump()
        theSquares = []
        initXLoc = 0
        initYLoc = 0
        startX, startY, editable, number = 0, 0, "N", 0
        for y in range(9):
            for x in range(9):
                if x in (0, 1, 2):  startX = (x * 57) + 38
                if x in (3, 4, 5):  startX = (x * 57) + 99
                if x in (6, 7, 8):  startX = (x * 57) + 159

                if y in (0, 1, 2):  startY = (y * 57) + 35
                if y in (3, 4, 5):  startY = (y * 57) + 100
                if y in (6, 7, 8):  startY = (y * 57) + 165
                col = digits[y]
                row = rows[x]
                string_number = values[row + col]
                if len(string_number) > 1 or string_number == '' or string_number == '.':
                    number = None
                else:
                    number = int(string_number)
                theSquares.append(SudokuSquare.SudokuSquare(number, startX, startY, editable, x, y))

        screen.blit(background_image, (0, 0))
        for num in theSquares:
            num.draw()

        pygame.display.flip()
        pygame.display.update()
        clock.tick(5)


if __name__ == "__main__":
    main()
    sys.exit()
    