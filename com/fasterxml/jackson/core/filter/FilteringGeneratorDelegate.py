def FilteringGeneratorDelegate():
    '''    public FilteringGeneratorDelegate(final JsonGenerator d, final TokenFilter f, final boolean includePath, final boolean allowMultipleMatches)
    '''
def getFilter():
    '''    public TokenFilter getFilter()
    '''
def getFilterContext():
    '''    public JsonStreamContext getFilterContext()
    '''
def getMatchCount():
    '''    public int getMatchCount()
    '''
def getOutputContext():
    '''    public JsonStreamContext getOutputContext()
    '''
def writeStartArray():
    '''    public void writeStartArray()
    public void writeStartArray(final int size)
    '''
def writeEndArray():
    '''    public void writeEndArray()
    '''
def writeStartObject():
    '''    public void writeStartObject()
    public void writeStartObject(final Object forValue)
    '''
def writeEndObject():
    '''    public void writeEndObject()
    '''
def writeFieldName():
    '''    public void writeFieldName(final String name)
    public void writeFieldName(final SerializableString name)
    '''
def writeString():
    '''    public void writeString(final String value)
    public void writeString(final char[] text, final int offset, final int len)
    public void writeString(final SerializableString value)
    '''
def writeRawUTF8String():
    '''    public void writeRawUTF8String(final byte[] text, final int offset, final int length)
    '''
def writeUTF8String():
    '''    public void writeUTF8String(final byte[] text, final int offset, final int length)
    '''
def writeRaw():
    '''    public void writeRaw(final String text)
    public void writeRaw(final String text, final int offset, final int len)
    public void writeRaw(final SerializableString text)
    public void writeRaw(final char[] text, final int offset, final int len)
    public void writeRaw(final char c)
    '''
def writeRawValue():
    '''    public void writeRawValue(final String text)
    public void writeRawValue(final String text, final int offset, final int len)
    public void writeRawValue(final char[] text, final int offset, final int len)
    '''
def writeBinary():
    '''    public void writeBinary(final Base64Variant b64variant, final byte[] data, final int offset, final int len)
    public int writeBinary(final Base64Variant b64variant, final InputStream data, final int dataLength)
    '''
def writeNumber():
    '''    public void writeNumber(final short v)
    public void writeNumber(final int v)
    public void writeNumber(final long v)
    public void writeNumber(final BigInteger v)
    public void writeNumber(final double v)
    public void writeNumber(final float v)
    public void writeNumber(final BigDecimal v)
    public void writeNumber(final String encodedValue)
    '''
def writeBoolean():
    '''    public void writeBoolean(final boolean v)
    '''
def writeNull():
    '''    public void writeNull()
    '''
def writeOmittedField():
    '''    public void writeOmittedField(final String fieldName)
    '''
def writeObjectId():
    '''    public void writeObjectId(final Object id)
    '''
def writeObjectRef():
    '''    public void writeObjectRef(final Object id)
    '''
def writeTypeId():
    '''    public void writeTypeId(final Object id)
    '''
