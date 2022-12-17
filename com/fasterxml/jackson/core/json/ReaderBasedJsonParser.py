def ():
    '''returns ReaderBasedJsonParser\n\n
    (final IOContext ctxt, final int features, final Reader r, final ObjectCodec codec, final CharsToNameCanonicalizer st, final char[] inputBuffer, final int start, final int end, final boolean bufferRecyclable)\n
    (final IOContext ctxt, final int features, final Reader r, final ObjectCodec codec, final CharsToNameCanonicalizer st)\n
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
    releaseBuffered(final Writer w)\n
    '''
def getInputSource():
    '''returns Object\n\n
    getInputSource()\n
    '''
def getText():
    '''returns int\n\n
    getText(final Writer writer)\n
    '''
def getBinaryValue():
    '''returns byte[]\n\n
    getBinaryValue(final Base64Variant b64variant)\n
    '''
def readBinaryValue():
    '''returns int\n\n
    readBinaryValue(final Base64Variant b64variant, final OutputStream out)\n
    '''
def finishToken():
    '''returns None\n\n
    finishToken()\n
    '''
def nextFieldName():
    '''returns String\n\n
    nextFieldName(final SerializableString sstr)\n
    nextFieldName()\n
    '''
def getTokenLocation():
    '''returns JsonLocation\n\n
    getTokenLocation()\n
    '''
def getCurrentLocation():
    '''returns JsonLocation\n\n
    getCurrentLocation()\n
    '''
