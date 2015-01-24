def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alphabet = string.ascii_lowercase
    availableLetters = ''
    for char in alphabet:
        if not char in lettersGuessed:
            availableLetters += char
    return availableLetters

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getAvailableLetters(lettersGuessed)
#abcdfghjlmnoqtuvwxyz
