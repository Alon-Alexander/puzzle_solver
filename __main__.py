from PIL import Image
import argparse

from consts import Consts
from image_utils import shuffle_image, solve_image
from utils import log


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('-i', '--input', type=str, default=Consts.INPUT_PATH,
                        help='path to the input image')
    parser.add_argument('-o', '--output', type=str, default=Consts.OUTPUT_PATH,
                        help='path to output result into')
    parser.add_argument('-t', '--thresh', type=int, default=Consts.THRESHOLD,
                        help='amount of threshold to use for distance between edges')
    parser.add_argument('-ts', type=int, default=Consts.TILE_SIZE,
                        help='amount of pixels in a single tile')
    parser.add_argument('-ta', type=int, default=Consts.TILES_AMOUNT,
                        help='amount of tiles in a row/column')
    parser.add_argument('--shuffle', action="store_true",
                        help='shuffle input image instead of solving')
    parser.add_argument('--show', action="store_true",
                        help='show solved image after execution')
    parser.add_argument('--no-save', action="store_true",
                        help='don\'t save image after execution')

    parser.add_argument('-v', '--verbose', action='store_true',
                        help='print status during execution')

    args = parser.parse_args()
    Consts.INPUT_PATH = args.input
    Consts.OUTPUT_PATH = args.output
    Consts.THRESHOLD = args.thresh
    Consts.TILE_SIZE = args.ts
    Consts.TILES_AMOUNT = args.ta
    Consts.VERBOSE = args.verbose

    log('loading image')
    img = Image.open(args.input)
    log('image loaded')

    if args.shuffle:
        log('shuffling image')
        out = shuffle_image(img)
        log('image shuffled')
    else:
        log('solving puzzle')
        out = solve_image(img)
        log('puzzle solved')

    if args.show:
        log('showing result')
        out.show()

    if not args.no_save:
        log('saving output')
        out.save(args.output)
        log('output saved')