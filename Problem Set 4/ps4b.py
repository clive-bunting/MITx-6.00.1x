from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    best_score = 0

    # Create a new variable to store the best word seen so far (initially None)  
    best_word = None
    
    # For each word in the wordList
    for word in wordList:

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList):
            
            # Find out how much making that word is worth
            score = getWordScore(word, n)
            
            # If the score for that word is higher than your best score
            if score > best_score:

                # Update your best score, and best word accordingly
                best_score = score
                best_word = word 

    # return the best word you found.
    return best_word

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    current_hand = hand.copy()
    current_score = 0
    while True:
        print 'Current Hand: ',
        displayHand(current_hand)
        word = compChooseWord(current_hand, wordList, n)
        if word == None:
            break
        score = getWordScore(word, n)
        current_score += score
        print '"' + word + '" earned ' + str(score) + ' points. Total: ' + str(current_score) + ' points'
        current_hand = updateHand(current_hand, word)
        if calculateHandlen(current_hand) == 0:
            break
        print
    print 'Total score: ' + str(current_score) + ' points.'
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    hand = {}
    while True:
        option = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if option == 'n' or option == 'r':
            if option == 'r' and len(hand) == 0:
                print 'You have not played a hand yet. Please play a new hand first!'
            else:
                if option == 'n':
                    hand = dealHand(HAND_SIZE)
                while True:
                    user_or_computer = raw_input('Enter u to have yourself play, c to have the computer play: ')
                    if user_or_computer == 'u':
                        playHand(hand, wordList, HAND_SIZE)
                        break
                    elif user_or_computer == 'c':
                        compPlayHand(hand, wordList, HAND_SIZE)
                        break
                    else:
                        print 'Invalid command.'
        elif option == 'e':
            break
        else:
            print 'Invalid command.'

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


