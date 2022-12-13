TOKENS_PER_SEGMENT = "int  16"
def TokenBuffer():
'''public TokenBuffer(final ObjectCodec codec)
'''
pass
def asParser():
'''public JsonParser asParser()
public JsonParser asParser(final ObjectCodec codec)
public JsonParser asParser(final JsonParser src)
'''
pass
def serialize():
'''public void serialize(final JsonGenerator jgen)
'''
pass
def toString():
'''public String toString()
'''
pass
def enable():
'''public JsonGenerator enable(final Feature f)
'''
pass
def disable():
'''public JsonGenerator disable(final Feature f)
'''
pass
def isEnabled():
'''public boolean isEnabled(final Feature f)
'''
pass
def useDefaultPrettyPrinter():
'''public JsonGenerator useDefaultPrettyPrinter()
'''
pass
def setCodec():
'''public JsonGenerator setCodec(final ObjectCodec oc)
public void setCodec(final ObjectCodec c)
'''
pass
def getCodec():
'''public ObjectCodec getCodec()
public ObjectCodec getCodec()
'''
pass
def getOutputContext():
'''public final JsonWriteContext getOutputContext()
'''
pass
def flush():
'''public void flush()
'''
pass
def close():
'''public void close()
public void close()
'''
pass
def isClosed():
'''public boolean isClosed()
public boolean isClosed()
'''
pass
def writeStartArray():
'''public final void writeStartArray()
'''
pass
def writeEndArray():
'''public final void writeEndArray()
'''
pass
def writeStartObject():
'''public final void writeStartObject()
'''
pass
def writeEndObject():
'''public final void writeEndObject()
'''
pass
def writeFieldName():
'''public final void writeFieldName(final String name)
public void writeFieldName(final SerializableString name)
public void writeFieldName(final SerializedString name)
'''
pass
def writeString():
'''public void writeString(final String text)
public void writeString(final char[] text, final int offset, final int len)
public void writeString(final SerializableString text)
'''
pass
def writeRawUTF8String():
'''public void writeRawUTF8String(final byte[] text, final int offset, final int length)
'''
pass
def writeUTF8String():
'''public void writeUTF8String(final byte[] text, final int offset, final int length)
'''
pass
def writeRaw():
'''public void writeRaw(final String text)
public void writeRaw(final String text, final int offset, final int len)
public void writeRaw(final char[] text, final int offset, final int len)
public void writeRaw(final char c)
'''
pass
def writeRawValue():
'''public void writeRawValue(final String text)
public void writeRawValue(final String text, final int offset, final int len)
public void writeRawValue(final char[] text, final int offset, final int len)
'''
pass
def writeNumber():
'''public void writeNumber(final int i)
public void writeNumber(final long l)
public void writeNumber(final double d)
public void writeNumber(final float f)
public void writeNumber(final BigDecimal dec)
public void writeNumber(final BigInteger v)
public void writeNumber(final String encodedValue)
'''
pass
def writeBoolean():
'''public void writeBoolean(final boolean state)
'''
pass
def writeNull():
'''public void writeNull()
'''
pass
def writeObject():
'''public void writeObject(final Object value)
'''
pass
def writeTree():
'''public void writeTree(final JsonNode rootNode)
'''
pass
def writeBinary():
'''public void writeBinary(final Base64Variant b64variant, final byte[] data, final int offset, final int len)
'''
pass
def copyCurrentEvent():
'''public void copyCurrentEvent(final JsonParser jp)
'''
pass
def copyCurrentStructure():
'''public void copyCurrentStructure(final JsonParser jp)
'''
pass
def Parser():
'''public Parser(final Segment firstSeg, final ObjectCodec codec)
'''
pass
def setLocation():
'''public void setLocation(final JsonLocation l)
'''
pass
def peekNextToken():
'''public JsonToken peekNextToken()
'''
pass
def nextToken():
'''public JsonToken nextToken()
'''
pass
def getParsingContext():
'''public JsonStreamContext getParsingContext()
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
def getCurrentName():
'''public String getCurrentName()
'''
pass
def getText():
'''public String getText()
'''
pass
def getTextCharacters():
'''public char[] getTextCharacters()
'''
pass
def getTextLength():
'''public int getTextLength()
'''
pass
def getTextOffset():
'''public int getTextOffset()
'''
pass
def hasTextCharacters():
'''public boolean hasTextCharacters()
'''
pass
def getBigIntegerValue():
'''public BigInteger getBigIntegerValue()
'''
pass
def getDecimalValue():
'''public BigDecimal getDecimalValue()
'''
pass
def getDoubleValue():
'''public double getDoubleValue()
'''
pass
def getFloatValue():
'''public float getFloatValue()
'''
pass
def getIntValue():
'''public int getIntValue()
'''
pass
def getLongValue():
'''public long getLongValue()
'''
pass
def getNumberType():
'''public NumberType getNumberType()
'''
pass
def getNumberValue():
'''public final Number getNumberValue()
'''
pass
def getEmbeddedObject():
'''public Object getEmbeddedObject()
'''
pass
def getBinaryValue():
'''public byte[] getBinaryValue(final Base64Variant b64variant)
'''
pass
def Segment():
'''public Segment()
'''
pass
def type():
'''public JsonToken type(final int index)
'''
pass
def get():
'''public Object get(final int index)
'''
pass
def next():
'''public Segment next()
'''
pass
def append():
'''public Segment append(final int index, final JsonToken tokenType)
public Segment append(final int index, final JsonToken tokenType, final Object value)
'''
pass
def set():
'''public void set(final int index, final JsonToken tokenType)
public void set(final int index, final JsonToken tokenType, final Object value)
'''
pass
