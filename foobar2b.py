def solution(xs):
    highestNegative = -1000
    negativeCount = 0
    posCount = 0
    zeroCount = 0
    total = 1
    flag = 0

    if len(xs) > 1:
        cmp = xs[0]
        for char in xs:
            if char != cmp: flag = 0
            if char > 0: posCount += 1
            if char < 0: negativeCount += 1
            if char == 0: zeroCount += 1
        if flag == 1:
            for char in xs:
                total *= char
            total_str = str(total)
            print(xs)
            return total_str
        if posCount == 0 and negativeCount == 1 and zeroCount > 0:
            return "0"

        for char in xs:
            if char == 0:
                xs.remove(0)
            elif char < 0:
                if char > highestNegative:
                    highestNegative = char

    if (negativeCount % 2) != 0 and len(xs) > 1:
        xs.remove(highestNegative)

    for char in xs:
        total *= char
    total_str = str(total)
    return total_str
