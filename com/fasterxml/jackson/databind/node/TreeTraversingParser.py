def ():
    '''returns TreeTraversingParser\n\n
    (final JsonNode n)\n
    (final JsonNode n, final ObjectCodec codec)\n
    '''
def setCodec():
    '''returns None\n\n
    setCodec(final ObjectCodec c)\n
    '''
def getCodec():
    '''returns ObjectCodec\n\n
    getCodec()\n
    '''
def version():
    '''returns Version\n\n
    version()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def nextToken():
    '''returns JsonToken\n\n
    nextToken()\n
    '''
def skipChildren():
    '''returns JsonParser\n\n
    skipChildren()\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
def getCurrentName():
    '''returns String\n\n
    getCurrentName()\n
    '''
def overrideCurrentName():
    '''returns None\n\n
    overrideCurrentName(final String name)\n
    '''
def getParsingContext():
    '''returns JsonStreamContext\n\n
    getParsingContext()\n
    '''
def getTokenLocation():
    '''returns JsonLocation\n\n
    getTokenLocation()\n
    '''
def getCurrentLocation():
    '''returns JsonLocation\n\n
    getCurrentLocation()\n
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
def hasTextCharacters():
    '''returns boolean\n\n
    hasTextCharacters()\n
    '''
def getBigIntegerValue():
    '''returns BigInteger\n\n
    getBigIntegerValue()\n
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
def getLongValue():
    '''returns long\n\n
    getLongValue()\n
    '''
def getIntValue():
    '''returns int\n\n
    getIntValue()\n
    '''
def getNumberValue():
    '''returns Number\n\n
    getNumberValue()\n
    '''
def getEmbeddedObject():
    '''returns Object\n\n
    getEmbeddedObject()\n
    '''
def isNaN():
    '''returns boolean\n\n
    isNaN()\n
    '''
def getBinaryValue():
    '''returns byte[]\n\n
    getBinaryValue(final Base64Variant b64variant)\n
    '''
def readBinaryValue():
    '''returns int\n\n
    readBinaryValue(final Base64Variant b64variant, final OutputStream out)\n
    '''
