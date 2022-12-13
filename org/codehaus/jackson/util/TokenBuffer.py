TOKENS_PER_SEGMENT = "int  16"
def TokenBuffer():
    '''public TokenBuffer(final ObjectCodec codec)
    '''
def asParser():
    '''public JsonParser asParser()
    public JsonParser asParser(final ObjectCodec codec)
    public JsonParser asParser(final JsonParser src)
    '''
def serialize():
    '''public void serialize(final JsonGenerator jgen)
    '''
def toString():
    '''public String toString()
    '''
def enable():
    '''public JsonGenerator enable(final Feature f)
    '''
def disable():
    '''public JsonGenerator disable(final Feature f)
    '''
def isEnabled():
    '''public boolean isEnabled(final Feature f)
    '''
def useDefaultPrettyPrinter():
    '''public JsonGenerator useDefaultPrettyPrinter()
    '''
def setCodec():
    '''public JsonGenerator setCodec(final ObjectCodec oc)
    public void setCodec(final ObjectCodec c)
    '''
def getCodec():
    '''public ObjectCodec getCodec()
    public ObjectCodec getCodec()
    '''
def getOutputContext():
    '''public final JsonWriteContext getOutputContext()
    '''
def flush():
    '''public void flush()
    '''
def close():
    '''public void close()
    public void close()
    '''
def isClosed():
    '''public boolean isClosed()
    public boolean isClosed()
    '''
def writeStartArray():
    '''public final void writeStartArray()
    '''
def writeEndArray():
    '''public final void writeEndArray()
    '''
def writeStartObject():
    '''public final void writeStartObject()
    '''
def writeEndObject():
    '''public final void writeEndObject()
    '''
def writeFieldName():
    '''public final void writeFieldName(final String name)
    public void writeFieldName(final SerializableString name)
    public void writeFieldName(final SerializedString name)
    '''
def writeString():
    '''public void writeString(final String text)
    public void writeString(final char[] text, final int offset, final int len)
    public void writeString(final SerializableString text)
    '''
def writeRawUTF8String():
    '''public void writeRawUTF8String(final byte[] text, final int offset, final int length)
    '''
def writeUTF8String():
    '''public void writeUTF8String(final byte[] text, final int offset, final int length)
    '''
def writeRaw():
    '''public void writeRaw(final String text)
    public void writeRaw(final String text, final int offset, final int len)
    public void writeRaw(final char[] text, final int offset, final int len)
    public void writeRaw(final char c)
    '''
def writeRawValue():
    '''public void writeRawValue(final String text)
    public void writeRawValue(final String text, final int offset, final int len)
    public void writeRawValue(final char[] text, final int offset, final int len)
    '''
def writeNumber():
    '''public void writeNumber(final int i)
    public void writeNumber(final long l)
    public void writeNumber(final double d)
    public void writeNumber(final float f)
    public void writeNumber(final BigDecimal dec)
    public void writeNumber(final BigInteger v)
    public void writeNumber(final String encodedValue)
    '''
def writeBoolean():
    '''public void writeBoolean(final boolean state)
    '''
def writeNull():
    '''public void writeNull()
    '''
def writeObject():
    '''public void writeObject(final Object value)
    '''
def writeTree():
    '''public void writeTree(final JsonNode rootNode)
    '''
def writeBinary():
    '''public void writeBinary(final Base64Variant b64variant, final byte[] data, final int offset, final int len)
    '''
def copyCurrentEvent():
    '''public void copyCurrentEvent(final JsonParser jp)
    '''
def copyCurrentStructure():
    '''public void copyCurrentStructure(final JsonParser jp)
    '''
def Parser():
    '''public Parser(final Segment firstSeg, final ObjectCodec codec)
    '''
def setLocation():
    '''public void setLocation(final JsonLocation l)
    '''
def peekNextToken():
    '''public JsonToken peekNextToken()
    '''
def nextToken():
    '''public JsonToken nextToken()
    '''
def getParsingContext():
    '''public JsonStreamContext getParsingContext()
    '''
def getTokenLocation():
    '''public JsonLocation getTokenLocation()
    '''
def getCurrentLocation():
    '''public JsonLocation getCurrentLocation()
    '''
def getCurrentName():
    '''public String getCurrentName()
    '''
def getText():
    '''public String getText()
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
def hasTextCharacters():
    '''public boolean hasTextCharacters()
    '''
def getBigIntegerValue():
    '''public BigInteger getBigIntegerValue()
    '''
def getDecimalValue():
    '''public BigDecimal getDecimalValue()
    '''
def getDoubleValue():
    '''public double getDoubleValue()
    '''
def getFloatValue():
    '''public float getFloatValue()
    '''
def getIntValue():
    '''public int getIntValue()
    '''
def getLongValue():
    '''public long getLongValue()
    '''
def getNumberType():
    '''public NumberType getNumberType()
    '''
def getNumberValue():
    '''public final Number getNumberValue()
    '''
def getEmbeddedObject():
    '''public Object getEmbeddedObject()
    '''
def getBinaryValue():
    '''public byte[] getBinaryValue(final Base64Variant b64variant)
    '''
def Segment():
    '''public Segment()
    '''
def type():
    '''public JsonToken type(final int index)
    '''
def get():
    '''public Object get(final int index)
    '''
def next():
    '''public Segment next()
    '''
def append():
    '''public Segment append(final int index, final JsonToken tokenType)
    public Segment append(final int index, final JsonToken tokenType, final Object value)
    '''
def set():
    '''public void set(final int index, final JsonToken tokenType)
    public void set(final int index, final JsonToken tokenType, final Object value)
    '''
