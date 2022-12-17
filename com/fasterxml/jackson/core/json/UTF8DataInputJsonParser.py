def ():
    '''returns UTF8DataInputJsonParser\n\n
    (final IOContext ctxt, final int features, final DataInput inputData, final ObjectCodec codec, final ByteQuadsCanonicalizer sym, final int firstByte)\n
    '''
def getCodec():
    '''returns ObjectCodec\n\n
    getCodec()\n
    '''
def setCodec():
    '''returns None\n\n
    setCodec(final ObjectCodec c)\n
    '''
def releaseBuffered():
    '''returns int\n\n
    releaseBuffered(final OutputStream out)\n
    '''
def getInputSource():
    '''returns Object\n\n
    getInputSource()\n
    '''
def getText():
    '''returns int\n\n
    getText()\n
    getText(final Writer writer)\n
    '''
def getValueAsString():
    '''returns String\n\n
    getValueAsString()\n
    getValueAsString(final String defValue)\n
    '''
def getValueAsInt():
    '''returns int\n\n
    getValueAsInt()\n
    getValueAsInt(final int defValue)\n
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
def getBinaryValue():
    '''returns byte[]\n\n
    getBinaryValue(final Base64Variant b64variant)\n
    '''
def readBinaryValue():
    '''returns int\n\n
    readBinaryValue(final Base64Variant b64variant, final OutputStream out)\n
    '''
def nextToken():
    '''returns JsonToken\n\n
    nextToken()\n
    '''
def finishToken():
    '''returns None\n\n
    finishToken()\n
    '''
def nextFieldName():
    '''returns String\n\n
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
def getTokenLocation():
    '''returns JsonLocation\n\n
    getTokenLocation()\n
    '''
def getCurrentLocation():
    '''returns JsonLocation\n\n
    getCurrentLocation()\n
    '''
