def WriterBasedJsonGenerator():
    '''public WriterBasedJsonGenerator(final IOContext ctxt, final int features, final ObjectCodec codec, final Writer w)
    '''
def getOutputTarget():
    '''public Object getOutputTarget()
    '''
def getOutputBuffered():
    '''public int getOutputBuffered()
    '''
def canWriteFormattedNumbers():
    '''public boolean canWriteFormattedNumbers()
    '''
def writeFieldName():
    '''public void writeFieldName(final String name)
    public void writeFieldName(final SerializableString name)
    '''
def writeStartArray():
    '''public void writeStartArray()
    '''
def writeEndArray():
    '''public void writeEndArray()
    '''
def writeStartObject():
    '''public void writeStartObject(final Object forValue)
    public void writeStartObject()
    '''
def writeEndObject():
    '''public void writeEndObject()
    '''
def writeString():
    '''public void writeString(final String text)
    public void writeString(final Reader reader, final int len)
    public void writeString(final char[] text, final int offset, final int len)
    public void writeString(final SerializableString sstr)
    '''
def writeRawUTF8String():
    '''public void writeRawUTF8String(final byte[] text, final int offset, final int length)
    '''
def writeUTF8String():
    '''public void writeUTF8String(final byte[] text, final int offset, final int length)
    '''
def writeRaw():
    '''public void writeRaw(final String text)
    public void writeRaw(final String text, final int start, final int len)
    public void writeRaw(final SerializableString text)
    public void writeRaw(final char[] text, final int offset, final int len)
    public void writeRaw(final char c)
    '''
def writeBinary():
    '''public void writeBinary(final Base64Variant b64variant, final byte[] data, final int offset, final int len)
    public int writeBinary(final Base64Variant b64variant, final InputStream data, final int dataLength)
    '''
def writeNumber():
    '''public void writeNumber(final short s)
    public void writeNumber(final int i)
    public void writeNumber(final long l)
    public void writeNumber(final BigInteger value)
    public void writeNumber(final double d)
    public void writeNumber(final float f)
    public void writeNumber(final BigDecimal value)
    public void writeNumber(final String encodedValue)
    '''
def writeBoolean():
    '''public void writeBoolean(final boolean state)
    '''
def writeNull():
    '''public void writeNull()
    '''
def flush():
    '''public void flush()
    '''
def close():
    '''public void close()
    '''
