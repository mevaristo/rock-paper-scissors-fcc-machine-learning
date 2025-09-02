import random

GUESS_DICT = {1: "R", 2: "P", 3: "S"}
data = { "history": [] }

state_vectors = {
    "quincy": [1/3, 1/3, 1/3],
    "abbey": [1/3, 1/3, 1/3],
    "chris": [1/3, 1/3, 1/3],
    "mrugesh": [1/3, 1/3, 1/3],
}

transition_matrix = [
    [1/3, 1/3, 1/3],
    [1/3, 1/3, 1/3],
    [1/3, 1/3, 1/3]
]

# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    data["history"] = opponent_history
    play = random.randint(1, 3)
    guess = GUESS_DICT[play]

    return guess

def calculate_next_state(state_vector: list, transition_matrix: list[list]) -> list:
    """
    Calculate the next state vector in a Markov Chain.
    """
    next_state = []

    n_states = len(state_vector)
    for i in range(n_states):
        next_state_i = 0
        for j in range(n_states):
            next_state_i += state_vector[i] * transition_matrix[i][j]
        next_state.append(next_state_i)

    return next_state

