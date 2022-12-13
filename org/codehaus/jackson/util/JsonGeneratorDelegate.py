def JsonGeneratorDelegate():
'''public JsonGeneratorDelegate(final JsonGenerator d)
'''
pass
def close():
'''public void close()
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
def disable():
'''public JsonGenerator disable(final Feature f)
'''
pass
def enable():
'''public JsonGenerator enable(final Feature f)
'''
pass
def flush():
'''public void flush()
'''
pass
def getCodec():
'''public ObjectCodec getCodec()
'''
pass
def getOutputContext():
'''public JsonStreamContext getOutputContext()
'''
pass
def setSchema():
'''public void setSchema(final FormatSchema schema)
'''
pass
def canUseSchema():
'''public boolean canUseSchema(final FormatSchema schema)
'''
pass
def version():
'''public Version version()
'''
pass
def getOutputTarget():
'''public Object getOutputTarget()
'''
pass
def isClosed():
'''public boolean isClosed()
'''
pass
def isEnabled():
'''public boolean isEnabled(final Feature f)
'''
pass
def setCodec():
'''public JsonGenerator setCodec(final ObjectCodec oc)
'''
pass
def useDefaultPrettyPrinter():
'''public JsonGenerator useDefaultPrettyPrinter()
'''
pass
def writeBinary():
'''public void writeBinary(final Base64Variant b64variant, final byte[] data, final int offset, final int len)
'''
pass
def writeBoolean():
'''public void writeBoolean(final boolean state)
'''
pass
def writeEndArray():
'''public void writeEndArray()
'''
pass
def writeEndObject():
'''public void writeEndObject()
'''
pass
def writeFieldName():
'''public void writeFieldName(final String name)
public void writeFieldName(final SerializedString name)
public void writeFieldName(final SerializableString name)
'''
pass
def writeNull():
'''public void writeNull()
'''
pass
def writeNumber():
'''public void writeNumber(final int v)
public void writeNumber(final long v)
public void writeNumber(final BigInteger v)
public void writeNumber(final double v)
public void writeNumber(final float v)
public void writeNumber(final BigDecimal v)
public void writeNumber(final String encodedValue)
'''
pass
def writeObject():
'''public void writeObject(final Object pojo)
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
def writeStartArray():
'''public void writeStartArray()
'''
pass
def writeStartObject():
'''public void writeStartObject()
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
def writeTree():
'''public void writeTree(final JsonNode rootNode)
'''
pass
