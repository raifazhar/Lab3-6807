# -*- coding: utf-8 -*-
"""l226807 lab3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/116SmCM7lgn3B_4ZJSjWAdhbwbKD9E6ly
"""

from collections import deque
def main():
  matrix=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,-1,0,0,0],[0,0,0,-1,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
  path=find_shortest_path(matrix)
  print(path)

def find_shortest_path(matrix):
 # Directions: Up, Down, Left, Right
 directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
 # Initialize starting and ending positions
 start = (1, 1)
 end = (4, 4)
 # Initialize data structures for BFS
 queue = deque() # Use deque for BFS
 queue.append((start,[start]))
 visited = set() # Track visited positions
 # BFS Loop
 while queue:
  current,path=queue.popleft()
  if current not in visited:

    visited.add(current)
    if(current!=end):
      for direction in directions:
        nextposition=current[0]+direction[0],current[1]+direction[1]
        if(nextposition[0]>=0 and nextposition[0]<=5 and nextposition[1]>=0 and nextposition[1]<=5):
           queue.append((nextposition,(path +[nextposition])))
    else:
      return path

main()

import copy
import time
import numpy as np

def state_to_matrix(state):
    """Convert a string state to a 3x3 NumPy array."""
    matrix_elements = [int(char) for char in state]
    matrix = np.array(matrix_elements).reshape((3, 3))
    return matrix

def matrix_to_state(matrix):
    """Convert a 3x3 NumPy array back to a string state."""
    return ''.join(str(num) for num in np.array(matrix).flatten())

def get_moves(matrix):
    """Generate possible moves from the given state."""
    moves = []
    current_position = None

    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                current_position = (i, j)
    x, y = current_position
    if x > 0: moves.append((-1, 0))
    if x < 2: moves.append((1, 0))
    if y > 0: moves.append((0, -1))
    if y < 2: moves.append((0, 1))

    return current_position, moves

def apply_move(move, start_position, matrix):
    """Apply a move to the matrix and return the new state."""
    new_matrix = copy.deepcopy(matrix)
    x, y = start_position
    dir_x, dir_y = move
    new_matrix[x][y], new_matrix[x + dir_x][y + dir_y] = new_matrix[x + dir_x][y + dir_y], new_matrix[x][y]
    return new_matrix

def dfs(start_matrix, goal_matrix):
    """Perform Depth-First Search (DFS) to find a solution path."""
    stack = [(start_matrix, [])]
    visited = set()

    goal_state = matrix_to_state(goal_matrix)

    while stack:
        current_matrix, path = stack.pop()
        current_state = matrix_to_state(current_matrix)

        if current_state in visited:
            continue

        visited.add(current_state)

        if current_state == goal_state:
            return path

        current_position, moves = get_moves(current_matrix)

        for move in moves:
            new_matrix = apply_move(move, current_position, current_matrix)
            new_state = matrix_to_state(new_matrix)

            if new_state not in visited:
                stack.append((new_matrix, path + [new_matrix]))

    return None

def main():
    """Main function to take input and execute the DFS algorithm."""
    start_matrix = [[1, 2, 0], [3, 4, 5], [6, 7, 8]]
    goal_matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    print("-----------------")
    print("DFS Algorithm")
    print("-----------------")

    start_time = time.time()
    solution_path = dfs(start_matrix, goal_matrix)
    end_time = time.time()

    if solution_path:
        print("Time taken:", end_time - start_time, "seconds")
        print("Path Cost:", len(solution_path))
        print("No of Nodes Visited:", len(solution_path))

        for state in solution_path:
            for row in state:
                print(' '.join(map(str, row)))
            print("-----")
    else:
        print("No solution found.")

main()

import heapq

graph = {
    "The": {"cat": 2, "dog": 3},
    "cat": {"runs": 2},
    "dog": {"runs": 1},
    "runs": {"fast": 1},
    "fast": {}
}

heuristic = {
    "The": 4,
    "cat": 3,
    "dog": 3,
    "runs": 2,
    "fast": 1
}

def a_star(start, goal):
    """Perform A* search to find the best sentence completion."""
    pq = [(heuristic[start], 0, start, [start])]
    visited = set()

    while pq:
        _, g, current_word, path = heapq.heappop(pq)

        if current_word in visited:
            continue
        visited.add(current_word)

        if current_word == goal:
            return path, g

        for neighbor, cost in graph[current_word].items():
            if neighbor not in visited:
                f = g + cost + heuristic[neighbor]
                heapq.heappush(pq, (f, g + cost, neighbor, path + [neighbor]))

    return None, float("inf")

best_path, total_cost = a_star("The", "fast")

if best_path:
    print("Optimal Sentence Completion Path:", " → ".join(best_path))
    print("Total Cost:", total_cost)
else:
    print("No valid sentence completion found.")