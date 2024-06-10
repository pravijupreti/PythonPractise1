import random

def simulate_coin_flips(num_flips):
    outcomes = ["Heads", "Tails"]
    print(f"{num_flips} coin flips:")
    for _ in range(num_flips):
        result = random.choice(outcomes)
        print(result + "!")

# Simulate 5 coin flips
simulate_coin_flips(5)
