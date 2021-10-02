from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat_side):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat_side = boat side
    
    def is_valid_state(self):
		if self.missionaries < 0 or self.missionaries > 3:
			return False
		if self.cannibals < 0 or self.cannibals > 3:
			return False
		if self.missionaries < self.cannibals and self.missionaries > 0:
			return False
		if self.missionaries > self.cannibals and self.missionaries < 3 :
			return False

		return True  

    def is_goal(self):
		return self.missionaries == 0 and self.cannibals == 0 and self.boat_side == 0

    def space_state(self):
        new_states_dict = deque()

        where_to_move = -1 # -1 means that the boat moves to the right and the left numbers is reduced
        if(self.boat_side):
            where_to_move = 1 # we must change to the left, so its number increases

        # now we must compute the new states emerging from where we are and the valid ones
        for missionaries, cannibals in 3,3:
            new_state = State(self.missionaries + where_to_move*missionaries, self.cannibals + where_to_move*cannibals, self.boat_side -where_to_move)
            if (new_states.is_valid_state()):
                new_states_dict.append(new_state)

