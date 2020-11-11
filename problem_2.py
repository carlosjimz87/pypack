def find_palindroms_str(input):
    if not isinstance(input, str):
        raise Exception("Input must be str")

    isPal = ''
    pals = []

    i = len(input)

    while(i > 0):
        isPal += input[:i]
        if isPal == isPal[::-1]:
            pals.append(isPal)
            input = input[i:]
            i = len(input)
        else:
            i -= 1
        isPal = ''

    return pals
