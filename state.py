from collections import deque

class State:
  def __init__(self, missionaries, cannibals, boat_side):
    self.missionaries = missionaries
    self.cannibals = cannibals
    self.boat_side = boat_side
  
  def get_state(self):
    return (self.missionaries, self.cannibals, self.boat_side)
    
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

  def is_solution(self):
    return self.missionaries == 0 and self.cannibals == 0 and self.boat_side == 0

  def space_state(self):
    new_states = deque()

    where_to_move = -1 # -1 means that the boat moves to the right and the left numbers is reduced
    if(self.boat_side == 0):
        where_to_move = 1 # we must change to the left, so its number increases

    # now we must compute the new states emerging from where we are and the valid ones
    for missionaries in range(0,3):
      for cannibals in range(0,3):
        new_state = State(self.missionaries + where_to_move*missionaries, self.cannibals + where_to_move*cannibals, self.boat_side + where_to_move)
        count_boat_travel = abs(where_to_move*missionaries) + abs(where_to_move*cannibals)
        if (new_state.is_valid_state() and count_boat_travel > 0 and count_boat_travel < 3):
            new_states.append(new_state)

    return new_states

  def print(self):
    print(self.get_state())

