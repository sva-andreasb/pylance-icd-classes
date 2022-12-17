FLAG_NEGATIVE = "int  1"
FLAG_PERCENT = "int  2"
FLAG_PERMILLE = "int  4"
FLAG_HAS_EXPONENT = "int  8"
FLAG_HAS_DECIMAL_SEPARATOR = "int  32"
FLAG_NAN = "int  64"
FLAG_INFINITY = "int  128"
FLAG_FAIL = "int  256"
def ():
    '''returns ParsedNumber\n\n
    ()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def copyFrom():
    '''returns None\n\n
    copyFrom(final ParsedNumber other)\n
    '''
def setCharsConsumed():
    '''returns None\n\n
    setCharsConsumed(final StringSegment segment)\n
    '''
def postProcess():
    '''returns None\n\n
    postProcess()\n
    '''
def success():
    '''returns boolean\n\n
    success()\n
    '''
def seenNumber():
    '''returns boolean\n\n
    seenNumber()\n
    '''
def getNumber():
    '''returns Number\n\n
    getNumber()\n
    getNumber(final int parseFlags)\n
    '''
def compare():
    '''returns int\n\n
    compare(final ParsedNumber o1, final ParsedNumber o2)\n
    '''
