import random

words = ['python','java','javascript','swift','csharp','ruby','kotlin']

#  random select

chose_word = random.choice(words)

word_display = ['_' for _ in chose_word]

attempts = 8 # Numnber of allowed attempts


print ('Welcome to Hangman')

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in chose_word:
        for index,letter in enumerate(chose_word):
            if letter == guess:
                word_display[index] = guess #reveal letter

    else:
        print("That letter doesnt appear in the word, Yedya !!!")
        attempts -= 1

# Game conclusion
if '_' not in word_display:
    print("You guessed the word !")
    print(' '.join(word_display))
    print("You survived !")
else:
    print("You ran out of attempts. The word was: "+chose_word)
    print("You lost!")