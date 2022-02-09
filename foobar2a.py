def solution(n, b):
    flag = 0            #flag for if duplicated element is in ID list
    id_array = []
    n = str(n)

    while flag != 1:                                #loops until finding a duplicate
        tmpID = str(idAlgorithm(n, b))
        if tmpID == '1':
            return 0
        if tmpID in id_array:
            flag = 1
            id_array.append(tmpID)
            break
        id_array.append(tmpID)
        n = tmpID

    index = id_array.index(tmpID) + 1              #goes to the original entry's index,
    counter = 1
    while index < len(id_array):
        if id_array[index] == tmpID:                #iterates until finding duplicate, counts steps and returns them
            break
        index += 1
        counter += 1

    return counter


def idAlgorithm(n, b):
    # 1 minion ID = n  ---- nonnegative int of length k ---- in base b
    # 2 x and y are int of length k ---- x is digits of n descending --- y is ascending
    # 3 z = x - y   ----- add leading zeroes to z to maintain length if needed
    # 4 n = z --- to get next ID ---- go back to step 2
    original_length = len(n)

    x = sorted(n, reverse=True)  # descending
    y = sorted(n, reverse=False)  # ascending

    x_string = "".join(x)  # makes list a string
    y_string = "".join(y)

    x_int = x_string  # makes strings to an int
    y_int = y_string

    if b != 10:                                 #base 10 case
        x_int2 = int(baseToDec(x_int, b))
        y_int2 = int(baseToDec(y_int, b))

        z = x_int2 - y_int2
        z2 = decToBase(z, b)
        n = z2  # step 4 -- this is next minion ID, repeat step 2
    else:
        x_int2 = int(x_int)                     #base not 10 case
        y_int2 = int(y_int)
        n = str(x_int2 - y_int2)

    if(len(n) < original_length):               #adds leading 0's if necessary
        final = '0' + n
        return final
    return n

def decToBase(num, base):   # done
    number = int(num)
    arr = []
    while number > 1:
        remainder = number % base
        arr.append(int(remainder))
        number = number / base                  #gets remainder of each, then adds to list, to form base x number

    reverse = (list(reversed(arr)))
    strn = ""
    for char in reverse:
        strn = strn + str(char)             # reverses list and then makes it into a string which is returned
    return strn

def baseToDec(number, base):    #done
    power = len(number) - 1
    total = 0

    for char in number:
        tmp = int(char) * (base ** power)
        total += tmp
        power -= 1
    return total
