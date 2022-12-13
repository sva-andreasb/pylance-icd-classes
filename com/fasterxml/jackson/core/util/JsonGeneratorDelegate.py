def JsonGeneratorDelegate():
'''public JsonGeneratorDelegate(final JsonGenerator d)
public JsonGeneratorDelegate(final JsonGenerator d, final boolean delegateCopyMethods)
'''
pass
def getCurrentValue():
'''public Object getCurrentValue()
'''
pass
def setCurrentValue():
'''public void setCurrentValue(final Object v)
'''
pass
def getDelegate():
'''public JsonGenerator getDelegate()
'''
pass
def getCodec():
'''public ObjectCodec getCodec()
'''
pass
def setCodec():
'''public JsonGenerator setCodec(final ObjectCodec oc)
'''
pass
def setSchema():
'''public void setSchema(final FormatSchema schema)
'''
pass
def getSchema():
'''public FormatSchema getSchema()
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
def getOutputBuffered():
'''public int getOutputBuffered()
'''
pass
def canUseSchema():
'''public boolean canUseSchema(final FormatSchema schema)
'''
pass
def canWriteTypeId():
'''public boolean canWriteTypeId()
'''
pass
def canWriteObjectId():
'''public boolean canWriteObjectId()
'''
pass
def canWriteBinaryNatively():
'''public boolean canWriteBinaryNatively()
'''
pass
def canOmitFields():
'''public boolean canOmitFields()
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
def getFeatureMask():
'''public int getFeatureMask()
'''
pass
def setFeatureMask():
'''public JsonGenerator setFeatureMask(final int mask)
'''
pass
def overrideStdFeatures():
'''public JsonGenerator overrideStdFeatures(final int values, final int mask)
'''
pass
def overrideFormatFeatures():
'''public JsonGenerator overrideFormatFeatures(final int values, final int mask)
'''
pass
def setPrettyPrinter():
'''public JsonGenerator setPrettyPrinter(final PrettyPrinter pp)
'''
pass
def getPrettyPrinter():
'''public PrettyPrinter getPrettyPrinter()
'''
pass
def useDefaultPrettyPrinter():
'''public JsonGenerator useDefaultPrettyPrinter()
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
def getCharacterEscapes():
'''public CharacterEscapes getCharacterEscapes()
'''
pass
def setCharacterEscapes():
'''public JsonGenerator setCharacterEscapes(final CharacterEscapes esc)
'''
pass
def setRootValueSeparator():
'''public JsonGenerator setRootValueSeparator(final SerializableString sep)
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
def writeFieldId():
'''public void writeFieldId(final long id)
'''
pass
def writeArray():
'''public void writeArray(final int[] array, final int offset, final int length)
public void writeArray(final long[] array, final int offset, final int length)
public void writeArray(final double[] array, final int offset, final int length)
'''
pass
def writeString():
'''public void writeString(final String text)
public void writeString(final Reader reader, final int len)
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
public void writeRaw(final SerializableString raw)
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
'''public void writeBoolean(final boolean state)
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
def writeEmbeddedObject():
'''public void writeEmbeddedObject(final Object object)
'''
pass
def writeObject():
'''public void writeObject(final Object pojo)
'''
pass
def writeTree():
'''public void writeTree(final TreeNode tree)
'''
pass
def copyCurrentEvent():
'''public void copyCurrentEvent(final JsonParser p)
'''
pass
def copyCurrentStructure():
'''public void copyCurrentStructure(final JsonParser p)
'''
pass
def getOutputContext():
'''public JsonStreamContext getOutputContext()
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
def isClosed():
'''public boolean isClosed()
'''
pass
