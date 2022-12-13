def UTF8JsonGenerator():
    '''public UTF8JsonGenerator(final IOContext ctxt, final int features, final ObjectCodec codec, final OutputStream out)
    public UTF8JsonGenerator(final IOContext ctxt, final int features, final ObjectCodec codec, final OutputStream out, final byte[] outputBuffer, final int outputOffset, final boolean bufferRecyclable)
    '''
def getOutputTarget():
    '''public Object getOutputTarget()
    '''
def getOutputBuffered():
    '''public int getOutputBuffered()
    '''
def writeFieldName():
    '''public void writeFieldName(final String name)
    public void writeFieldName(final SerializableString name)
    '''
def writeStartArray():
    '''public final void writeStartArray()
    '''
def writeEndArray():
    '''public final void writeEndArray()
    '''
def writeStartObject():
    '''public final void writeStartObject()
    public void writeStartObject(final Object forValue)
    '''
def writeEndObject():
    '''public final void writeEndObject()
    '''
def writeString():
    '''public void writeString(final String text)
    public void writeString(final Reader reader, final int len)
    public void writeString(final char[] text, final int offset, final int len)
    public final void writeString(final SerializableString text)
    '''
def writeRawUTF8String():
    '''public void writeRawUTF8String(final byte[] text, final int offset, final int length)
    '''
def writeUTF8String():
    '''public void writeUTF8String(final byte[] text, final int offset, final int len)
    '''
def writeRaw():
    '''public void writeRaw(final String text)
    public void writeRaw(final String text, int offset, int len)
    public void writeRaw(final SerializableString text)
    public final void writeRaw(final char[] cbuf, int offset, int len)
    public void writeRaw(final char ch)
    '''
def writeRawValue():
    '''public void writeRawValue(final SerializableString text)
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
