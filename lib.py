from typing import List, Optional, Tuple
from random import sample

digits = [str(x) for x in range(10)]

def genRandom() -> List[int]:
    return sample(range(10), 4)

def getChoice() -> Optional[List[int]]:
    while True:
        guess = input("Guess: ").strip()

        if guess == "exit":
            return None

        sGuess = set(guess)

        if len(sGuess) != 4 or len(sGuess.difference(digits)) != 0:
            print("Guess must be 4 unique digits")
            continue

        return [int(c) for c in guess]

def cmpLists(a: List[int], b: List[int]) -> Tuple[int, int]: # (cows, bulls)
    if a is b: return (0, 4)
    bulls = sum([v == b[i] for (i, v) in enumerate(a)])
    cows = len(set(a).intersection(b)) - bulls
    return (cows, bulls)

def main() -> None:
    iGuess, count = genRandom(), 0 # Internal Guess, Guess count

    while True:
        uGuess, count = getChoice(), count + 1 # User Guess, Increase count

        if not uGuess:
            print(''.join(iGuess))
            return

        details = cmpLists(iGuess, uGuess) # (cows, bulls)

        print(f"{details[0]} cows and {details[1]} bulls.")

        if details == (0, 4):
            print(f"Well Done! You guessed correctly in {count} guesses!")
            return

main()