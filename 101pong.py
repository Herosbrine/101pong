#!/usr/bin/python3
import sys

def main():
    argv = sys.argv
    result = 0
    result1 = 0
    result2 = 0
    x0 = float(sys.argv[1])
    y0 = float(sys.argv[2])
    z0 = float(sys.argv[3])
    x1 = float(sys.argv[4])
    y1 = float(sys.argv[5])
    z1 = float(sys.argv[6])
    n = float(sys.argv[7])
    if argv[1] == '-h':
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
    if x1 == 1:
        result = x1 - x0 
        result1 = y1 - y0
        result2 = z1 - z0
        print("The velocity vector of the ball is:\n", (result, result1, result2))
if __name__ == "__main__":
    main()