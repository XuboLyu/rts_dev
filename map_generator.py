import sys,os
import numpy as np
import noise

MAP_WIDTH = 640
MAP_HEIGHT = 480


class Map(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map_array = np.array((width, height))

    def create(self, noise=None):
        if noise is None:
            raise ValueError("Please specify a noise type!!")

    def perlin_noise(self):
        pass


def LinearConversion(src, des, x):
    assert len(src) == len(des) == 2
    assert src[0] < src[1] and des[0] < des[1]
    res = des[0] + (x - src[0]) * abs(des[1]-des[0]) / abs(src[1]-src[0])
    return res


if __name__ == "__main__":
    np.random.seed()
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import cm
    import math
    value = np.zeros((MAP_HEIGHT, MAP_WIDTH))
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            nx, ny = x/MAP_WIDTH-0.5, y/MAP_HEIGHT-0.5
            # value[y][x] = LinearConversion([-1,1], [0,1], noise.pnoise2(7.00*nx, 7.00*ny))
            e = 1 * LinearConversion([-1,1], [0,1], noise.pnoise2(1*nx, 1*ny)) \
                + 0.50 * LinearConversion([-1,1], [0,1], noise.pnoise2(2*nx, 2*ny)) \
                + 0.25 * LinearConversion([-1,1], [0,1], noise.pnoise2(4*nx, 4*ny)) \
                + 0.13 * LinearConversion([-1,1], [0,1], noise.pnoise2(8*nx, 8*ny)) \
                # + 0.06 * LinearConversion([-1,1], [0,1], noise.pnoise2(16*nx, 16*ny)) \
                # + 0.03 * LinearConversion([-1,1], [0,1], noise.pnoise2(32*nx, 32*ny)) \
            # e /= (1.00 + 0.50 + 0.25)
            # # e = 1 * noise.pnoise2(1*nx, 1*ny) \
            # #     + 0.5 * noise.pnoise2(2*nx, 2*ny) \
            # #     + 0.25 * noise.pnoise2(4*nx, 4*ny)
            value[y][x] = math.pow(e, 8)
    # print(value)
    # print("shape of value:", np.shape(value))
    # print("height range:", np.shape(np.arange(MAP_HEIGHT)))
    # print("width range:", np.shape(np.arange(MAP_WIDTH)))

    X, Y = np.meshgrid(np.arange(MAP_WIDTH), np.arange(MAP_HEIGHT))
    fig = plt.figure()
    # ax = fig.gca(projection='3d')
    # ax.grid(False)
    # ax.set_zlim(0, 1)
    # surf = ax.plot_surface(X, Y, value, cmap='Greens_r')
    plt.imshow(value, cmap='Greens_r')
    plt.show()