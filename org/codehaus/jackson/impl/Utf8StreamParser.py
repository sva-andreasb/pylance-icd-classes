def ():
    '''returns Utf8StreamParser\n\n
    (final IOContext ctxt, final int features, final InputStream in, final ObjectCodec codec, final BytesToNameCanonicalizer sym, final byte[] inputBuffer, final int start, final int end, final boolean bufferRecyclable)\n
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
def getBinaryValue():
    '''returns byte[]\n\n
    getBinaryValue(final Base64Variant b64variant)\n
    '''
def nextToken():
    '''returns JsonToken\n\n
    nextToken()\n
    '''
def close():
    '''returns None\n\n
    close()\n
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
