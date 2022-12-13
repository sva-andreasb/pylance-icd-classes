def Utf8Generator():
'''public Utf8Generator(final IOContext ctxt, final int features, final ObjectCodec codec, final OutputStream out)
public Utf8Generator(final IOContext ctxt, final int features, final ObjectCodec codec, final OutputStream out, final byte[] outputBuffer, final int outputOffset, final boolean bufferRecyclable)
'''
pass
def setHighestNonEscapedChar():
'''public JsonGenerator setHighestNonEscapedChar(final int charCode)
'''
pass
def getHighestEscapedChar():
'''public int getHighestEscapedChar()
'''
pass
def setCharacterEscapes():
'''public JsonGenerator setCharacterEscapes(final CharacterEscapes esc)
'''
pass
def getCharacterEscapes():
'''public CharacterEscapes getCharacterEscapes()
'''
pass
def getOutputTarget():
'''public Object getOutputTarget()
'''
pass
def writeStringField():
'''public final void writeStringField(final String fieldName, final String value)
'''
pass
def writeFieldName():
'''public final void writeFieldName(final String name)
public final void writeFieldName(final SerializedString name)
public final void writeFieldName(final SerializableString name)
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
def writeString():
'''public void writeString(final String text)
public void writeString(final char[] text, final int offset, final int len)
public final void writeString(final SerializableString text)
'''
pass
def writeRawUTF8String():
'''public void writeRawUTF8String(final byte[] text, final int offset, final int length)
'''
pass
def writeUTF8String():
'''public void writeUTF8String(final byte[] text, final int offset, final int len)
'''
pass
def writeRaw():
'''public void writeRaw(final String text)
public void writeRaw(final String text, int offset, int len)
public final void writeRaw(final char[] cbuf, int offset, int len)
public void writeRaw(final char ch)
'''
pass
def writeBinary():
'''public void writeBinary(final Base64Variant b64variant, final byte[] data, final int offset, final int len)
'''
pass
def writeNumber():
'''public void writeNumber(final int i)
public void writeNumber(final long l)
public void writeNumber(final BigInteger value)
public void writeNumber(final double d)
public void writeNumber(final float f)
public void writeNumber(final BigDecimal value)
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
def flush():
'''public final void flush()
'''
pass
def close():
'''public void close()
'''
pass
