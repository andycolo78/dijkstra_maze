"""
    Dijkstra Maze Resolver.
    A pratical application of Dijkstra algohrithm.
    Takes an textual ASCII maze file and find the shortest path 
    from Enter to Exit. 
"""

import argparse
from collections import deque
import sys

from dataclasses import dataclass, field
from typing import Optional

ADMITTED_MAZE_CHARS = {"#", " ", "S", "E"}
END_CHAR = "E"
START_CHAR = "S"
PATH_CHAR = " "
WALL_CHAR = "#"
WALKED_CHAR = "O"

explored_map = deque([])
frontier = deque([])


@dataclass
class Tile:
    coordinates: tuple[int, int]
    previous_node: Optional[tuple[int, int]] = None
    distance: int = 0
    type: str = ''

def main():
    parser = argparse.ArgumentParser(description="Resolve the maze.")
    parser.add_argument(
        "--file",
        type=str,
        help="Text file, must contain an ASCII format maze",
    )
    args = parser.parse_args()

    ## Parse file 
    maze = load_maze_file(args.file)

    print(*maze, sep="\n")

    ## Find enter and exit
    end_node = find_end(maze)

    print(f"Found end at {end_node}")

    frontier.append(end_node)

    ## explore the maze
    while frontier:
        actual_node = frontier.popleft()
        neighbour_paths = find_neighbours(actual_node, maze)

        while neighbour_paths:
            neighbour = neighbour_paths.pop()
            if not is_already_explored(neighbour, explored_map):
                frontier.append(neighbour)

        explored_map.append(actual_node)

    print("EXPLORED WHOLE MAP")
                
#        print(f"FRONTIER - {frontier}")

    resolved_maze = maze

#    print(*explored_map, sep="\n")

    start_node = get_start_node(explored_map)

    print(f"START NODE - {start_node}")

    walk_to = start_node
    while True:
        walk_to = get_node_by_coordinates(walk_to.previous_node, explored_map)
        if walk_to == end_node:
            break
        resolved_maze = walk_node(walk_to, resolved_maze)

    
    print(*resolved_maze, sep="\n")



    


    

def load_maze_file(path: str) -> list[str]:
    maze = []
    with open(path, "r", encoding="utf-8") as f:
        for row_num, line in enumerate(f, start=1):
            row = line.rstrip("\n")

            caratteri_riga = set(row)
            wrong_chars = caratteri_riga - ADMITTED_MAZE_CHARS
            if wrong_chars:
                print(f"Error: wrong chars found {wrong_chars} on row {row_num}")
                sys.exit(1)

            maze.append(row)

    maze_width = max(len(r) for r in maze)
    maze = [r.ljust(maze_width, "#") for r in maze]

    return maze

def find_end(maze: list) -> set:
    for y, row in enumerate(maze):
        x = row.find(END_CHAR)
        if x != -1:
            return Tile(coordinates=(y,x), type=END_CHAR)

def find_neighbours(tile: Tile, maze: list[str]) -> list[Tile]:

    #print(f"Find neighbours for {tile.coordinates} ")

    tile_y,tile_x = tile.coordinates

    maze_x_max = len(maze[0]) - 1
    maze_y_max = len(maze) - 1

    neighbours = []

    north = maze[tile_y - 1][tile_x] if tile_y > 0 else None
    south = maze[tile_y + 1][tile_x] if tile_y < maze_y_max else None
    west = maze[tile_y][tile_x - 1] if tile_x > 0 else None
    east = maze[tile_y][tile_x + 1] if tile_x < maze_x_max else None

    if north in [PATH_CHAR,START_CHAR] and (tile.previous_node != (tile_y - 1,tile_x) or not tile.previous_node):
        neighbours.append(Tile((tile_y - 1,tile_x),tile.coordinates,tile.distance+1,north))
    if south in [PATH_CHAR,START_CHAR] and (tile.previous_node != (tile_y + 1,tile_x) or not tile.previous_node):
        neighbours.append(Tile((tile_y + 1,tile_x),tile.coordinates,tile.distance+1,south))
    if west in [PATH_CHAR,START_CHAR] and (tile.previous_node != (tile_y,tile_x - 1) or not tile.previous_node):
        neighbours.append(Tile((tile_y,tile_x - 1),tile.coordinates,tile.distance+1,west))
    if east in [PATH_CHAR,START_CHAR] and (tile.previous_node != (tile_y,tile_x + 1) or not tile.previous_node):
        neighbours.append(Tile((tile_y,tile_x + 1),tile.coordinates,tile.distance+1,east))

    #print(f"Found neighbours : {neighbours}")

    return neighbours

def is_already_explored(node: Tile, explored: list[Tile]) -> bool :
    if next((explored_node for explored_node in explored if explored_node.coordinates == node.coordinates), None):
        return True

    return False     

def get_start_node(explored: list[Tile]) -> Tile :
    return next((explored_node for explored_node in explored if is_start(explored_node)), None)

def get_node_by_coordinates(coordinates: tuple, explored: list[Tile]) -> Tile:
    return next((explored_node for explored_node in explored if explored_node.coordinates == coordinates), None)

    
def is_start(node: Tile) -> bool:
    return node.type == START_CHAR

def walk_node(node: Tile, maze: list[str]) -> None:
    y,x = node.coordinates
    row = maze[y]
    maze[y] = row[:x] + WALKED_CHAR + row[x+1:]
    return maze


if __name__ == "__main__":
    main()