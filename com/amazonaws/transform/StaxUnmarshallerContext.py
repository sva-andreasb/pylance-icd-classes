def setCurrentHeader():
    '''returns None\n\n
    setCurrentHeader(final String currentHeader)\n
    '''
def isInsideResponseHeader():
    '''returns boolean\n\n
    isInsideResponseHeader()\n
    '''
def ():
    '''returns MetadataExpression\n\n
    (final XMLEventReader eventReader)\n
    (final XMLEventReader eventReader, final Map<String, String> headers)\n
    (final String expression, final int targetDepth, final String key)\n
    '''
def getHeader():
    '''returns String\n\n
    getHeader(final String header)\n
    '''
def readText():
    '''returns String\n\n
    readText()\n
    '''
def getCurrentDepth():
    '''returns int\n\n
    getCurrentDepth()\n
    '''
def testExpression():
    '''returns boolean\n\n
    testExpression(final String expression)\n
    testExpression(final String expression, int startingStackDepth)\n
    '''
def isStartOfDocument():
    '''returns boolean\n\n
    isStartOfDocument()\n
    '''
def nextEvent():
    '''returns XMLEvent\n\n
    nextEvent()\n
    '''
def registerMetadataExpression():
    '''returns None\n\n
    registerMetadataExpression(final String expression, final int targetDepth, final String storageKey)\n
    '''
