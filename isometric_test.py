import sys,os
import numpy as np
import pygame


def draw_sprite(screen, screen_x, screen_y, sprite, sprite_x, sprite_y, sprite_width, sprite_height):
    partial_sprite = sprite.subsurface(pygame.Rect(sprite_x, sprite_y, sprite_width, sprite_height))
    screen.blit(partial_sprite, (screen_x, screen_y))
    return True


def world_to_screen(x, y, origin, tile_size):
    screen_x = origin[0] * tile_size[0] + (x-y) * (tile_size[0]/2)
    screen_y = origin[1] * tile_size[1] + (x+y) * (tile_size[1]/2)

    return screen_x, screen_y


if __name__ == "__main__":
    # pass

    world_size = (14, 10)  # number of iso tiles each axis
    tile_size = (40, 20)   # length and width of single iso tile

    origin = (5, 1)  # relative original position on screen in tile size

    pworld = np.zeros(world_size)

    screen_width = 640
    screen_height = 480

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill([255, 255, 255])
    pygame.display.update()

    sprite = pygame.image.load("./assets/images/isometric_demo.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            screen.fill([255, 255, 255])
            mouse_pos = pygame.mouse.get_pos()

            # cell is regular rectagle
            cell_idx = (mouse_pos[0] // tile_size[0], mouse_pos[1] // tile_size[1])
            offset = (mouse_pos[0] % tile_size[0], mouse_pos[1] % tile_size[1])

            # where is the mouse currently on iso tile world , no need to click
            selected_idx = ((cell_idx[1] - origin[1]) + (cell_idx[0] - origin[0]),
                            (cell_idx[1] - origin[1]) - (cell_idx[0] - origin[0]))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if selected_idx[0] >= 0 and selected_idx[0] < world_size[0] and selected_idx[1] >= 0 and selected_idx[1] < world_size[1]:
                    pworld[selected_idx] %= 6
                    pworld[selected_idx] += 1

            for y in range(world_size[1]):
                for x in range(world_size[0]):
                    screen_x, screen_y = world_to_screen(x, y, origin, tile_size)
                    if pworld[x][y] == 0:
                        # invisible isometric tile
                        draw_sprite(screen, screen_x, screen_y, sprite, 1 * tile_size[0], 0, tile_size[0], tile_size[1])
                        # break
                    elif pworld[x][y] == 1:
                        # grass
                        draw_sprite(screen, screen_x, screen_y, sprite, 2 * tile_size[0], 0, tile_size[0], tile_size[1])
                        # break
                    elif pworld[x][y] == 2:
                        # tree
                        draw_sprite(screen, screen_x, screen_y, sprite, 0, 1 * tile_size[1], tile_size[0], tile_size[1]*2)
                        # break
                    elif pworld[x][y] == 3:
                        # bad tree
                        draw_sprite(screen, screen_x, screen_y, sprite, 1 * tile_size[0], 1 * tile_size[1], tile_size[0], tile_size[1]*2)
                        # break
                    elif pworld[x][y] == 4:
                        # desert
                        draw_sprite(screen, screen_x, screen_y, sprite, 2 * tile_size[0], 1 * tile_size[1], tile_size[0], tile_size[1]*2)
                        # break
                    elif pworld[x][y] == 5:
                        # water
                        draw_sprite(screen, screen_x, screen_y, sprite, 3 * tile_size[0], 1 * tile_size[1], tile_size[0], tile_size[1]*2)
                        # break
                    else:
                        raise ValueError("pworld value should be less than 6")

            selected_screen_x, selected_screen_y = world_to_screen(selected_idx[0], selected_idx[1], origin, tile_size)
            draw_sprite(screen, selected_screen_x, selected_screen_y, sprite, 0, 0, tile_size[0], tile_size[1])

        pygame.display.update()