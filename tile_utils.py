def fill(tile, direction):
    tile.find(direction)
    while tile.neighbors[direction] is not None:
        tile = tile.neighbors[direction]
        tile.find(direction)


def get_row(tile):
    ts = []

    while tile.neighbors['left'] is not None:
        tile = tile.neighbors['left']

    while tile is not None:
        ts.append(tile)
        tile = tile.neighbors['right']

    return ts


def get_col(tile):
    ts = []

    tile = go(tile, 'up')

    while tile is not None:
        ts.append(tile)
        tile = tile.neighbors['down']

    return ts


def go(tile, direction):
    while tile.neighbors[direction] is not None:
        tile = tile.neighbors[direction]
    return tile


def go_to_top_left(tile):
    fill(tile, 'up')
    tile = go(tile, 'up')

    fill(tile, 'left')
    tile = go(tile, 'left')

    return tile

