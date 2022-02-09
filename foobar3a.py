import numpy as np
from fractions import Fraction
                                                #     I | O          I | O
def solution(m):                                #     R | Q         FR | O    F = (I - Q) ^-1
    if len(m) < 2:
        return [1, 1]
    rList, qList = matrixMath(m)
    fList = np.linalg.inv(np.subtract(np.identity(len(qList)), qList))      #identity is ones on the main diagonal.. subtracts and gets inverse to become F
    fr = np.dot(fList, rList)                           #multiplies the two arrays
    return getFractions(fr[0])

def matrixMath(m):
    terminals = []
    rList = []
    qList = []
    for row in range(len(m)):
        if sum(m[row]) == 0:
            terminals.append(row)      #checking if row absorbs
    for row in range(len(m)):
        if row not in terminals:                    #if doesn't absorb, create list of absolute odds
            total = float(sum(m[row]))
            rTemp = []
            qTemp = []
            for column in range(len(m[row])):
                temp = m[row][column]/total
                if column in terminals:
                    rTemp.append(temp)          #take value, divide by total in row, return value
                else:
                    qTemp.append(temp)
            rList.append(rTemp)
            qList.append(qTemp)
    return rList, qList

def getFractions(dec_list):
    fracList = []
    denominators = []

    for dec in dec_list:
        frac = Fraction(dec).limit_denominator()          #used for retaining floats???
        fracList.append(frac.numerator)
        denominators.append(frac.denominator)
    lcd = 1
    for denom in denominators:
        lcd = np.lcm(lcd, denom)

    for index in range(len(fracList)):
        fracList[index] *= int(lcd/denominators[index])

    fracList.append(lcd)
    return fracList
