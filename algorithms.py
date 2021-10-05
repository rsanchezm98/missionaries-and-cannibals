from state import State
from collections import deque

def bfs(initial_node):
    if (initial_node.is_solution()):
        return initial_node
    
    frontier = deque()
    visited = dict()
    parents = dict()
    parents[initial_node.get_state()] = None


    frontier.append(initial_node)
    visited[initial_node.get_state()] = True
    while frontier:
        node = frontier.popleft()
        if node.is_solution():
            return get_path(node, parents)
        visited[node.get_state()] = True
        children = node.space_state()
        for child in children:
            if (child.get_state() not in visited):
                frontier.append(child)
                parents[child.get_state()] = node
                

    return 

def get_path(goal, parents):
    path = deque()
    path.append(goal)

    current_node = goal

    while(current_node is not None):
        current_node = parents[current_node.get_state()]
        if current_node is not None:
            path.appendleft(current_node)
    
    return path
