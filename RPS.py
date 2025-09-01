import random
GUESS_DICT = {1: "R", 2: "P", 3: "S"}
data = { "history": [] }
# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.


def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    data["history"] = opponent_history
    play = random.randint(1, 3)
    guess = GUESS_DICT[play]

    return guess
