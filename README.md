# dijkstra_maze
A maze resolver based on Dijkstra's algorithm, implemented in Python.

## Description
`dijkstra_maze` is an application of Dijkstra's algorithm to resolve the shortest path from a start point to an end point of a textual maze. Each cell of the maze is a graph node, and edges connect traversable adjacent cells. 

## Features

- Maze parsing from a text file
- Graph construction from the grid
- Shortest path computation with Dijkstra
- Visualization of the maze and the found path
- Support for custom cell weights
- Resolves maze with loops

## Requirements

- Python 3.9+
- Dependencies listed in `requirements.txt`

## Installation

```bash
git clone https://github.com/andycolo78/dijkstra_maze.git
cd dijkstra_maze
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python3 dijkstra_maze_resolver.py --file maze.txt
```

### Maze format

The maze can be provided as a text file, where each character represents a cell:

```
###################################################
S   #                   #             #       #   #
# ### ### # ### ######### ##### # ### ##### ### # #
#       # # # #   #   #   # # # # #       #     # #
### ######### # # # ### # # # ####### ##### # # # #
# #   # #     # # #   # #       # #       # # # # #
# # ### # ######### # ### ##### # ############### #
#               #   #   #   # # #   #   # #       #
# ##### # ########### ### ### ### # # ### # # # ###
#     # #   # # #           #     # #       # #   #
### ### ### # # # # ######### # # ##### # #########
#   # #   #   # # #   # # #   # # # # # # #   #   #
# # # # # ### # ### ### # # ##### # # # ##### # ###
# #   # # #       # # # #   #                   # #
# ##### ####### ### # # # ##### # # ### # ##### # #
# #         #               # # # #   # # # # # # #
# # # # # # ### ######### ### # # ### # ### # ### #
# # # # # # # # #   # #       # #   # #           #
# ### ####### # # ### ### # ##### ##### ### ### ###
#   # #                 # #   #       #   #   #   E
###################################################
```

- `#` = wall
- ` ` = free cell
- `S` = start point
- `E` = end point

## License

[MIT](LICENSE)