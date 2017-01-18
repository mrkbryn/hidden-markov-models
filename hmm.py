import numpy as np

class HMM:
    """Represents a Hidden Markov Model"""
    
    def __init__(self, states):
        """Initialize a HMM with 0 observations for each state"""
        self.states = states
        # count transitions from state to state for transition probabilities
        # all entries initialized to 0, access as transition_counts[from_state][to_state]
        # transition_counts = [
        #   from_state_0:     [to_state_0, to_state1, ..., to_state_start, to_state_final],
        #   from_state_1:     [to_state_0, to_state1, ..., to_state_start, to_state_final],
        #     ...
        #   from_state_start:   ...
        #   from_state_final: [to_state_0, to_state1, ..., to_state_start, to_state_final],
        # ]
        self.transition_counts = np.zeros((len(self.states) + 2, len(self.states) + 2), dtype=np.int)
        # each state maintains a tuple with a dictionary of observations seen from that state along with the
        # total number of observations seen from that state. This will be used to calculate conditional probabilities
        # i.e. P(observing observation_x given state_y) = dict["observation_x"]/num_observations(state_y)
        # i.e. P(.) = dict["observation_x"]/observations_at_state_y
        self.observation_counts = [({},0)] * (len(self.states) + 2)
    
    def index_of_state(self, state):
        """Returns index of states that will be used to determine which entries in
        probability matrices correspond to state. Returns -1 if not a valid state."""
        if state == 'start':
            return len(self.states)
        elif state == 'final':
            return len(self.states) + 1
        
        # TODO: throw error here? InvalidStateException?
        return self.states.index(state) if state in self.states else -1
    
    def emission_probability(self, state, observation):
        pass
    
    def transition_probability(self, first_state, second_state):
        pass
    
    def __str__(self):
        return "HMM[states=%s]" % (str(self.states))
