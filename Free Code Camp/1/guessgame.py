secret_word = 'giraffe'
guess = ''
guess_count = 0
guess_limit = 3

while guess != secret_word:
    guess = input("Enter guess: ")
    guess_count += 1
    if secret_word == guess:
        print("You Win")
        break
    if guess_count == guess_limit:
        print("Try again")
        break
    