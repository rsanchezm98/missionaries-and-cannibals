from algorithms import bfs
from state import State
from state import Node



def print_path(path):
    counter = 0
    for node in path:
        counter = counter + 1
        print("Step: ", counter, ": ", node.state().get_state())

def main():
    print('Welcome to missionaries and cannibals problem solving...')

    origin_state = State(3,3,1)
    print("Initial state:")
    origin_state.print()
    print("************************")

    state_space = origin_state.space_state()
    for i in range (0, len(state_space)):
        state_space[i].print()


    path = bfs(Node(origin_state, "NOT DEFINED"))
    print(path)


if __name__ == "__main__":
    main()