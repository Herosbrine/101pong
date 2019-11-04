#!/usr/bin/python3
import sys
from math import *

def main():
    argv = sys.argv
    V1 = 0
    V2 = 0
    V3 = 0
    X4 = 0
    Y4 = 0
    Z4 = 0
    vect_u1  = 0
    vect_u2  = 0
    vect_u3  = 0
    vect_v1 = 3
    vect_v2 = 0
    vect_v3 = 0
    x0 = float(sys.argv[1])
    y0 = float(sys.argv[2])
    z0 = float(sys.argv[3])
    x1 = float(sys.argv[4])
    y1 = float(sys.argv[5])
    z1 = float(sys.argv[6])
    n = float(sys.argv[7])
    if len(sys.argv) != 8:
        help()
    else:
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
        vect_u1 = X4 - x1
        vect_u2 = Y4 - y1
        vect_u3 = Z4 - z1
        produit_scalaire = vect_u1 * vect_v1 + vect_u2 * vect_v2 + vect_u3 * vect_v3
        norme_vect = sqrt((vect_u1**2)+(vect_u2**2)+(vect_u3)**2) * sqrt((vect_v1**2)+(vect_v2**2)+(vect_v3)**2)
        angle_incidence = produit_scalaire / norme_vect
        print ("The incidence angle is :")
        print ("%.2f degrees" % angle_incidence)
def help():
        print(" USAGE")
        print("    ./101pong x0 y0 z0 x1 y1 z1 n\n")
        print(" DESCRIPTION")
        print("     x0  ball abscissa at time t - 1")
        print("     y0  ball ordinate at time t - 1")
        print("     z0  ball ordinate at time t - 1")
        print("     x1  ball abscissa at time t")
        print("     y1  ball ordinate at time t")
        print("     z1  ball altitude at time t")
        print("     n   time shift (greater than or equal to zero, integer)") 
if __name__ == "__main__":
    main()