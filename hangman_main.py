import random
import hangman_word
import hangman_art

print(hangman_art.logo)
#Randoml choosing a word from the word_list and assiging it to a variable called choosen_word
chosen_word = random.choice(hangman_word.word_list) 

#creating a variable called 'lives' to keep track of the number of lives left
lives = 6

#creating an empty List called display and for each letter in the chosen_word, I am adding a "_" to display
display = []
for letter in chosen_word:
    display.append("_")

#Creating a variable to check if the game as ended
end_game = False

#Creating a while loop so that the user can guess again and the loop will only stop 
#if the user has guessed all the letters and 'display' has no more blanks or if the lives has reached 0
while not end_game:
    #Asking the user to guess a letter and assigning their answer to a variable called guess and making sure that guess is lowercase
    guess = (input("Guess a letter: ")).lower()
    
    #The user has entered a letter that they have already guessed.
    if guess in display:
      print(f"You've already guessed {guess}")

    #Checking if the letter the user guessed is one of the letters in the chosen word and then replacing the blank in display with that letter
    for index in range(0,len(display)):
        if chosen_word[index] == guess:
            display[index] = guess
    

    #condition to check if the guess is in chosen_word. If it is not , reduce number of lives.
    if guess not in chosen_word:
        print(f"You've guessed {guess}, that's not in the word. You've lost a life.")
        lives -= 1
        if lives == 0:
            end_game = True
            print("You Lose")
    #Join all the elements in the list and turn it into a string
    print(f"{' '.join(display)}")
    #This condition checks if all the blanks in the display list has been filled up indicating that the user has won.
    if "_" not in display:
        end_game = True
        print("You Win")
    
    
    
    #This prints the ASCII art from 'stages' that corresponds to the currect number of 'lives' the user has remaining
    print(hangman_art.stages[lives])
    
