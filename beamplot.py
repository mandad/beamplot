import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

data_type = 'kongsberg'

def deg_cos(angle):
    return np.cos(angle * np.math.pi/180)

def deg_sin(angle):
    return np.sin(angle * np.math.pi/180)

def main(file):
    data = np.load(file)
    proj_pts = [[0, 0, 0]]
    #['b_dir_corr', 'r_dir', 'r_takeoff', 'b_takeoff']
    # for beam in zip(data['b_dir_corr'],data['b_takeoff']):
    # for beam in zip(data['r_dir'],data['r_takeoff']):
    for beam in zip(data['b_dir'],data['b_takeoff']):
        bd = beam[0]
        # second beam angle is from straight down, our coordinate zero is stbd
        bt = 90 - beam[1]
        # first rotation is around z axis from forward
        rot1 = np.matrix([[deg_cos(bd), deg_sin(bd), 0],
            [-deg_sin(bd), deg_cos(bd), 0],
            [0, 0, 1]])
        # second rotation is around rotated y axis
        rot2 = np.matrix([[deg_cos(bt), 0, -deg_sin(bt)],
            [0, 1, 0],
            [deg_sin(bt), 0, deg_cos(bt)]])
        # we are rotating an intial vector facing straight forward
        fwd_vec = np.matrix([[1],[0],[0]])

        rot_beam = rot1 * (rot2 * fwd_vec)
        # intersect with a plane at nadir depth depth
        if data_type == 'kongsberg':
            t = data['ranges'][int(len(data['ranges'])/2)]/float(rot_beam[2])
        else:
            t = 100/float(rot_beam[2])
        beam_plane = rot_beam * t
        proj_pts = np.vstack((proj_pts, np.array(np.reshape(beam_plane,3))))

    print proj_pts
    plt.scatter(proj_pts[1:,0], proj_pts[1:,1], s=5, edgecolors='none')
    # plt.axis('equal')

    plt.show()
    return proj_pts
        

if __name__ == '__main__':
    main(sys.argv[1])