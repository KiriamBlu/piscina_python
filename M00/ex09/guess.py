import random

class Guess:
    def __init__(self):
        try:
            self.outputs = {
                "high": "Too high!",
                "low": "Too low!",
                "not_number": "That's not a number.",
                "win": "Congratulations, you've got it!\nYou won in {} attempts!",
                "42": "The answer to the ultimate question of life, the universe and everything is 42.",
                "first_t": "Congratulations! You got it on your first try!",
                "exit" : "Goodbye!"
            }
            self.dicti = ["high", "low", "not_number", "win", "42", "first_t", "exit"]
            self.number_of_attempts = 0
            guess = None
            self.random_number = random.randint(1, 99)
            guess_int = -1
            while guess_int != self.random_number and guess != "exit":
                guess = input("What's your guess between 1 and 99?\n>> ")
                if guess.strip():
                    self.number_of_attempts += 1
                    try:
                        guess_int = int(guess)
                    except ValueError:
                        guess_int = -1
                    p_values = self.parse(guess, guess_int)
                    if p_values is not None:
                        for elem in p_values:
                            print(self.outputs[elem] if elem != "win" else self.outputs[elem].format(self.number_of_attempts))

        except ValueError as v:
            print(v)

    def parse(self, guess, guess_int):
        print_values = []
        if guess == "exit":
            print_values.append(self.dicti[6])
        elif guess_int == -1:
            print_values.append(self.dicti[2])
            self.number_of_attempts -= 1
        elif guess_int > self.random_number:
            print_values.append(self.dicti[0])
        elif guess_int < self.random_number:
            print_values.append(self.dicti[1])
        if self.random_number == guess_int and guess == str(guess_int):
            if guess == "42":
                print_values.append(self.dicti[4])
            if self.number_of_attempts == 1:
                print_values.append(self.dicti[5])
            else:
                print_values.append(self.dicti[3])
        return print_values

Guess()
