questions = { 'Who invented Electric Bulb?':'A', 'Where is New York?':'C', 
'How many continents are there?':'C', 'Is Earth is round?':'B'}

# dictionary of questions and answers

options = [['A: Edison', 'B: Einstein', 'C: Tesla', 'D: Newton '], 
['A: South Africa', 'B: Vietnam', 'C: USA', 'D: Japan'],
['A: 3', 'B: 6', 'C: 7', 'D: 8'],
['A: No', 'B: Yes', 'C: Maybe', 'D: What is Earth?']]

# lists of options

def new_game():
    
        guesses = []                      # guesses list
        correct_guesses = 0                 # number correct guesses
        question_num = 1                        # question number
        for key in questions:
            print()
            print(question_num,'. ', key, sep='')        # printing questions
            print()
            for i in options[question_num-1]:
                print('  ', i)                       # printing options
            guess = input('\nEnter (A, B, C , or D): ').upper()           # inputing your answer
            guesses.append(guess)               # adding your answer to guesses list
            correct_guesses += check_guess(questions.get(key), guess)         # adding your correct answer to the correct guesses
            question_num += 1            # incrementing question numbers 
    
        display_score(guesses, correct_guesses)            # displaying scores by calling function
        play_again()                    


def check_guess(answer, guess):
    
    # checking the answers
    if answer == guess:            
        print('CORRECT!')    
        return 1
    else:
        print('WRONG :(')
        return 0
    
def display_score(guesses, correct_answer):

    # for displaying the answers and guesses
    
    print('\nYour answers: ', end ='')
    for i in guesses:
        print(i, sep= ' ', end = ' ')         # displaying your answers with space
    
    print('\n\ncorrect answers: ', end ='')
    for i in questions:
        print(questions.get(i), sep=' ', end=' ')             # displaying correct answers with space
    
    print()
    print('\nYour Score: ',correct_answer, '\n')             # displaying the score

def play_again():

    # for playing the quiz again
    
    play = input('Want to play again? (Y/N)').lower()
    if play == 'y':
        new_game()      # calling the game function again
    else:
        print('Byeee!')
        
    

    
new_game()

