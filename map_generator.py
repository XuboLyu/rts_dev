import sys,os
import numpy as np
import noise
import pygame


class Grid(object):
    def __init__(self, size):
        self.xs = np.zeros(size)
        self.ys = np.zeros(size)
        self.connections = {}


class Map(object):
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen

        self.grid = None

    def createGrid(self, g_size, dx, view='regular'):
        assert g_size[0] > 1 and g_size[1] > 1
        self.grid = Grid(g_size) # g_size:[3,4]
        red = (255,0,0)
        # grows = g_size[0] - 1 # grows: consider interval as one row
        # gcols = g_size[1] - 1 # gcols: consider interval as one col

        assert (g_size[0]-1) * dx < self.height and (g_size[1] - 1) * dx < self.width

        origin_x = (self.width - (g_size[0]-1) * dx) // 2
        origin_y = (self.height - (g_size[1] - 1) * dx) // 2
        # print("origin x:", origin_x)
        # print("origin y:", origin_y)

        for r in range(g_size[0]):
            for c in range(g_size[1]):
                cur_x = origin_x + c * dx
                cur_y = origin_y + r * dx
                if view == "regular":
                    self.grid.xs[r][c] = cur_x
                    self.grid.ys[r][c] = cur_y
                elif view == "isometric":
                    # self.grid.xs[r][c] = cur_x - cur_y
                    # self.grid.ys[r][c] = (cur_x + cur_y) / 2

                    cart_x = cur_x - self.width / 2
                    cart_y = self.height / 2 - cur_y
                    iso_x = cart_x - cart_y
                    iso_y = (cart_x + cart_y) / 2
                    print("cart_x:", cart_x, "cart_y:", cart_y, "iso_x:", iso_x, "iso_y:", iso_y)

                    self.grid.xs[r][c] = iso_x + self.width / 2
                    self.grid.ys[r][c] = self.height / 2 - iso_y
                self.grid.connections[(r, c)] = []
                for nb in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    if 0 <= nb[0] <= g_size[0]-1 and 0 <= nb[1] <= g_size[1]-1:
                        self.grid.connections[(r, c)].append((nb[0], nb[1]))

        for key, value in self.grid.connections.items():
            for v in value:
                print("v:", v)
                start_coordx = self.grid.xs[key]
                start_coordy = self.grid.ys[key]

                end_coordx = self.grid.xs[v]
                end_coordy = self.grid.ys[v]
                pygame.draw.line(self.screen, red, (start_coordx, start_coordy), (end_coordx, end_coordy), 1)

    def perlin_noise(self):
        pass


def LinearConversion(src, des, x):
    assert len(src) == len(des) == 2
    assert src[0] < src[1] and des[0] < des[1]
    res = des[0] + (x - src[0]) * abs(des[1]-des[0]) / abs(src[1]-src[0])
    return res


if __name__ == "__main__":
    display_width = 1280
    display_height = 960

    pygame.init()
    screen = pygame.display.set_mode((display_width, display_height))

    Map = Map(display_width, display_height, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        Map.createGrid([8,8], 60, view="isometric")
        pygame.display.update()

    # np.random.seed()
    # import matplotlib.pyplot as plt
    # from mpl_toolkits.mplot3d import Axes3D
    # from matplotlib import cm
    # import math
    # value = np.zeros((MAP_HEIGHT, MAP_WIDTH))
    # for y in range(MAP_HEIGHT):
    #     for x in range(MAP_WIDTH):
    #         nx, ny = x/MAP_WIDTH-0.5, y/MAP_HEIGHT-0.5
    #         # value[y][x] = LinearConversion([-1,1], [0,1], noise.pnoise2(7.00*nx, 7.00*ny))
    #         e = 1 * LinearConversion([-1,1], [0,1], noise.pnoise2(1*nx, 1*ny)) \
    #             + 0.50 * LinearConversion([-1,1], [0,1], noise.pnoise2(2*nx, 2*ny)) \
    #             + 0.25 * LinearConversion([-1,1], [0,1], noise.pnoise2(4*nx, 4*ny)) \
    #             + 0.13 * LinearConversion([-1,1], [0,1], noise.pnoise2(8*nx, 8*ny)) \
    #             + 0.06 * LinearConversion([-1,1], [0,1], noise.pnoise2(16*nx, 16*ny)) \
    #             + 0.03 * LinearConversion([-1,1], [0,1], noise.pnoise2(32*nx, 32*ny)) \
    #         # e /= (1.00 + 0.50 + 0.25)
    #         value[y][x] = math.pow(e, 5)
    # # print(value)
    # # print("shape of value:", np.shape(value))
    # # print("height range:", np.shape(np.arange(MAP_HEIGHT)))
    # # print("width range:", np.shape(np.arange(MAP_WIDTH)))
    #
    # X, Y = np.meshgrid(np.arange(MAP_WIDTH), np.arange(MAP_HEIGHT))
    # fig = plt.figure()
    # # ax = fig.gca(projection='3d')
    # # ax.grid(False)
    # # ax.set_zlim(0, 1)
    # # surf = ax.plot_surface(X, Y, value, cmap='Greens_r')
    # plt.imshow(value, cmap='Greens_r')
    # plt.show()
