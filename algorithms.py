from state import State

def bfs(initial_state):
    if (initial_state.is_solution()):
        return initial_state
    
    frontier = list()
    explored = set()
    frontier.append(initial_state)
    while frontier:
        state = frontier.pop(0)
        if state.is_solution():
            return state
        explored.add(state)
        children = state.space_state()
        for child in children:
            if (child not in explored) or (child not in frontier):
                frontier.append(child)
    return 
