# Display a number in LED form


zero  = ('******', '*    *', '*    *', '*    *', '******')
one   = ('     *', '     *', '     *', '     *', '     *')
two   = ('******', '     *', '******', '*     ', '******')
three = ('******', '     *', '******', '     *', '******')
four  = ('*    *', '*    *', '******', '     *', '     *')
five  = ('******', '*     ', '******', '     *', '******')
six   = ('******', '*     ', '******', '*    *', '******')
seven = ('******', '     *', '     *', '     *', '     *')
eight = ('******', '*    *', '******', '*    *', '******')
nine  = ('******', '*    *', '******', '     *', '******')

printList = [zero, one, two, three, four, five, six, seven, eight, nine]

inputVal = int(input("Enter an Integer: "))
inputStr = str(inputVal)
inputDigits = [int(x) for x in inputStr]

#print (inputStr)
#print (inputDigits)

for column in range(5):
    result = ""
    for row in inputDigits:
        result += printList[row][column] + '   '
    print (result)