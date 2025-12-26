import random
import sys

correct_guesses: list[str] = []
all_words: list[str] = []


def load_game_words() -> None:
    global all_words

    try:
        with open("words.txt", "r") as words_file:
            for line in words_file.readlines():
                all_words.append(line.strip())
    except OSError as ose:
        sys.exit(f"ERROR: Could load words from 'words.txt': {ose.strerror}")


def choose_game_word() -> str:
    global all_words

    valid_game_words: list[str] = []
    for word in all_words:
        if len(word) == 7 and len(set(word)) == 7:
            valid_game_words.append(word)

    return random.choice(valid_game_words)


def mix(gameword: str) -> None:
    gameword_chars: list[str] = list(gameword)

    random.shuffle(gameword_chars)
    print(" ".join(gameword_chars))


def handle_score(gameword: str) -> int:
    global all_words, correct_guesses

    if gameword not in all_words or len(gameword) < 4 or gameword in correct_guesses:
        return 0

    correct_guesses.append(gameword)
    if len(gameword) == 4:
        return 1
    else:
        return len(gameword)


def main() -> None:
    global correct_guesses

    load_game_words()
    gameword: str = choose_game_word()
    score: int = 0

    mix(gameword)
    while True:
        user_input: str = input("> ").lower()
        match (user_input):
            case "mix":
                mix(gameword)
            case "ls":
                print(correct_guesses)
            case "bye":
                sys.exit("Thanks for playing!")
            case _:
                score += handle_score(user_input)
        print(f"Score: {score}")


if __name__ == "__main__":
    main()
