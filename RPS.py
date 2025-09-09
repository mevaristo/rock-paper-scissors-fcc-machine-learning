import random
import math

QUINCY = 'quincy'
ABBEY = 'abbey'
KRIS = 'Kris'
MRUGESH = 'mrugesh'

ROCK = 'R'
PAPER = 'P'
SCISSORS = 'S'

ROCK_N = 0
PAPER_N = 1
SCISSORS_N = 2

EMPTY_PLAY = ''


GUESS = {0: ROCK, 1: PAPER, 2: SCISSORS}

OPPONENTS = {
    1: QUINCY,
    2: ABBEY,
    3: KRIS,
    4: MRUGESH
}

data = { "history": [] }


# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. 
# It is not a very good player so you will need to change the code to pass the challenge.


def player(prev_play, opponent_history=[]):
    # opponent = guess_opponent(prev_play)
    opponent = ABBEY
    
    opponent_history.append(prev_play)
    
    data["history"] = opponent_history
    play = CURRENT_STRATEGY(prev_play, opponent)
    guess = GUESS[play]
    print('prev:', prev_play)
    #guess = post_strategy(opponent, prev_play, guess)
    print('guess:', guess)
    # print("prev:", prev_play, "guess:", guess)

    return guess

def calculate_random_play(prev_play, opponent):
    return random.randint(0, 2)

def post_strategy(opponent, prev_play, guess):
    if opponent == ABBEY:
        if prev_play == ROCK:
            guess = PAPER
        if prev_play == PAPER:
            guess = SCISSORS if random.randint(0, 1) == 1 else PAPER
        if prev_play == SCISSORS:
            guess = ROCK if random.randint(0, 1) == 1 else SCISSORS
    return guess

def calculate_tuple_freq_distribution(freq_history: list[str]):
    rr = (ROCK, ROCK)
    rp = (ROCK, PAPER)
    rs = (ROCK, SCISSORS)

    pp = (PAPER, PAPER)
    ps = (PAPER, SCISSORS)
    pr = (PAPER, ROCK)

    ss = (SCISSORS, SCISSORS)
    sp = (SCISSORS, PAPER)
    sr = (SCISSORS, ROCK)

    freq_dict = {
        rr: 0,
        rp: 0,
        rs: 0,

        pp: 0,
        ps: 0,
        pr: 0,

        ss: 0,
        sp: 0,
        sr: 0
    }

    # frequency relative by row
    freq_relative = {
        rr: 0,
        rp: 0,
        rs: 0,

        pp: 0,
        ps: 0,
        pr: 0,

        ss: 0,
        sp: 0,
        sr: 0
    }

    for i in range(1, len(freq_history) - 1):
        freq_dict[(freq_history[i], freq_history[i+1])] += 1

    rock_row = freq_dict[rr] + freq_dict[rp] + freq_dict[rs]
    paper_row = freq_dict[pp] + freq_dict[ps] + freq_dict[pr]
    scissors_row = freq_dict[ss] + freq_dict[sp] + freq_dict[sr]

    for i in [rr, rp, rs]:
        freq_relative[i] = freq_dict[i]/rock_row if rock_row != 0 else 0

    for i in [pp, ps, pr]:
        freq_relative[i] = freq_dict[i]/paper_row if paper_row != 0 else 0

    for i in [ss, sp, sr]:
        freq_relative[i] = freq_dict[i]/scissors_row if scissors_row != 0 else 0


    return freq_dict, freq_relative



empty_plays = 0
def guess_opponent(prev_play: str) -> str:
    global empty_plays
    if prev_play == EMPTY_PLAY:
        empty_plays += 1
    return OPPONENTS[empty_plays]




class MarkovChainPlayer:
    def __init__(self):
        self.state_vectors = {
            QUINCY: [1/3, 1/3, 1/3],
            ABBEY: [1/3, 1/3, 1/3],
            KRIS: [1/3, 1/3, 1/3],
            MRUGESH: [1/3, 1/3, 1/3],
        }

        self.state_map = {
            ROCK: [1, 0, 0],
            PAPER: [0, 1, 0],
            SCISSORS: [0, 0, 1]
        }

        """     R        P       S
            R   [R->R,  ...,    ...],
            P   [P->R,  ...,    ...],
            S   [...,   ...,    ...]
        """
        self.transition_matrices = {
            QUINCY: [
                # quincy = {
                # ('R', 'R'): 1999, ('R', 'P'): 2000, ('R', 'S'): 0, 
                # ('P', 'P'): 2000, ('P', 'S'): 2000, ('P', 'R'): 0, 
                # ('S', 'S'): 0, ('S', 'P'): 0, ('S', 'R'): 1999}
                # quincy starts with rock everytime and follows a fixed pattern
                [0.5, 0.5, 0  ],
                [0,   0.5, 0.5],
                [1,   0,   0  ]
                ],
            ABBEY: [
                # abbey = {
                # 10m run directly with proportions
                # ('R', 'R'): 6171559, 
                # ('R', 'P'): 864101, 
                # ('R', 'S'): 80526, 
                # ('P', 'P'): 863517, 
                # ('P', 'S'): 321601, 
                # ('P', 'R'): 863783, 
                # ('S', 'S'): 432784, 
                # ('S', 'P'): 321282, 
                # ('S', 'R'): 80845}
                # proportions:
                # ('R', 'R'): 0.8672565613096679, ('R', 'P'): 0.12142754559816171, ('R', 'S'): 0.01131589309217044, 
                # ('P', 'P'): 0.4214537452029161, ('P', 'S'): 0.15696268389736742, ('P', 'R'): 0.4215835708997165, 
                # ('S', 'S'): 0.5183594419045863, ('S', 'P'): 0.3848098779390857, ('S', 'R'): 0.09683068015632804}
                [0.867, 0.121, 0.012],
                [0.42, 0.157, 0.423],
                [0.518, 0.384, 0.098]
                ],
            KRIS: [[]],
            MRUGESH: [[]]
        }

        
    def decide_play_by_state_vector(self, state_vector: list[float]) -> str:
        vector_max = -math.inf
        guess_index = 0
        for i in range(len(state_vector)):
            if state_vector[i] > vector_max:
                vector_max = state_vector[i]
                guess_index = i
            # if state_vector[i] == vector_max and there is a tie, I will just ignore, making the guess the first one encountered as the decided play
        # guess index represents what opponent will play, so I should make a counter-play
        return (guess_index + 1) % 3

    def calculate_markov_chain_play(self, prev_play: str, opponent: str) -> str:
        if prev_play == EMPTY_PLAY:
            if opponent == QUINCY:
                return PAPER_N
            if opponent == ABBEY:
                return SCISSORS_N
        
        self.state_vectors[opponent] = self.calculate_next_state(self.map_current_state(prev_play), self.transition_matrices[opponent])

        print(self.state_vectors[opponent])
        return self.decide_play_by_state_vector(self.state_vectors[opponent])

    def map_current_state(self, prev_play):
        return self.state_map[prev_play]

    def calculate_next_state(self, state_vector: list, transition_matrix: list[list]) -> list:
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


markov_chain_player = MarkovChainPlayer()

    

STRATEGY_RANDOM = calculate_random_play
STRATEGY_MARKOV_CHAIN = markov_chain_player.calculate_markov_chain_play

CURRENT_STRATEGY = STRATEGY_MARKOV_CHAIN