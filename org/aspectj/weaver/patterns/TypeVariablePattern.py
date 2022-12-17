def ():
    '''returns TypeVariablePattern\n\n
    (final String variableName)\n
    (final String variableName, final TypePattern upperBound)\n
    (final String variableName, final TypePattern upperLimit, final TypePattern[] interfaceBounds, final TypePattern lowerBound)\n
    '''
def accept():
    '''returns Object\n\n
    accept(final PatternNodeVisitor visitor, final Object data)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def isAnythingPattern():
    '''returns boolean\n\n
    isAnythingPattern()\n
    '''
def getRawTypePattern():
    '''returns TypePattern\n\n
    getRawTypePattern()\n
    '''
def getUpperBound():
    '''returns TypePattern\n\n
    getUpperBound()\n
    '''
def hasLowerBound():
    '''returns boolean\n\n
    hasLowerBound()\n
    '''
def getLowerBound():
    '''returns TypePattern\n\n
    getLowerBound()\n
    '''
def hasAdditionalInterfaceBounds():
    '''returns boolean\n\n
    hasAdditionalInterfaceBounds()\n
    '''
def getAdditionalInterfaceBounds():
    '''returns TypePattern[]\n\n
    getAdditionalInterfaceBounds()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
    '''
