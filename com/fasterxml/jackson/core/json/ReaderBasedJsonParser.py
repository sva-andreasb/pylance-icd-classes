def ReaderBasedJsonParser():
'''public ReaderBasedJsonParser(final IOContext ctxt, final int features, final Reader r, final ObjectCodec codec, final CharsToNameCanonicalizer st, final char[] inputBuffer, final int start, final int end, final boolean bufferRecyclable)
public ReaderBasedJsonParser(final IOContext ctxt, final int features, final Reader r, final ObjectCodec codec, final CharsToNameCanonicalizer st)
'''
pass
def getCodec():
'''public ObjectCodec getCodec()
'''
pass
def setCodec():
'''public void setCodec(final ObjectCodec c)
'''
pass
def releaseBuffered():
'''public int releaseBuffered(final Writer w)
'''
pass
def getInputSource():
'''public Object getInputSource()
'''
pass
def getText():
'''public final String getText()
public int getText(final Writer writer)
'''
pass
def getValueAsString():
'''public final String getValueAsString()
public final String getValueAsString(final String defValue)
'''
pass
def getTextCharacters():
'''public final char[] getTextCharacters()
'''
pass
def getTextLength():
'''public final int getTextLength()
'''
pass
def getTextOffset():
'''public final int getTextOffset()
'''
pass
def getBinaryValue():
'''public byte[] getBinaryValue(final Base64Variant b64variant)
'''
pass
def readBinaryValue():
'''public int readBinaryValue(final Base64Variant b64variant, final OutputStream out)
'''
pass
def nextToken():
'''public final JsonToken nextToken()
'''
pass
def finishToken():
'''public void finishToken()
'''
pass
def nextFieldName():
'''public boolean nextFieldName(final SerializableString sstr)
public String nextFieldName()
'''
pass
def nextTextValue():
'''public final String nextTextValue()
'''
pass
def nextIntValue():
'''public final int nextIntValue(final int defaultValue)
'''
pass
def nextLongValue():
'''public final long nextLongValue(final long defaultValue)
'''
pass
def nextBooleanValue():
'''public final Boolean nextBooleanValue()
'''
pass
def getTokenLocation():
'''public JsonLocation getTokenLocation()
'''
pass
def getCurrentLocation():
'''public JsonLocation getCurrentLocation()
'''
pass
