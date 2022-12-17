PLAIN = "int  0"
SCIENTIFIC = "int  1"
ENGINEERING = "int  2"
ROUND_CEILING = "int  2"
ROUND_DOWN = "int  1"
ROUND_FLOOR = "int  3"
ROUND_HALF_DOWN = "int  5"
ROUND_HALF_EVEN = "int  6"
ROUND_HALF_UP = "int  4"
ROUND_UNNECESSARY = "int  7"
ROUND_UP = "int  0"
def ():
    '''returns MathContext\n\n
    (final int setdigits)\n
    (final int setdigits, final int setform)\n
    (final int setdigits, final int setform, final boolean setlostdigits)\n
    (final int setdigits, final int setform, final boolean setlostdigits, final int setroundingmode)\n
    '''
def getDigits():
    '''returns int\n\n
    getDigits()\n
    '''
def getForm():
    '''returns int\n\n
    getForm()\n
    '''
def getLostDigits():
    '''returns boolean\n\n
    getLostDigits()\n
    '''
def getRoundingMode():
    '''returns int\n\n
    getRoundingMode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
