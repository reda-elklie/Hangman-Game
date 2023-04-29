from art import *
# print("""
# =================================================================================================================================================================
# ||                                                                                                                                                              ||
# ||                                                                Prenom : RIDA                                                                                 ||
# ||                                                                Nom    : EL KLIE                                                                              ||
# ||                                                                DEV    : 103                                                                                  ||
# ||                                                                                                                                                              ||  
# ||                                                                                                                                                              ||      
# ||                                                                                                                                                              ||
# ==================================================================================================================================================================
# """)
# tprint("hangman ",font="block",chr_ignore=True)
tprint("hangman",font="rnd-xlarge")



import random
from words import word_as_list

# function to import the word form the file
def im_words():
    word=random.choice(word_as_list)
    return word.upper()

def play(word):
    len_word ="_" * len(word)
    guessed =False
    guessed_letters=[] 
    guessed_words=[] 
    tries=6 

    print(display_hangman(tries))
    print(len_word)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Pleas guess a letter or word : ").upper() 
        # dakhal klma convert to uppercase
        if len(guess)==1 and guess.isalpha(): 
            # lettre condition
            if guess in guessed_letters: 
                # dakhal haref mara wehda
                print("You already guessed the letter",guess)
                # wrong guess
            elif guess not in word:
                print(guess,"is not in the word .")
                tries-=1 # tries = tries - 1
                guessed_letters.append(guess) 
                # bax maydakhalaxi mara akhera
            else:
                print("God job ! ",guess,"is in the word .")
                # bax maydakhalaxi mara akhera
                guessed_letters.append(guess)

                word_as_list = list(len_word)
                indices =[i for i,letter in enumerate(word) if letter==guess]
                # enumerate() function return the index and the value in list (word as list)
                for index in indices:
                    word_as_list[index]=guess
                len_word="".join(word_as_list)
                if "_" not in len_word:
                    guessed =True # correct guess
         # for word option 
        elif len(guess)==len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word ",guess)
            elif guess!=word:
                print(guess,"is not the word !")
                tries-=1
                guessed_words.append(guess)
            else:
                guessed=True # correct guess
                len_word=word
        else:
            print("Not a valide guesse ! ")
        print(display_hangman(tries))
        print(len_word)
        print("\n")
    if guessed: # True 
        tprint("Congratulations !! ")
        art("random") 
    else:
        print("Sorry , you ran out of tries , the word was -->",word )
        tprint(" Maybe next time ! ")

def display_hangman(tries):
    step =[ '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
 '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''
, '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========='''
, '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========='''
, '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========='''
,
 '''
  +---+
  |   |
  O   |
      |
      |
      |
========='''
,
        '''
  +---+
  |   |
      |
      |
      |
      |
=========''',
]
    return step[tries]
def main():
    word=im_words()
    play(word)
    while input("Play again ? (Yes or No) : ").upper()=="YES":
        word=im_words()
        play(word)

if __name__ == "__main__": 
    main() 


"""La construction if __name__ == "__main__":
peut être utilisée dans un certain nombre de situations où vous souhaitez contrôler
 l'exécution du code selon que le script est exécuté directement ou s'il est importé en tant que bibliothèque"""