from state import State
from collections import deque

def bfs(initial_node):
    if (initial_node.is_solution()):
        return initial_node
    
    frontier = list()
    explored = set() 
    id = 0
    initial_node.set_unique_id(id)
    frontier.append(initial_node)
    while frontier:
        node = frontier.pop(0)
        if node.is_solution():
            return get_path(node, explored)
        explored.add(node)
        children = node.space_state()
        for child in children:
            if (child not in explored) or (child not in frontier):
                child.set_parent(node.get_unique_id())
                id = id + 1
                child.set_unique_id(id)
                frontier.append(child)

    return 

def get_path(goal, explored):
    path = deque()
    path.append(goal)

    current_node = goal.get_parent()

    exit_while = False
    while(not exit_while):
        if current_node.get_parent() == False:
            exit_while = True
        path.append(current_node)
        current_node = explored[current_node.get_parent()]
        path.appendleft(current_node)
    
    return path
