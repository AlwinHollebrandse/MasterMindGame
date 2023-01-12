from asyncio import constants
import random
import Constants

def makeRandomGuess():
    return [Constants.COLORS[random.randrange(len(Constants.COLORS))] for i in range(Constants.NUMBER_OF_COLUMNS)]

def getHumanGuess():
    guessList = input('Crack the Code: ').lower().strip().split(',')
    while len(guessList) != Constants.NUMBER_OF_COLUMNS or any(x not in Constants.COLORS for x in guessList):
        guessList = input('Crack the Code: ').lower().strip().split(',')
    # print('you guessed: ' + str(guessList))
    return guessList