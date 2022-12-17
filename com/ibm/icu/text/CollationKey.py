LOWER = "int  0"
UPPER = "int  1"
UPPER_LONG = "int  2"
COUNT = "int  3"
def ():
    '''returns CollationKey\n\n
    (final String source, final byte[] key)\n
    (final String source, final RawCollationKey key)\n
    '''
def getSourceString():
    '''returns String\n\n
    getSourceString()\n
    '''
def toByteArray():
    '''returns byte[]\n\n
    toByteArray()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final CollationKey target)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object target)\n
    equals(final CollationKey target)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def getBound():
    '''returns CollationKey\n\n
    getBound(final int boundType, int noOfLevels)\n
    '''
def merge():
    '''returns CollationKey\n\n
    merge(final CollationKey source)\n
    '''
