def FilteringGeneratorDelegate():
'''public FilteringGeneratorDelegate(final JsonGenerator d, final TokenFilter f, final boolean includePath, final boolean allowMultipleMatches)
'''
pass
def getFilter():
'''public TokenFilter getFilter()
'''
pass
def getFilterContext():
'''public JsonStreamContext getFilterContext()
'''
pass
def getMatchCount():
'''public int getMatchCount()
'''
pass
def getOutputContext():
'''public JsonStreamContext getOutputContext()
'''
pass
def writeStartArray():
'''public void writeStartArray()
public void writeStartArray(final int size)
'''
pass
def writeEndArray():
'''public void writeEndArray()
'''
pass
def writeStartObject():
'''public void writeStartObject()
public void writeStartObject(final Object forValue)
'''
pass
def writeEndObject():
'''public void writeEndObject()
'''
pass
def writeFieldName():
'''public void writeFieldName(final String name)
public void writeFieldName(final SerializableString name)
'''
pass
def writeString():
'''public void writeString(final String value)
public void writeString(final char[] text, final int offset, final int len)
public void writeString(final SerializableString value)
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
public void writeRaw(final SerializableString text)
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
def writeBinary():
'''public void writeBinary(final Base64Variant b64variant, final byte[] data, final int offset, final int len)
public int writeBinary(final Base64Variant b64variant, final InputStream data, final int dataLength)
'''
pass
def writeNumber():
'''public void writeNumber(final short v)
public void writeNumber(final int v)
public void writeNumber(final long v)
public void writeNumber(final BigInteger v)
public void writeNumber(final double v)
public void writeNumber(final float v)
public void writeNumber(final BigDecimal v)
public void writeNumber(final String encodedValue)
'''
pass
def writeBoolean():
'''public void writeBoolean(final boolean v)
'''
pass
def writeNull():
'''public void writeNull()
'''
pass
def writeOmittedField():
'''public void writeOmittedField(final String fieldName)
'''
pass
def writeObjectId():
'''public void writeObjectId(final Object id)
'''
pass
def writeObjectRef():
'''public void writeObjectRef(final Object id)
'''
pass
def writeTypeId():
'''public void writeTypeId(final Object id)
'''
pass