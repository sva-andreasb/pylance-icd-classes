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
def setFeature():
    '''returns None\n\n
    setFeature(final Feature f, final boolean state)\n
    '''
def enableFeature():
    '''returns None\n\n
    enableFeature(final Feature f)\n
    '''
def disableFeature():
    '''returns None\n\n
    disableFeature(final Feature f)\n
    '''
def nextValue():
    '''returns JsonToken\n\n
    nextValue()\n
    '''
def nextFieldName():
    '''returns boolean\n\n
    nextFieldName(final SerializableString str)\n
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
def getLastClearedToken():
    '''returns JsonToken\n\n
    getLastClearedToken()\n
    '''
def isExpectedStartArrayToken():
    '''returns boolean\n\n
    isExpectedStartArrayToken()\n
    '''
def hasTextCharacters():
    '''returns boolean\n\n
    hasTextCharacters()\n
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
def readValueAsTree():
    '''returns JsonNode\n\n
    readValueAsTree()\n
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
