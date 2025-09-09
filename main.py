# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player, data, calculate_tuple_freq_distribution
from unittest import main

# play(player, quincy, 100)
play(player, abbey, 20000)
# play(player, kris, 100)
# play(player, mrugesh, 100)


# Uncomment line below to play interactively against a bot:
# play(human, abbey, 20, verbose=True)

# Uncomment line below to play against a bot that plays randomly:
# play(human, random_player, 1000)



# Uncomment line below to run unit tests automatically
# main(module='test_module', exit=False)

# my tests

# from RPS import calculate_next_state, transition_matrix
# state_vector = [1/2, 1/4, 1/4]
# print(calculate_next_state(state_vector=state_vector, transition_matrix=transition_matrix))

#print(data["history"])
freq_d, freq_r = calculate_tuple_freq_distribution(data["history"])
print(freq_d)

print("proportions:")
print(freq_r)
