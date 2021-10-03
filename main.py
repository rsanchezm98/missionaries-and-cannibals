from algorithms import bfs
from state import State

def print_path(path):
    for i in range (0,len(path)):
        print(i + " state: " + path[i].get_state())

def main():
    print('Welcome to missionaries and cannibals problem solving...')

    origin_state = State(3,3,1)
    print("Initial state:")
    origin_state.print()
    print("************************")

    state_space = origin_state.space_state()
    for i in range (0, len(state_space)):
        state_space[i].print()


    solution = bfs(origin_state)
    solution.print()


if __name__ == "__main__":
    main()