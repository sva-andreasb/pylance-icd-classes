def ():
    '''returns FilteringParserDelegate\n\n
    (final JsonParser p, final TokenFilter f, final boolean includePath, final boolean allowMultipleMatches)\n
    '''
def getFilter():
    '''returns TokenFilter\n\n
    getFilter()\n
    '''
def getMatchCount():
    '''returns int\n\n
    getMatchCount()\n
    '''
def getCurrentToken():
    '''returns JsonToken\n\n
    getCurrentToken()\n
    '''
def currentToken():
    '''returns JsonToken\n\n
    currentToken()\n
    '''
def hasCurrentToken():
    '''returns boolean\n\n
    hasCurrentToken()\n
    '''
def hasTokenId():
    '''returns boolean\n\n
    hasTokenId(final int id)\n
    '''
def isExpectedStartArrayToken():
    '''returns boolean\n\n
    isExpectedStartArrayToken()\n
    '''
def isExpectedStartObjectToken():
    '''returns boolean\n\n
    isExpectedStartObjectToken()\n
    '''
def getCurrentLocation():
    '''returns JsonLocation\n\n
    getCurrentLocation()\n
    '''
def getParsingContext():
    '''returns JsonStreamContext\n\n
    getParsingContext()\n
    '''
def getCurrentName():
    '''returns String\n\n
    getCurrentName()\n
    '''
def clearCurrentToken():
    '''returns None\n\n
    clearCurrentToken()\n
    '''
def getLastClearedToken():
    '''returns JsonToken\n\n
    getLastClearedToken()\n
    '''
def overrideCurrentName():
    '''returns None\n\n
    overrideCurrentName(final String name)\n
    '''
def nextToken():
    '''returns JsonToken\n\n
    nextToken()\n
    '''
def nextValue():
    '''returns JsonToken\n\n
    nextValue()\n
    '''
def skipChildren():
    '''returns JsonParser\n\n
    skipChildren()\n
    '''
def getText():
    '''returns String\n\n
    getText()\n
    '''
def hasTextCharacters():
    '''returns boolean\n\n
    hasTextCharacters()\n
    '''
def getTextCharacters():
    '''returns char[]\n\n
    getTextCharacters()\n
    '''
def getTextLength():
    '''returns int\n\n
    getTextLength()\n
    '''
def getTextOffset():
    '''returns int\n\n
    getTextOffset()\n
    '''
def getBigIntegerValue():
    '''returns BigInteger\n\n
    getBigIntegerValue()\n
    '''
def getBooleanValue():
    '''returns boolean\n\n
    getBooleanValue()\n
    '''
def getByteValue():
    '''returns byte\n\n
    getByteValue()\n
    '''
def getShortValue():
    '''returns short\n\n
    getShortValue()\n
    '''
def getDecimalValue():
    '''returns BigDecimal\n\n
    getDecimalValue()\n
    '''
def getDoubleValue():
    '''returns double\n\n
    getDoubleValue()\n
    '''
def getFloatValue():
    '''returns float\n\n
    getFloatValue()\n
    '''
def getIntValue():
    '''returns int\n\n
    getIntValue()\n
    '''
def getLongValue():
    '''returns long\n\n
    getLongValue()\n
    '''
def getNumberType():
    '''returns NumberType\n\n
    getNumberType()\n
    '''
def getNumberValue():
    '''returns Number\n\n
    getNumberValue()\n
    '''
def getValueAsInt():
    '''returns int\n\n
    getValueAsInt()\n
    getValueAsInt(final int defaultValue)\n
    '''
def getValueAsLong():
    '''returns long\n\n
    getValueAsLong()\n
    getValueAsLong(final long defaultValue)\n
    '''
def getValueAsDouble():
    '''returns double\n\n
    getValueAsDouble()\n
    getValueAsDouble(final double defaultValue)\n
    '''
def getValueAsBoolean():
    '''returns boolean\n\n
    getValueAsBoolean()\n
    getValueAsBoolean(final boolean defaultValue)\n
    '''
def getValueAsString():
    '''returns String\n\n
    getValueAsString()\n
    getValueAsString(final String defaultValue)\n
    '''
def getEmbeddedObject():
    '''returns Object\n\n
    getEmbeddedObject()\n
    '''
def getBinaryValue():
    '''returns byte[]\n\n
    getBinaryValue(final Base64Variant b64variant)\n
    '''
def readBinaryValue():
    '''returns int\n\n
    readBinaryValue(final Base64Variant b64variant, final OutputStream out)\n
    '''
def getTokenLocation():
    '''returns JsonLocation\n\n
    getTokenLocation()\n
    '''
