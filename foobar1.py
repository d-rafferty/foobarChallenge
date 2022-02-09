def solution(s):
    length = len(s)
    increments = 1  # how far to split string for comparisons
    successes = 0  # how many comparisons succeeded

    while increments <= ((length / 2)):
        master_array = ''
        tmp_array = ''
        index = increments  # sets index for comparison iteration to where split stopped
        for char in s[0: increments: 1]:
            master_array += char  # adds the character(s) to an array, this number is decided by increments

        while index <= (length - increments):                      #loops checking against master array while making sure we don't step over end of array

            for char in s[index: (index + increments): 1]:
                tmp_array += char
            if tmp_array == master_array:
                successes += 1
                tmp_array = ''
                index = index + increments
                if (index >= length):
                    pieces = successes + 1                      #making x splits, always leaves an extra section at the end, so add one
                    return pieces
            else:
                increments += 1
                successes = 0
                break
    return 1
