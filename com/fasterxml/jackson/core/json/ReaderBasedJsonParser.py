def ReaderBasedJsonParser():
    '''public ReaderBasedJsonParser(final IOContext ctxt, final int features, final Reader r, final ObjectCodec codec, final CharsToNameCanonicalizer st, final char[] inputBuffer, final int start, final int end, final boolean bufferRecyclable)
    public ReaderBasedJsonParser(final IOContext ctxt, final int features, final Reader r, final ObjectCodec codec, final CharsToNameCanonicalizer st)
    '''
def getCodec():
    '''public ObjectCodec getCodec()
    '''
def setCodec():
    '''public void setCodec(final ObjectCodec c)
    '''
def releaseBuffered():
    '''public int releaseBuffered(final Writer w)
    '''
def getInputSource():
    '''public Object getInputSource()
    '''
def getText():
    '''public final String getText()
    public int getText(final Writer writer)
    '''
def getValueAsString():
    '''public final String getValueAsString()
    public final String getValueAsString(final String defValue)
    '''
def getTextCharacters():
    '''public final char[] getTextCharacters()
    '''
def getTextLength():
    '''public final int getTextLength()
    '''
def getTextOffset():
    '''public final int getTextOffset()
    '''
def getBinaryValue():
    '''public byte[] getBinaryValue(final Base64Variant b64variant)
    '''
def readBinaryValue():
    '''public int readBinaryValue(final Base64Variant b64variant, final OutputStream out)
    '''
def nextToken():
    '''public final JsonToken nextToken()
    '''
def finishToken():
    '''public void finishToken()
    '''
def nextFieldName():
    '''public boolean nextFieldName(final SerializableString sstr)
    public String nextFieldName()
    '''
def nextTextValue():
    '''public final String nextTextValue()
    '''
def nextIntValue():
    '''public final int nextIntValue(final int defaultValue)
    '''
def nextLongValue():
    '''public final long nextLongValue(final long defaultValue)
    '''
def nextBooleanValue():
    '''public final Boolean nextBooleanValue()
    '''
def getTokenLocation():
    '''public JsonLocation getTokenLocation()
    '''
def getCurrentLocation():
    '''public JsonLocation getCurrentLocation()
    '''
