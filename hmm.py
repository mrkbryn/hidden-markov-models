
class HMM:
    """Represents a Hidden Markov Model"""
    
    def __init__(self, states):
        self.states = states
        
    def emission_probability(state, observation):
        pass
    
    def transition_probability(first_state,second_state):
        pass
        
    def __str__(self):
        return "HMM[states=%s]" % (str(self.states))


if __name__ == "__main__":
    testHMM = HMM(states=['B','I','O'])
    print testHMM

