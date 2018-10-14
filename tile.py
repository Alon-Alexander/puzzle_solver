import math

from PIL import Image

import utils
from consts import Consts


class Tile:
    tiles = []
    opposite_direction = {
        'left': 'right',
        'right': 'left',
        'up': 'down',
        'down': 'up',
    }
    direction_to_edge = {
        'left': 'left',
        'right': 'right',
        'up': 'top',
        'down': 'bottom',
    }

    def __init__(self, img: Image, x, y):
        self.img = img.crop((x * Consts.TILE_SIZE, y * Consts.TILE_SIZE, (x + 1) * Consts.TILE_SIZE, (y + 1) * Consts.TILE_SIZE))
        self.x = x
        self.y = y
        self.neighbors = {
            'left': None,
            'right': None,
            'up': None,
            'down': None,
        }
        self.edges = {
            'top': self._create_edge('top'),
            'bottom': self._create_edge('bottom'),
            'left': self._create_edge('left'),
            'right': self._create_edge('right'),
        }

    def _create_edge(self, edge):
        x, y = 0, 0
        dx, dy = 0, 0

        if edge == 'top':
            dx = 1
        elif edge == 'bottom':
            dx = 1
            y = Consts.TILE_SIZE - 1
        elif edge == 'left':
            dy = 1
        elif edge == 'right':
            dy = 1
            x = Consts.TILE_SIZE - 1

        return [self.img.getpixel((x + dx * i, y + dy * i)) for i in range(Consts.TILE_SIZE)]

    def find(self, direction):
        opposite_direction = Tile.opposite_direction[direction]
        if self.neighbors[direction] is not None:
            return
        le = self[Tile.direction_to_edge[direction]]
        diffs = [utils.distance(le, t[Tile.direction_to_edge[opposite_direction]]) for t in Tile.tiles]
        m = min(diffs)
        i = diffs.index(m)
        while (Tile.tiles[i].neighbors[opposite_direction] is not None or Tile.tiles[i] == self) and not math.isinf(m):
            diffs[i] = math.inf
            m = min(diffs)
            i = diffs.index(m)

        if math.isinf(m) or Tile.tiles[i] == self:
            return

        if m < Consts.THRESHOLD:
            self.neighbors[direction] = Tile.tiles[i]
            Tile.tiles[i].neighbors[opposite_direction] = self

    def show(self):
        self.img.show()

    def __getitem__(self, item):
        return self.edges.get(item, None)

    def __repr__(self):
        return "Tile(x:%d, y:%d)" % (self.x, self.y)

    def __eq__(self, other):
        return type(other) is Tile and other.x == self.x and other.y == self.y
