from algorithms import bfs
from state import State

def print_path(path):
    counter = 0
    for node in path:
        counter = counter + 1
        print("Step: ", counter, ": ", node.get_state())

def main():
    print('Welcome to missionaries and cannibals problem solving...')

    origin_state = State(3,3,1)
    print("Initial state:")
    origin_state.print()
    print("************************")

    path = bfs(origin_state)
    print_path(path)
        


if __name__ == "__main__":
    main()