defStrVersion = "String  \"x.x.x.x\""
defIntVersion = "int  0"
regEx = "String  \"\\p{XDigit}{1,4}\\.\\p{XDigit}{1,4}\\.\\p{XDigit}{1,4}\\.\\p{XDigit}{1,4}\""
def ():
    '''returns FileVersion\n\n
    ()\n
    (final String strVersion)\n
    (final long longVersion)\n
    '''
def setVersion():
    '''returns None\n\n
    setVersion(final long longVersion)\n
    setVersion(final String strVersion)\n
    '''
def getVersionAsLong():
    '''returns long\n\n
    getVersionAsLong()\n
    '''
def getVersionAsString():
    '''returns String\n\n
    getVersionAsString()\n
    '''
def isUpToDate():
    '''returns boolean\n\n
    isUpToDate(final FileVersion fileVersion)\n
    '''
