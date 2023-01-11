import random
import Constants


def main(): # TODO add help option to print rules
    print('You\'ll never crack my code!')
    print(Constants.COLORS)
    print('The length of the code is ' + str(Constants.NUMBER_OF_COLUMNS))
    board = createBoard()
    codeBreakerResponses = createBoard()
    answer = createAnswer()
    # print('answer: ' + str(answer))
    currentGuessAttempt = 0
    while currentGuessAttempt < Constants.MAX_NUMBER_OF_TURNS:
        guess = getGuess()
        board[currentGuessAttempt] = guess
        codeBreakerResponse = judgeGuess(guess, answer)
        if codeBreakerResponse == 0:
            print('CORRECT FINAL ANSWER!!!')
            print('Impossible! You\'ve defeated my brilliant code!')
            break
        codeBreakerResponses[currentGuessAttempt] = codeBreakerResponse
        printBoard(board, codeBreakerResponses)
        currentGuessAttempt += 1

    if currentGuessAttempt >= Constants.MAX_NUMBER_OF_TURNS:
        print('you lose, you\'re the worst code breaker')
    print('you took ' + str((currentGuessAttempt + 1)) + ' guess(es)') # 1 based to make more human readable
    print('answer: ' + str(answer))
    printBoard(board, codeBreakerResponses)


def getGuess():
    guessList = input('Crack the Code: ').lower().strip().split(',')
    while len(guessList) != Constants.NUMBER_OF_COLUMNS or any(x not in Constants.COLORS for x in guessList):
        guessList = input('Crack the Code: ').lower().strip().split(',')
    print('you guessed: ' + str(guessList))
    return guessList


def createBoard():
    board = [[0 for i in range(Constants.NUMBER_OF_COLUMNS)] for j in range(Constants.MAX_NUMBER_OF_TURNS)]
    return board


def createAnswer():
    answer = []
    for column in range(Constants.NUMBER_OF_COLUMNS):
        colorIndex = random.randrange(len(Constants.COLORS))
        answer.append(Constants.COLORS[colorIndex])
    return answer


def makeColorDict(colorList):
    dict = {}
    for color in colorList:
        if color not in dict:
            dict[color] = 0
        dict[color] += 1
    return dict


# "There is nothing about the placement of the Key Pegs to indicate which particular Code Pegs are meant." - rulebook
def judgeGuess(guess, answer):
    answerDict = makeColorDict(answer)

    feedback = []
    guessCopyNoCorrect = []
    numberOfCorrectGuesses = 0
    numberOfCorrectColors = 0
    for index, guessedColor in enumerate(guess): # get all exact matches
        if guessedColor == answer[index]:
            feedback.append('correct')
            numberOfCorrectGuesses += 1
            answerDict[guessedColor] -= 1
        else:
            guessCopyNoCorrect.append(guessedColor)

    for index, guessedColor in enumerate(guessCopyNoCorrect): # get remaining colors
        if guessedColor in answerDict and answerDict[guessedColor] > 0:
            numberOfCorrectColors += 1
            answerDict[guessedColor] -= 1

    # Red Peg = right color, right position
    # White peg = right color, wrong position
    for i in range(numberOfCorrectColors):
        feedback.append('color')

    for i in range(len(guess) - len(feedback)):
        feedback.append('wrong')

    if numberOfCorrectGuesses == len(guess):
        return 0

    random.shuffle(feedback)
    return feedback

def printBoard(board, codeBreakerResponses):
    for index, row in enumerate(board):
        print(str(row) + '      ' + str(codeBreakerResponses[index]))

if __name__ == "__main__":
    main()
