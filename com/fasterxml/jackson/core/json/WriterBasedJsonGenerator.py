def WriterBasedJsonGenerator():
'''public WriterBasedJsonGenerator(final IOContext ctxt, final int features, final ObjectCodec codec, final Writer w)
'''
pass
def getOutputTarget():
'''public Object getOutputTarget()
'''
pass
def getOutputBuffered():
'''public int getOutputBuffered()
'''
pass
def canWriteFormattedNumbers():
'''public boolean canWriteFormattedNumbers()
'''
pass
def writeFieldName():
'''public void writeFieldName(final String name)
public void writeFieldName(final SerializableString name)
'''
pass
def writeStartArray():
'''public void writeStartArray()
'''
pass
def writeEndArray():
'''public void writeEndArray()
'''
pass
def writeStartObject():
'''public void writeStartObject(final Object forValue)
public void writeStartObject()
'''
pass
def writeEndObject():
'''public void writeEndObject()
'''
pass
def writeString():
'''public void writeString(final String text)
public void writeString(final Reader reader, final int len)
public void writeString(final char[] text, final int offset, final int len)
public void writeString(final SerializableString sstr)
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
public void writeRaw(final String text, final int start, final int len)
public void writeRaw(final SerializableString text)
public void writeRaw(final char[] text, final int offset, final int len)
public void writeRaw(final char c)
'''
pass
def writeBinary():
'''public void writeBinary(final Base64Variant b64variant, final byte[] data, final int offset, final int len)
public int writeBinary(final Base64Variant b64variant, final InputStream data, final int dataLength)
'''
pass
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
'''public void flush()
'''
pass
def close():
'''public void close()
'''
pass
