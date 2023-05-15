from random import randint  # Do not delete this line


def displayIntro():
    print("""_______________________________________________
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
_______________________________________________
_____________________Rules_____________________
Try to guess the hidden word one letter at a   
time. The number of dashes are equivalent to   
the number of letters in the word. If a player 
suggests a letter that occurs in the word,     
blank places containing this character will be 
filled with that letter. If the word does not  
contain the suggested letter, one new element  
of a hangman’s gallow is painted. As the game  
progresses, a segment of a victim is added for 
every suggested letter not in the word. Goal is
to guess the word before the man hangs!        
_______________________________________________""")


def displayEnd(result):
    if result:
        print("""________________________________________________________________________
          _                                  _                          
         (_)                                (_)                         
__      ___ _ __  _ __   ___ _ __  __      ___ _ __  _ __   ___ _ __    
\ \ /\ / / | '_ \| '_ \ / _ \ '__| \ \ /\ / / | '_ \| '_ \ / _ \ '__|   
 \ V  V /| | | | | | | |  __/ |     \ V  V /| | | | | | | |  __/ |      
  \_/\_/ |_|_| |_|_| |_|\___|_|      \_/\_/ |_|_| |_|_| |_|\___|_|      
           | |   (_)    | |                  | (_)                      
        ___| |__  _  ___| | _____ _ __     __| |_ _ __  _ __   ___ _ __ 
       / __| '_ \| |/ __| |/ / _ \ '_ \   / _` | | '_ \| '_ \ / _ \ '__|
      | (__| | | | | (__|   <  __/ | | | | (_| | | | | | | | |  __/ |   
       \___|_| |_|_|\___|_|\_\___|_| |_|  \__,_|_|_| |_|_| |_|\___|_|   
________________________________________________________________________""")
    else:
        print(""" __     __           _           _   _                                    
 \ \   / /          | |         | | | |                                   
  \ \_/ /__  _   _  | | ___  ___| |_| |                                   
   \   / _ \| | | | | |/ _ \/ __| __| |                                   
    | | (_) | |_| | | | (_) \__ \ |_|_|                                   
    |_|\___/ \__,_| |_|\___/|___/\__(_)                                   
        _______ _                                        _ _          _ _ 
       |__   __| |                                      | (_)        | | |
          | |  | |__   ___   _ __ ___   __ _ _ __     __| |_  ___  __| | |
          | |  | '_ \ / _ \ | '_ ` _ \ / _` | '_ \   / _` | |/ _ \/ _` | |
          | |  | | | |  __/ | | | | | | (_| | | | | | (_| | |  __/ (_| |_|
          |_|  |_| |_|\___| |_| |_| |_|\__,_|_| |_|  \__,_|_|\___|\__,_(_)
__________________________________________________________________________""")


def displayHangman(state):
    if state == 5:
        print("""
        ._______.   
     |/          
     |           
     |           
     |           
     |           
     |           
 ____|___""")
    elif state == 4:
        print("""
        ._______.   
     |/      |   
     |           
     |           
     |           
     |           
     |           
 ____|___""")
    elif state == 3:
        print("""
        ._______.   
     |/      |   
     |      (_)  
     |           
     |           
     |           
     |           
 ____|___""")
    elif state == 2:
        print("""
        ._______.   
     |/      |   
     |      (_)  
     |       |   
     |       |   
     |           
     |           
 ____|___""")
    elif state == 1:
        print("""
        ._______.   
     |/      |   
     |      (_)  
     |      \|/  
     |       |   
     |           
     |           
 ____|___""")
    elif state == 0:
        print("""
        ._______.   
     |/      |   
     |      (_)  
     |      \|/  
     |       |   
     |      / \  
     |           
 ____|___""")


def getWord():
    words = []
    with open('hangman-words.txt', 'r') as file:
        for line in file:
            for word in line.split():
                words.append(word)
    return words[randint(0, len(words) - 1)]



def valid(c):
    return len(c) == 1 and c.isalpha() and c.islower()


def displayWord(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word


def play():
    word_to_guess = getWord()
    lives = 5
    current_word = ["_" for _ in range(len(word_to_guess))]

    while True:
        displayHangman(lives)
        print(" ".join(current_word))

        guess = input("Enter your guess: ")
        while not valid(guess):
            guess = input("Invalid input. Enter your guess: ")

        if guess in word_to_guess:
            for i, c in enumerate(word_to_guess):
                if c == guess:
                    current_word[i] = c
        else:
            lives -= 1

        if lives == 0:
            displayHangman(0)
            print("Hidden word was: " + word_to_guess)
            return False
        elif "_" not in current_word:
            print("Hidden word was: " + word_to_guess)
            return True


def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break


if __name__ == "__main__":
    hangman()
