# Puzzle Solver

A small program written in python 3 that solves a given puzzle, with a simple CLI to activate.

For now, the solver only works for square images and square tiles, but that might change...

## Getting Started

### Prerequisites

Have [python](https://www.python.org/downloads/) installed on your machine (if you are in [this](https://unix.stackexchange.com/a/24808) list then you have python pre-installed on your machine).

To run this program you also need PIL/PILLOW package installed. To install PIL you need to run the following:

```sh
# For windows users
C:\current\path> pip install pillow

# For unix-like users
$ pip3 install pillow
```

Note: If you are on a unix-like machine you might need to use `sudo` before the rest of the statement to have successful installation. 

### Downloading

To download the project to your local machine, first download the zipped repo from [here](https://github.com/Alon-Alexander/puzzle_solver/archive/master.zip) or clone the repository using [git](https://git-scm.com/):

```sh
$ git clone https://github.com/Alon-Alexander/puzzle_solver.git
```

### Usage

You can get all the information you need by running:

```sh
# For windows users
C:\current\path> python puzzle_solver -h

# For unix-like users
$ python3 puzzle_solver -h
```

which will display:

```
usage: puzzle_solver [-h] [-i INPUT] [-o OUTPUT] [-t THRESH] [-ts TS] [-ta TA]
                     [--shuffle] [--show] [--no-save] [-v]

Process some integers.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        path to the input image
  -o OUTPUT, --output OUTPUT
                        path to output result into
  -t THRESH, --thresh THRESH
                        amount of threshold to use for distance between edges
  -ts TS                amount of pixels in a single tile
  -ta TA                amount of tiles in a row/column
  --shuffle             shuffle input image instead of solving
  --show                show solved image after execution
  --no-save             don't save image after execution
  -v, --verbose         print status during execution
```

but here are the basics...

#### Solve a Puzzle

To solve a puzzle you need to have a few known factors:
1. The amount of tiles in the puzzle.
1. The amount of pixels in a single tile's row/column.

Now you can solve the puzzle using:

```sh
# For windows users
C:\containing\directory> python puzzle_solver -i path\to\puzzle -o path\to\output\solved\image.png  -ts <tile-size> -ta <tile-amount>

# For unix-like users
$ python3 puzzle_solver -i path\to\puzzle -o path\to\output\solved\image.png  -ts <tile-size> -ta <tile-amount>
```

and you should get your solved puzzle in the specified folder.

Probably, unless your are using the example, **you will need to change the threshold of the solver**.

To run with a custom threshold use the `-t` *or* `--thresh` option and specify your threshold (f.e. the default threshold is `40000`).

As a rule of thumb: When you get an error you got *to many* tiles you should *decrease* your threshold and vise-versa.

#### Create a puzzle

To create a puzzle you need a square image.

Next you need to decide a tile-size: It must be a divider of the size of the image. For example, if your image is `1000x1000` you can choose a tile size of `100` or `250`, but you can't choose a tile size of `150`.

Now you can use the package to create your puzzle:

```sh
# For windows users
C:\current\path> python puzzle_solver -i path\to\original -o path\to\output -ts <tile-size> -ta <tile-amount> --shuffle

# For unix-like users
$ python3 puzzle_solver -i path\to\original -o path\to\output -ts <tile-size> -ta <tile-amount> --shuffle
```

Just replace <tile-size> with your chosen tile size and <tile-amount> with your **image side** divided by the **tile size**.


### Walk-through Example

First, open a CMD/terminal in the folder in which the project lies, if you followed the steps above using git then you are in the correct folder.

To check if you are in the correct folder run the following:

```sh
# For windows users
C:\current\path> dir

# For unix-like users
$ ls
```

You are supposed to see the folder `puzzle_solver` as one of the results.

<br>

**Now we can run the solver from the CMD/terminal using its CLI.**

If you look in the example folder in the package you can see there is a file called `shuffled.png`. It is a puzzle created from `orig.png` using the CLI.
Let's copy the shuffled image to our current working folder by executing:

```sh
$ cp puzzle_solver/example/shuffled.png shuffled.png
```

Now that we have puzzle to solve we can use the solver to solve it. Run the solver:

```sh
# For windows users
C:\current\path> python puzzle_solver -i shuffled.png -o solved.png

# For unix-like users
$ python3 puzzle_solver -i shuffled.png -o solved.png
```

After the script finishes you are supposed to have another file in your current folder called `solved.png`.
If you open this file you will see the solved puzzle (the same as `puzzle_solver/example/orig.png` and `puzzle_solver/example/solved.png`).

## Built With

* [Pillow](https://pillow.readthedocs.io/) - The package used for manipulating images.

## Authors

* **Alon Alexander** - [GitHub Profile](https://github.com/Alon-Alexander)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details