PRIMARY = "int  0"
SECONDARY = "int  1"
TERTIARY = "int  2"
QUATERNARY = "int  3"
IDENTICAL = "int  15"
FULL_DECOMPOSITION = "int  15"
NO_DECOMPOSITION = "int  16"
CANONICAL_DECOMPOSITION = "int  17"
def setStrength():
    '''returns None\n\n
    setStrength(final int newStrength)\n
    '''
def setStrength2():
    '''returns Collator\n\n
    setStrength2(final int newStrength)\n
    '''
def setDecomposition():
    '''returns None\n\n
    setDecomposition(final int decomposition)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def getStrength():
    '''returns int\n\n
    getStrength()\n
    '''
def getDecomposition():
    '''returns int\n\n
    getDecomposition()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final String source, final String target)\n
    '''
def getTailoredSet():
    '''returns UnicodeSet\n\n
    getTailoredSet()\n
    '''
def compare():
    '''returns int\n\n
    compare(final Object source, final Object target)\n
    '''
def visible():
    '''returns boolean\n\n
    visible()\n
    '''
def createCollator():
    '''returns Collator\n\n
    createCollator(final ULocale loc)\n
    createCollator(final Locale loc)\n
    '''
def getDisplayName():
    '''returns String\n\n
    getDisplayName(final Locale objectLocale, final Locale displayLocale)\n
    getDisplayName(final ULocale objectLocale, final ULocale displayLocale)\n
    '''
