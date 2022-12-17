CHECK_FCD = "int  1"
NUMERIC = "int  2"
CASE_FIRST = "int  512"
CASE_FIRST_AND_UPPER_MASK = "int  768"
CASE_LEVEL = "int  1024"
BACKWARD_SECONDARY = "int  2048"
def clone():
    '''returns CollationSettings\n\n
    clone()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def resetReordering():
    '''returns None\n\n
    resetReordering()\n
    '''
def setReordering():
    '''returns None\n\n
    setReordering(final CollationData data, final int[] codes)\n
    '''
def copyReorderingFrom():
    '''returns None\n\n
    copyReorderingFrom(final CollationSettings other)\n
    '''
def hasReordering():
    '''returns boolean\n\n
    hasReordering()\n
    '''
def reorder():
    '''returns long\n\n
    reorder(final long p)\n
    '''
def setStrength():
    '''returns None\n\n
    setStrength(final int value)\n
    '''
def setStrengthDefault():
    '''returns None\n\n
    setStrengthDefault(final int defaultOptions)\n
    '''
def getStrength():
    '''returns int\n\n
    getStrength()\n
    '''
def setFlag():
    '''returns None\n\n
    setFlag(final int bit, final boolean value)\n
    '''
def setFlagDefault():
    '''returns None\n\n
    setFlagDefault(final int bit, final int defaultOptions)\n
    '''
def getFlag():
    '''returns boolean\n\n
    getFlag(final int bit)\n
    '''
def setCaseFirst():
    '''returns None\n\n
    setCaseFirst(final int value)\n
    '''
def setCaseFirstDefault():
    '''returns None\n\n
    setCaseFirstDefault(final int defaultOptions)\n
    '''
def getCaseFirst():
    '''returns int\n\n
    getCaseFirst()\n
    '''
def setAlternateHandlingShifted():
    '''returns None\n\n
    setAlternateHandlingShifted(final boolean value)\n
    '''
def setAlternateHandlingDefault():
    '''returns None\n\n
    setAlternateHandlingDefault(final int defaultOptions)\n
    '''
def getAlternateHandling():
    '''returns boolean\n\n
    getAlternateHandling()\n
    '''
def setMaxVariable():
    '''returns None\n\n
    setMaxVariable(final int value, final int defaultOptions)\n
    '''
def getMaxVariable():
    '''returns int\n\n
    getMaxVariable()\n
    '''
def dontCheckFCD():
    '''returns boolean\n\n
    dontCheckFCD()\n
    '''
def isNumeric():
    '''returns boolean\n\n
    isNumeric()\n
    '''
