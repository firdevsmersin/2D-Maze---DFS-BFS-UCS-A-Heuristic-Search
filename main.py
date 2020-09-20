import json
from DFS import DFS
from BFS import BFS
from Node import Node
from IDS import IDS
from UCS import UCS
from GreedyBestFirstSearch import GreedyBestFirstSearch
from AStar import AStar
import sys


def main(file, mode):
    with open(file) as maze_file:
        maze_data = json.load(maze_file)
        maze = maze_data["maze"]
        initial_state = maze_data["initial_state"]
        initial_state = Node(initial_state[0], initial_state[1])
        goal_states = maze_data["goal_states"]
        #dfs = DFS("DEPTH-FIRST SEARCH", maze, initial_state, goal_states)
        #dfs.execute(mode)
        #bfs = BFS("BREADTH-FIRST SEARCH", maze, initial_state, goal_states)
        #bfs.execute(mode)
        #ids = IDS("ITERATIVE DEEPENING SEARCH", maze, initial_state, goal_states)
        #ids.execute(mode)
        #ucs = UCS("UNIFORM-COST SEARCH", maze, initial_state, goal_states)
        #ucs.execute(mode)
        #gbfs = GreedyBestFirstSearch("Greedy Best First Search", maze, initial_state, goal_states)
        #gbfs.execute(mode)
        astar = AStar("A Star Search", maze, initial_state, goal_states)
        astar.execute(mode)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        file_input = "maze.json"
        exec_mode = '0'
    else:
        file_input = sys.argv[1]
        exec_mode = sys.argv[2]
    main(file_input, exec_mode)
