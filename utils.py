from consts import Consts


def distance(e1, e2):
    diff = 0

    for i in range(Consts.TILE_SIZE):
        r = e1[i][0] - e2[i][0]
        g = e1[i][1] - e2[i][1]
        b = e1[i][2] - e2[i][2]

        diff += abs(r) + abs(g) + abs(b)

    return diff


def paste_tile_on_image(img, tile, x, y):
    img.paste(tile.img, (x * Consts.TILE_SIZE, y * Consts.TILE_SIZE))


def get_ext(path: str) -> str:
    return path.split('.')[-1]


def handle_err(length, index, is_row):
    if not length == Consts.TILES_AMOUNT:
        print('Error solving puzzle, got %d tiles in %s number %d instead of %d. Try changing your threshold.' %
              (length, 'row' if is_row else 'column', index + 1, Consts.TILES_AMOUNT))
        exit(1)


def log(msg):
    if Consts.VERBOSE:
        print('PUZZLE_SOLVER: %s' % msg)
