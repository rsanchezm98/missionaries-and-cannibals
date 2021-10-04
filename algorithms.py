from state import State
from state import Node

def bfs(initial_node):
    if (initial_node.state.is_solution()):
        return initial_node
    
    frontier = list()
    explored = set()
    frontier.append(initial_node)
    while frontier:
        node = frontier.pop(0)
        if node.state.is_solution():
            return get_path(node, explored)
        explored.add(node)
        children = node.state.space_state()
        for child in children:
            if (child not in explored) or (child not in frontier):
                frontier.append(child)
    return 
