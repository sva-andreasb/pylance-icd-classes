TIMEZONE_ICU = "int  0"
TIMEZONE_JDK = "int  1"
SHORT = "int  0"
LONG = "int  1"
SHORT_GENERIC = "int  2"
LONG_GENERIC = "int  3"
SHORT_GMT = "int  4"
LONG_GMT = "int  5"
SHORT_COMMONLY_USED = "int  6"
GENERIC_LOCATION = "int  7"
def getOffset():
    '''returns None\n\n
    getOffset(final long date)\n
    getOffset(long date, final boolean local, final int[] offsets)\n
    '''
def getID():
    '''returns String\n\n
    getID()\n
    '''
def setID():
    '''returns None\n\n
    setID(final String ID)\n
    '''
def getDisplayName():
    '''returns String\n\n
    getDisplayName(final boolean daylight, final int style, final Locale locale)\n
    getDisplayName(final boolean daylight, final int style, final ULocale locale)\n
    '''
def getDSTSavings():
    '''returns int\n\n
    getDSTSavings()\n
    '''
def hasSameRules():
    '''returns boolean\n\n
    hasSameRules(final TimeZone other)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
