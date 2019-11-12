def run():
    printOptions()
    while True:
        i = input("Input: ")
        if i == '':
            print('Ok, thx, bye!')
            break
        elif i == 't':
            test()
        else:
            print(calculateNumber(i))

def printOptions():
    print("*** ROMAN NUMBER TRANSLATOR ***")
    print('')
    print("'t' to run test numbers")
    print('enter to exit')
    print('')

def test():
    realNumbers = ['I', 'III', 'IV', 'VI', 'VIII', 'IX', 'X', 'XI',
    'XV', 'XIV', 'XVI', 'XL', 'XLIV','LXXX','LXXXVIII','XC','XCIX','C',
    'CD','CDL','CDLXVI','DCLXXVIII','MCMXCVII','MM','MMMCMXCIX']
    print('testing real numbers:')
    for n in realNumbers:
        try:
            print(calculateNumber(n))
        except Exception as e:
            print(e)
    print("")
    wrongNumbers = ['IIII', 'IIV', 'IIX', 'XXXX', 'XVX', 'VX', 'XIL',
    'MDMD','LXLX','IVIV','VV','LL','DD','DXD','MMMM']
    print('testing invalid numbers:')
    for n in wrongNumbers:
        try:
            print(calculateNumber(n))
        except Exception as e:
            print(e)  

def calculateNumber(numberString):
    intArray = makeIntArray(numberString)
    startIndex = 0
    index = 0
    numbers = []
    final = 0
    maxNumber = 3001
    while True:
        if startIndex + index == len(intArray):
            final += doNumber(numbers, maxNumber)
            break

        number = intArray[startIndex + index]

        if index == 0:
            numbers.append(number)
            index += 1
            continue
        if numbers[0] > number:
            final += doNumber(numbers, maxNumber)
            startIndex = startIndex + index
            index = 0
            if firstDigit(numbers[0]) == '5':
                maxNumber = numbers[0] / 5 * 4
            numbers = []
            continue
        if index == 1:
            if firstDigit(numbers[0]) == '5':
                raise Exception('invalid number')
            if numbers[0]*10 == number or numbers[0]*5 == number:
                numbers.append(number)
                final += doNumber(numbers, maxNumber)
                maxNumber = numbers[0]
                startIndex = startIndex + index + 1
                index = 0
                numbers = []
                continue
            elif numbers[0] == number:
                numbers.append(number)
                index += 1
                continue
            else:
                raise Exception('invalid number')
        if index == 2:
            if numbers[1] == number:
                numbers.append(number)
                index += 1
                continue
            else:
                raise Exception('invalid number')
        if index == 3:
            raise Exception('invalid number')
    return final

def firstDigit(number):
    return str(number)[0]
        
def doNumber(numbers, maxNumber):
    final = 0
    if len(numbers) == 0:
        return final
    previous = numbers[0]
    for n in numbers:
        if previous < n:
            previous = n
            final = n - final
        else:
            previous = n
            final += n
        if final >= maxNumber:
            raise Exception('invalid number')
    return final

def makeIntArray(numberString):
    intArray = []
    for char in numberString:
        intArray.append(intValue(char))
    return intArray

def intValue(c):
    c = c.capitalize()
    if c == 'M':
        return 1000
    if c == 'D':
        return 500
    if c == 'C':
        return 100
    if c == 'L':
        return 50
    if c == 'X':
        return 10
    if c == 'V':
        return 5
    if c == 'I':
        return 1
    raise Exception('invalid character')

run()
