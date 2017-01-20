from hmm import HMM

def print_emission_probabilities(testHMM, observation):
    print("Printing emission probabilities:")
    for state in testHMM.states:
        print("Emission probability of '%s' from state '%s': %s" % (observation, state, testHMM.emission_probability(state, observation)))

if __name__ == "__main__":
    # Empty HMM, P(a|B/I/O) = 0.0
    testHMM = HMM(states=['B','I','O'])
    print(testHMM)
    print_emission_probabilities(testHMM, 'a')
    
    # Add a few observations, P(a|B) = 1.0
    testHMM.add_observation('B', 'a')
    print_emission_probabilities(testHMM, 'a')
    
    # More, P(a|B) = P(b|B) = 0.5
    testHMM.add_observation('B', 'b')
    print_emission_probabilities(testHMM, 'a')
