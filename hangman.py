import random
import hangman_ascii_art


class Hangman_Game:
  
  words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
  ascii_art = hangman_ascii_art.art
  
  def __init__(self):
    self.word = random.choice(self.words)
    self.letters_guessed = []
    self.wrong_guesses = 0
    self.lives = len(self.ascii_art)
    
  def make_guess(self, guessed_letter: str) -> bool:
    """Returns true if guess was correct, otherwise returns false.
    If the letter has already been guessed, raises AssertionError.
    """
    assert guessed_letter not in self.letters_guessed
    self.letters_guessed.append(guessed_letter)
    guess_correct = guessed_letter in self.word
    if not guess_correct:
      self.wrong_guesses += 1
    return guess_correct
    
  def display_word(self) -> str:
    return ' '.join([letter.upper() for letter in self.word if letter in self.letters_guessed else '_'])
    
  def display_guesses(self) -> str:
    return ', '.join(self.letters_guessed)
    
  def have_lives_left(self) -> bool:
    return self.wrong_guesses < self.lives
    
  def get_ascii_art(self) -> str:
    return self.ascii_art[self.wrong_guesses]
  
  def word_correct(self):
    for letter in self.word:
      if letter not in self.letters_guessed:
        return False
    return True

    
def main():
  game = Hangman_Game()
  print('Welcome to hangman!')
  while game.have_lives_left():
    print('\n\n')  # prints 2 new lines
    if game.letters_guessed:
      print(f"Guesses: {game.display_guesses()}")
    print(f'Your word is {game.display_word()}')
    print(game.get_ascii_art)
    game.make_guess(input('Guess a letter')
                    
    if game.word_correct():
      print('Congratulations, you won!')
      break
    if not game.have_lives_left():
      print('You lost :(')
      break

if __name__ == '__main__':
  main()
