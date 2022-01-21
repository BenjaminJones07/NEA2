from typing import List, Optional, Set, Tuple
from random import sample

digits: Set[str] = {str(x) for x in range(10)}

def genRandom() -> List[int]:
    return sample(range(10), 4)

def getChoice() -> Optional[List[int]]:
    while True:
        guess: str = input("Guess: ").strip()

        if guess == "exit":
            return None

        sGuess: Set[int] = set(guess)

        # Verify guess is of length and only consists of digits 
        if len(guess) != 4 or len(sGuess) != 4 or len(sGuess.difference(digits)) != 0:
            print("Guess must be 4 unique digits")
            continue

        return [int(c) for c in guess]

def cmpLists(a: List[int], b: List[int]) -> Tuple[int, int]: # (cows, bulls)
    if a is b: return (0, 4) # Perfect guess
    bulls: List[int] = sum([v == b[i] for (i, v) in enumerate(a)]) # Find and count matching values
    cows: List[int] = len(set(a).intersection(b)) - bulls # Numbers in both sets - Numbers in correct place
    return (cows, bulls)

def main() -> None:
    count: int = 0 # Initialise guess count
    iGuess: List[int] = genRandom() # Internal Guess

    while True:
        count += 1
        uGuess: List[int] = getChoice() # User Guess

        if not uGuess:
            print(''.join(iGuess))
            return

        details: Tuple[int, int] = cmpLists(iGuess, uGuess) # (cows, bulls)

        if details == (0, 4):
            print(f"Well Done! You guessed correctly in {count} guesses!")
            return

        print(f"{details[0]} cows and {details[1]} bulls.")

if __name__ == "__main__": main()