def ():
    '''returns JsonParserDelegate\n\n
    (final JsonParser d)\n
    '''
def setCodec():
    '''returns None\n\n
    setCodec(final ObjectCodec c)\n
    '''
def getCodec():
    '''returns ObjectCodec\n\n
    getCodec()\n
    '''
def enable():
    '''returns JsonParser\n\n
    enable(final Feature f)\n
    '''
def disable():
    '''returns JsonParser\n\n
    disable(final Feature f)\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled(final Feature f)\n
    '''
def setSchema():
    '''returns None\n\n
    setSchema(final FormatSchema schema)\n
    '''
def canUseSchema():
    '''returns boolean\n\n
    canUseSchema(final FormatSchema schema)\n
    '''
def version():
    '''returns Version\n\n
    version()\n
    '''
def getInputSource():
    '''returns Object\n\n
    getInputSource()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
def getCurrentToken():
    '''returns JsonToken\n\n
    getCurrentToken()\n
    '''
def hasCurrentToken():
    '''returns boolean\n\n
    hasCurrentToken()\n
    '''
def clearCurrentToken():
    '''returns None\n\n
    clearCurrentToken()\n
    '''
def getCurrentName():
    '''returns String\n\n
    getCurrentName()\n
    '''
def getCurrentLocation():
    '''returns JsonLocation\n\n
    getCurrentLocation()\n
    '''
def getLastClearedToken():
    '''returns JsonToken\n\n
    getLastClearedToken()\n
    '''
def getParsingContext():
    '''returns JsonStreamContext\n\n
    getParsingContext()\n
    '''
def getText():
    '''returns String\n\n
    getText()\n
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
def getBooleanValue():
    '''returns boolean\n\n
    getBooleanValue()\n
    '''
def getBigIntegerValue():
    '''returns BigInteger\n\n
    getBigIntegerValue()\n
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
def getBinaryValue():
    '''returns byte[]\n\n
    getBinaryValue(final Base64Variant b64variant)\n
    '''
def getEmbeddedObject():
    '''returns Object\n\n
    getEmbeddedObject()\n
    '''
def getTokenLocation():
    '''returns JsonLocation\n\n
    getTokenLocation()\n
    '''
def nextToken():
    '''returns JsonToken\n\n
    nextToken()\n
    '''
def skipChildren():
    '''returns JsonParser\n\n
    skipChildren()\n
    '''
