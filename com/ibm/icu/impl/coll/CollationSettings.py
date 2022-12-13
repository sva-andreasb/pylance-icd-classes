CHECK_FCD = "int  1"
NUMERIC = "int  2"
CASE_FIRST = "int  512"
CASE_FIRST_AND_UPPER_MASK = "int  768"
CASE_LEVEL = "int  1024"
BACKWARD_SECONDARY = "int  2048"
def clone():
    '''public CollationSettings clone()
    '''
def equals():
    '''public boolean equals(final Object other)
    '''
def hashCode():
    '''public int hashCode()
    '''
def resetReordering():
    '''public void resetReordering()
    '''
def setReordering():
    '''public void setReordering(final CollationData data, final int[] codes)
    '''
def copyReorderingFrom():
    '''public void copyReorderingFrom(final CollationSettings other)
    '''
def hasReordering():
    '''public boolean hasReordering()
    '''
def reorder():
    '''public long reorder(final long p)
    '''
def setStrength():
    '''public void setStrength(final int value)
    '''
def setStrengthDefault():
    '''public void setStrengthDefault(final int defaultOptions)
    '''
def getStrength():
    '''public int getStrength()
    '''
def setFlag():
    '''public void setFlag(final int bit, final boolean value)
    '''
def setFlagDefault():
    '''public void setFlagDefault(final int bit, final int defaultOptions)
    '''
def getFlag():
    '''public boolean getFlag(final int bit)
    '''
def setCaseFirst():
    '''public void setCaseFirst(final int value)
    '''
def setCaseFirstDefault():
    '''public void setCaseFirstDefault(final int defaultOptions)
    '''
def getCaseFirst():
    '''public int getCaseFirst()
    '''
def setAlternateHandlingShifted():
    '''public void setAlternateHandlingShifted(final boolean value)
    '''
def setAlternateHandlingDefault():
    '''public void setAlternateHandlingDefault(final int defaultOptions)
    '''
def getAlternateHandling():
    '''public boolean getAlternateHandling()
    '''
def setMaxVariable():
    '''public void setMaxVariable(final int value, final int defaultOptions)
    '''
def getMaxVariable():
    '''public int getMaxVariable()
    '''
def dontCheckFCD():
    '''public boolean dontCheckFCD()
    '''
def isNumeric():
    '''public boolean isNumeric()
    '''
