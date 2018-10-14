from random import shuffle

from PIL import Image

import tile_utils as tu
import utils
from consts import Consts
from tile import Tile


def shuffle_image(img):
    shuffled_image = Image.new('RGB', (Consts.IMAGE_SIZE, Consts.IMAGE_SIZE))

    tiles = [Tile(img, x, y) for x in range(Consts.TILES_AMOUNT) for y in range(Consts.TILES_AMOUNT)]
    shuffle(tiles)

    for x in range(Consts.TILES_AMOUNT):
        for y in range(Consts.TILES_AMOUNT):
            tile = tiles[x * Consts.TILES_AMOUNT + y]
            utils.paste_tile_on_image(shuffled_image, tile, x, y)

    return shuffled_image


def solve_image(img):
    Tile.tiles = [Tile(img, x, y) for x in range(Consts.TILES_AMOUNT) for y in range(Consts.TILES_AMOUNT)]
    sol = Image.new('RGB', (Consts.TILE_SIZE * Consts.TILES_AMOUNT, Consts.TILE_SIZE * Consts.TILES_AMOUNT))

    t = tu.go_to_top_left(Tile.tiles[0])
    tu.fill(t, 'right')
    utils.handle_err(len(tu.get_row(t)), 0, True)

    for x, tile_first_row in enumerate(tu.get_row(t)):
        tu.fill(tile_first_row, 'down')
        utils.handle_err(len(tu.get_col(tile_first_row)), x, False)

        for y, tile in enumerate(tu.get_col(tile_first_row)):
            utils.paste_tile_on_image(sol, tile, x, y)

    return sol
