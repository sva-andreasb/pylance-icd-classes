def WriterBasedGenerator():
    '''    public WriterBasedGenerator(final IOContext ctxt, final int features, final ObjectCodec codec, final Writer w)
    '''
def setHighestNonEscapedChar():
    '''    public JsonGenerator setHighestNonEscapedChar(final int charCode)
    '''
def getHighestEscapedChar():
    '''    public int getHighestEscapedChar()
    '''
def setCharacterEscapes():
    '''    public JsonGenerator setCharacterEscapes(final CharacterEscapes esc)
    '''
def getCharacterEscapes():
    '''    public CharacterEscapes getCharacterEscapes()
    '''
def getOutputTarget():
    '''    public Object getOutputTarget()
    '''
def writeFieldName():
    '''    public final void writeFieldName(final String name)
    public final void writeFieldName(final SerializedString name)
    public final void writeFieldName(final SerializableString name)
    '''
def writeStringField():
    '''    public final void writeStringField(final String fieldName, final String value)
    '''
def writeStartArray():
    '''    public final void writeStartArray()
    '''
def writeEndArray():
    '''    public final void writeEndArray()
    '''
def writeStartObject():
    '''    public final void writeStartObject()
    '''
def writeEndObject():
    '''    public final void writeEndObject()
    '''
def _writeFieldName():
    '''    public void _writeFieldName(final SerializableString name, final boolean commaBefore)
    '''
def writeString():
    '''    public void writeString(final String text)
    public void writeString(final char[] text, final int offset, final int len)
    public final void writeString(final SerializableString sstr)
    '''
def writeRawUTF8String():
    '''    public void writeRawUTF8String(final byte[] text, final int offset, final int length)
    '''
def writeUTF8String():
    '''    public void writeUTF8String(final byte[] text, final int offset, final int length)
    '''
def writeRaw():
    '''    public void writeRaw(final String text)
    public void writeRaw(final String text, final int start, final int len)
    public void writeRaw(final char[] text, final int offset, final int len)
    public void writeRaw(final char c)
    '''
def writeBinary():
    '''    public void writeBinary(final Base64Variant b64variant, final byte[] data, final int offset, final int len)
    '''
def writeNumber():
    '''    public void writeNumber(final int i)
    public void writeNumber(final long l)
    public void writeNumber(final BigInteger value)
    public void writeNumber(final double d)
    public void writeNumber(final float f)
    public void writeNumber(final BigDecimal value)
    public void writeNumber(final String encodedValue)
    '''
def writeBoolean():
    '''    public void writeBoolean(final boolean state)
    '''
def writeNull():
    '''    public void writeNull()
    '''
def flush():
    '''    public final void flush()
    '''
def close():
    '''    public void close()
    '''
