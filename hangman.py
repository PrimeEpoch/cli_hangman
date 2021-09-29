import random
import hangman_ascii_art


class Hangman_Game:
  
  words = []
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

    
def main():
  pass
  
if __name__ == '__main__':
  main()
