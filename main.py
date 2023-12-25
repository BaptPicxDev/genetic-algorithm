# -*- coding: utf-8 -*-

#############################################
# author : Baptiste PICARD                  #
# date : 16/12/2020                         #
# last modif : 16/12/2020                   #
#                                           #
# overview : Genetic algorithm example.     #
# The main of this script is the get one of #
# the right path from a point to another.   #
#                                           #
#############################################

## Imports.
from math import sqrt
import random
import numpy as np
from datetime import datetime

## Envionment
N_ROWS = 8
N_COLS = 8
START = (0, 0)
END = (7, 7)

## Functions
def initialisation(n):
        individues = []
        for i in range(n):
                individues.append([random.randint(0, 3) for j in range(10)])
        return individues

def heuristic(individu) : 
        '''
                Calcul la distance entre l'individu et l'arrivée
                0 : haut
                1 : bas
                2 : droite
                3 : gauche
        '''
        up, down, left, right = individu.count(0), individu.count(1), individu.count(2), individu.count(3)
        up=up-down
        right=right-left
        x0 = START[0] + right
        y0 = START[1] + up
        if x0>0 and x0<=7 and y0>0 and y0<=7:
                h = sqrt((END[0] - x0)**2 + (END[1]-y0)**2)
                return h, (x0, y0)
        else:
                return None, (x0, y0)

def draw_map(point):
        carte = [['', '', '', '', '', '', '', ''] for i in range(8)]
        carte[len(carte)-1-START[0]][START[1]] = 'o'
        carte[len(carte)-1-END[0]][END[1]] = 'x'
        carte[len(carte)-1-point[0]][point[1]] = 'pt'
        for c in carte:
                print(c, '\n')

## Main part
if __name__ == '__main__':
        start = datetime.now()
        invs = initialisation(100)
        a = [heuristic(inv) for inv in invs]
        for index, a_ in enumerate(a):
                if a_[0]:
                        print('Index : {} --------------'.format(index))
                        draw_map(a_[1])
                        print(a_[0])
        print("It takes {} seconds to reach the end of the code.".format((datetime.now() - start).seconds))
  
