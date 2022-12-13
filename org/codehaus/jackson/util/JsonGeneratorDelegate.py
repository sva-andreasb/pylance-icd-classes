def JsonGeneratorDelegate():
    '''public JsonGeneratorDelegate(final JsonGenerator d)
    '''
def close():
    '''public void close()
    '''
def copyCurrentEvent():
    '''public void copyCurrentEvent(final JsonParser jp)
    '''
def copyCurrentStructure():
    '''public void copyCurrentStructure(final JsonParser jp)
    '''
def disable():
    '''public JsonGenerator disable(final Feature f)
    '''
def enable():
    '''public JsonGenerator enable(final Feature f)
    '''
def flush():
    '''public void flush()
    '''
def getCodec():
    '''public ObjectCodec getCodec()
    '''
def getOutputContext():
    '''public JsonStreamContext getOutputContext()
    '''
def setSchema():
    '''public void setSchema(final FormatSchema schema)
    '''
def canUseSchema():
    '''public boolean canUseSchema(final FormatSchema schema)
    '''
def version():
    '''public Version version()
    '''
def getOutputTarget():
    '''public Object getOutputTarget()
    '''
def isClosed():
    '''public boolean isClosed()
    '''
def isEnabled():
    '''public boolean isEnabled(final Feature f)
    '''
def setCodec():
    '''public JsonGenerator setCodec(final ObjectCodec oc)
    '''
def useDefaultPrettyPrinter():
    '''public JsonGenerator useDefaultPrettyPrinter()
    '''
def writeBinary():
    '''public void writeBinary(final Base64Variant b64variant, final byte[] data, final int offset, final int len)
    '''
def writeBoolean():
    '''public void writeBoolean(final boolean state)
    '''
def writeEndArray():
    '''public void writeEndArray()
    '''
def writeEndObject():
    '''public void writeEndObject()
    '''
def writeFieldName():
    '''public void writeFieldName(final String name)
    public void writeFieldName(final SerializedString name)
    public void writeFieldName(final SerializableString name)
    '''
def writeNull():
    '''public void writeNull()
    '''
def writeNumber():
    '''public void writeNumber(final int v)
    public void writeNumber(final long v)
    public void writeNumber(final BigInteger v)
    public void writeNumber(final double v)
    public void writeNumber(final float v)
    public void writeNumber(final BigDecimal v)
    public void writeNumber(final String encodedValue)
    '''
def writeObject():
    '''public void writeObject(final Object pojo)
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
def writeStartArray():
    '''public void writeStartArray()
    '''
def writeStartObject():
    '''public void writeStartObject()
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
def writeTree():
    '''public void writeTree(final JsonNode rootNode)
    '''
