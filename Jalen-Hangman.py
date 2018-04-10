import random
"""
1. make a word bank - 10 items
2. Select a random item to guess
3. take in a letter and add it to a list of letters_guessed
4. reveal letters based on input
5. create win a lose conditions
"""


word_bank = ["hi", "there", "if ", "you", "answer", "this", "you", "are", "cool", "bye",]
the_word = random.choice(word_bank)
print(random.choice(word_bank))
word_bank.append("supreme")
print(word_bank)
guess_taken = ''
letters_guessed = []
while guess_taken != 'end game':
    guess_taken = input("Guess a letter")