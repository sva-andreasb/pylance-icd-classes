def ():
    '''returns JsonParserDelegate\n\n
    (final JsonParser d)\n
    '''
def getCurrentValue():
    '''returns Object\n\n
    getCurrentValue()\n
    '''
def setCurrentValue():
    '''returns None\n\n
    setCurrentValue(final Object v)\n
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
def getFeatureMask():
    '''returns int\n\n
    getFeatureMask()\n
    '''
def setFeatureMask():
    '''returns JsonParser\n\n
    setFeatureMask(final int mask)\n
    '''
def overrideStdFeatures():
    '''returns JsonParser\n\n
    overrideStdFeatures(final int values, final int mask)\n
    '''
def overrideFormatFeatures():
    '''returns JsonParser\n\n
    overrideFormatFeatures(final int values, final int mask)\n
    '''
def getSchema():
    '''returns FormatSchema\n\n
    getSchema()\n
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
def requiresCustomCodec():
    '''returns boolean\n\n
    requiresCustomCodec()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
def currentToken():
    '''returns JsonToken\n\n
    currentToken()\n
    '''
def currentTokenId():
    '''returns int\n\n
    currentTokenId()\n
    '''
def getCurrentToken():
    '''returns JsonToken\n\n
    getCurrentToken()\n
    '''
def getCurrentTokenId():
    '''returns int\n\n
    getCurrentTokenId()\n
    '''
def hasCurrentToken():
    '''returns boolean\n\n
    hasCurrentToken()\n
    '''
def hasTokenId():
    '''returns boolean\n\n
    hasTokenId(final int id)\n
    '''
def hasToken():
    '''returns boolean\n\n
    hasToken(final JsonToken t)\n
    '''
def getCurrentName():
    '''returns String\n\n
    getCurrentName()\n
    '''
def getCurrentLocation():
    '''returns JsonLocation\n\n
    getCurrentLocation()\n
    '''
def getParsingContext():
    '''returns JsonStreamContext\n\n
    getParsingContext()\n
    '''
def isExpectedStartArrayToken():
    '''returns boolean\n\n
    isExpectedStartArrayToken()\n
    '''
def isExpectedStartObjectToken():
    '''returns boolean\n\n
    isExpectedStartObjectToken()\n
    '''
def isNaN():
    '''returns boolean\n\n
    isNaN()\n
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
def getText():
    '''returns int\n\n
    getText()\n
    getText(final Writer writer)\n
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
def nextToken():
    '''returns JsonToken\n\n
    nextToken()\n
    '''
def nextValue():
    '''returns JsonToken\n\n
    nextValue()\n
    '''
def finishToken():
    '''returns None\n\n
    finishToken()\n
    '''
def skipChildren():
    '''returns JsonParser\n\n
    skipChildren()\n
    '''
def canReadObjectId():
    '''returns boolean\n\n
    canReadObjectId()\n
    '''
def canReadTypeId():
    '''returns boolean\n\n
    canReadTypeId()\n
    '''
def getObjectId():
    '''returns Object\n\n
    getObjectId()\n
    '''
def getTypeId():
    '''returns Object\n\n
    getTypeId()\n
    '''
