import random
# Constants to be used in the implementation
WORD_LIST = ["lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"]
MAX_GUESS = 12
CHAR_PLACEHOLDER = '-'

def random_seed():
    seed = int(input("Random seed: "))
    random.seed(seed)

def get_word():
    word = random.choice(WORD_LIST)
    return word

def start(word):
    init_word = [CHAR_PLACEHOLDER] * len(word)
    return init_word

def print_current_guess(word):
    print("Word to guess: {}".format(" ".join(word)))


def print_instructions(word):
    print("The word you need to guess has {} characters".format(len(word)))

def process_guess(guessed_letters, num_of_guesses, guess,guess_word,secret_word):
    if guess in guessed_letters:
        print("You have already guessed that letter!")
    else:
        guessed_letters.add(guess)
        num_of_guesses += 1
        if guess in secret_word:
            print("You guessed correctly!")
            for i in range(0,len(secret_word)):
                if secret_word[i] == guess:
                    guess_word[i] = guess
        else: 
            print("The letter is not in the word!")
    return num_of_guesses



def play(secret_word,guess_word):
    guessed_letters = set()
    num_of_guesses = 0
    print_current_guess(guess_word)
    while num_of_guesses < MAX_GUESS:
        
        guess = input("Choose a letter: ").lower()
        num_of_guesses = process_guess(guessed_letters,num_of_guesses,guess, guess_word, secret_word)

        if CHAR_PLACEHOLDER not in guess_word:
            print("You won!")
            print_current_guess(secret_word)
            break
        else: 
            print("You are on guess {}/{}".format(num_of_guesses,MAX_GUESS))
            print_current_guess(guess_word)
    else:

        print("You lost! The secret word was",secret_word)


# Main program starts here
random_seed()
secret_word = get_word()
guess_word = start(secret_word)
print_instructions(guess_word)
play(secret_word, guess_word)






