def NonBlockingJsonParserBase():
    '''public NonBlockingJsonParserBase(final IOContext ctxt, final int parserFeatures, final ByteQuadsCanonicalizer sym)
    '''
def getCodec():
    '''public ObjectCodec getCodec()
    '''
def setCodec():
    '''public void setCodec(final ObjectCodec c)
    '''
def canParseAsync():
    '''public boolean canParseAsync()
    '''
def getInputSource():
    '''public Object getInputSource()
    '''
def hasTextCharacters():
    '''public boolean hasTextCharacters()
    '''
def getCurrentLocation():
    '''public JsonLocation getCurrentLocation()
    '''
def getTokenLocation():
    '''public JsonLocation getTokenLocation()
    '''
def getText():
    '''public String getText()
    public int getText(final Writer writer)
    '''
def getValueAsString():
    '''public String getValueAsString()
    public String getValueAsString(final String defValue)
    '''
def getTextCharacters():
    '''public char[] getTextCharacters()
    '''
def getTextLength():
    '''public int getTextLength()
    '''
def getTextOffset():
    '''public int getTextOffset()
    '''
def getBinaryValue():
    '''public byte[] getBinaryValue(final Base64Variant b64variant)
    '''
def readBinaryValue():
    '''public int readBinaryValue(final Base64Variant b64variant, final OutputStream out)
    '''
def getEmbeddedObject():
    '''public Object getEmbeddedObject()
    '''
