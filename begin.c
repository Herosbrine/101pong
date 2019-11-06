#!/usr/bin/python3
import sys
from math import *

def main():
    if len(sys.argv) != 8:
        help()
    else:
        argv = sys.argv
        vect_v1 = 3
        vect_v2 = 0
        vect_v3 = 0
        try :
            x0, y0, z0 = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
            x1, y1, z1 = float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])
            n = int(sys.argv[7])
        except ValueError:
            help()
            sys.exit(84)
        V1 = x1 - x0 
        V2 = y1 - y0
        V3 = z1 - z0
        print ("The velocity vector of the ball is:")
        print ("(%.2f, %.2f, %.2f)" %(V1, V2, V3))
        X4 = x1 + V1 * 4
        Y4 = y1 + V2 * 4
        Z4 = z1 + V3 * 4
        print("At time t + 4, ball coordinates will be:")
        print ("(%.2f, %.2f, %.2f)" %(X4, Y4, Z4))
        if X4 > 30: # changer condition car incorrecte -> lorsque le calcul avec vecteur_v x = 0
            print("The ball won't reach the paddle.")
            sys.exit(0)
        if Y4 > 30: # changer condition car incorrecte -> lorsque le calcul avec vecteur_v y = 0
            print("The ball won't reach the paddle.")
            sys.exit(0)
        if Z4 < -30: # changer condition car incorrecte -> lorsque le calcul avec vecteur_v z = 0
            print("The ball won't reach the paddle.")
            sys.exit(0)
        vect_u1 = X4 - x1
        vect_u2 = Y4 - y1
        vect_u3 = Z4 - z1