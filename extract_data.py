import sys
import numpy as np

def line_to_list(linetxt):
    return [float(x) for x in linetxt.split(" ")]

# Open and read the data file
def process_RMB(datafile):
    ranges = line_to_list(datafile.readline())
    b_takeoff = line_to_list(datafile.readline())
    b_dir = line_to_list(datafile.readline())

def main():
    # Save out to a numpy file
    datafile = open(sys.argv[1])
    process_RMB(datafile)
    np.savez(sys.argv[2], ranges=ranges, b_takeoff=b_takeoff, b_dir=b_dir)

if __name__ == '__main__':
    main()