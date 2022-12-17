def getInputSource():
    '''returns Object\n\n
    getInputSource()\n
    '''
def getCurrentValue():
    '''returns Object\n\n
    getCurrentValue()\n
    '''
def setCurrentValue():
    '''returns None\n\n
    setCurrentValue(final Object v)\n
    '''
def setRequestPayloadOnError():
    '''returns None\n\n
    setRequestPayloadOnError(final RequestPayload payload)\n
    setRequestPayloadOnError(final byte[] payload, final String charset)\n
    setRequestPayloadOnError(final String payload)\n
    '''
def setSchema():
    '''returns None\n\n
    setSchema(final FormatSchema schema)\n
    '''
def getSchema():
    '''returns FormatSchema\n\n
    getSchema()\n
    '''
def canUseSchema():
    '''returns boolean\n\n
    canUseSchema(final FormatSchema schema)\n
    '''
def requiresCustomCodec():
    '''returns boolean\n\n
    requiresCustomCodec()\n
    '''
def canParseAsync():
    '''returns boolean\n\n
    canParseAsync()\n
    '''
def getNonBlockingInputFeeder():
    '''returns NonBlockingInputFeeder\n\n
    getNonBlockingInputFeeder()\n
    '''
def releaseBuffered():
    '''returns int\n\n
    releaseBuffered(final OutputStream out)\n
    releaseBuffered(final Writer w)\n
    '''
def enable():
    '''returns JsonParser\n\n
    enable(final Feature f)\n
    '''
def disable():
    '''returns JsonParser\n\n
    disable(final Feature f)\n
    '''
def configure():
    '''returns JsonParser\n\n
    configure(final Feature f, final boolean state)\n
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
def getFormatFeatures():
    '''returns int\n\n
    getFormatFeatures()\n
    '''
def overrideFormatFeatures():
    '''returns JsonParser\n\n
    overrideFormatFeatures(final int values, final int mask)\n
    '''
def nextFieldName():
    '''returns String\n\n
    nextFieldName(final SerializableString str)\n
    nextFieldName()\n
    '''
def nextTextValue():
    '''returns String\n\n
    nextTextValue()\n
    '''
def nextIntValue():
    '''returns int\n\n
    nextIntValue(final int defaultValue)\n
    '''
def nextLongValue():
    '''returns long\n\n
    nextLongValue(final long defaultValue)\n
    '''
def nextBooleanValue():
    '''returns Boolean\n\n
    nextBooleanValue()\n
    '''
def finishToken():
    '''returns None\n\n
    finishToken()\n
    '''
def currentToken():
    '''returns JsonToken\n\n
    currentToken()\n
    '''
def currentTokenId():
    '''returns int\n\n
    currentTokenId()\n
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
def currentName():
    '''returns String\n\n
    currentName()\n
    '''
def getText():
    '''returns int\n\n
    getText(final Writer writer)\n
    '''
def getByteValue():
    '''returns byte\n\n
    getByteValue()\n
    '''
def getShortValue():
    '''returns short\n\n
    getShortValue()\n
    '''
def getBooleanValue():
    '''returns boolean\n\n
    getBooleanValue()\n
    '''
def getEmbeddedObject():
    '''returns Object\n\n
    getEmbeddedObject()\n
    '''
def getBinaryValue():
    '''returns byte[]\n\n
    getBinaryValue()\n
    '''
def readBinaryValue():
    '''returns int\n\n
    readBinaryValue(final OutputStream out)\n
    readBinaryValue(final Base64Variant bv, final OutputStream out)\n
    '''
def getValueAsInt():
    '''returns int\n\n
    getValueAsInt()\n
    getValueAsInt(final int def)\n
    '''
def getValueAsLong():
    '''returns long\n\n
    getValueAsLong()\n
    getValueAsLong(final long def)\n
    '''
def getValueAsDouble():
    '''returns double\n\n
    getValueAsDouble()\n
    getValueAsDouble(final double def)\n
    '''
def getValueAsBoolean():
    '''returns boolean\n\n
    getValueAsBoolean()\n
    getValueAsBoolean(final boolean def)\n
    '''
def getValueAsString():
    '''returns String\n\n
    getValueAsString()\n
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
def enabledByDefault():
    '''returns boolean\n\n
    enabledByDefault()\n
    '''
def enabledIn():
    '''returns boolean\n\n
    enabledIn(final int flags)\n
    '''
def getMask():
    '''returns int\n\n
    getMask()\n
    '''
