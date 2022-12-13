def JsonGeneratorDelegate():
    '''    public JsonGeneratorDelegate(final JsonGenerator d)
    public JsonGeneratorDelegate(final JsonGenerator d, final boolean delegateCopyMethods)
    '''
def getCurrentValue():
    '''    public Object getCurrentValue()
    '''
def setCurrentValue():
    '''    public void setCurrentValue(final Object v)
    '''
def getDelegate():
    '''    public JsonGenerator getDelegate()
    '''
def getCodec():
    '''    public ObjectCodec getCodec()
    '''
def setCodec():
    '''    public JsonGenerator setCodec(final ObjectCodec oc)
    '''
def setSchema():
    '''    public void setSchema(final FormatSchema schema)
    '''
def getSchema():
    '''    public FormatSchema getSchema()
    '''
def version():
    '''    public Version version()
    '''
def getOutputTarget():
    '''    public Object getOutputTarget()
    '''
def getOutputBuffered():
    '''    public int getOutputBuffered()
    '''
def canUseSchema():
    '''    public boolean canUseSchema(final FormatSchema schema)
    '''
def canWriteTypeId():
    '''    public boolean canWriteTypeId()
    '''
def canWriteObjectId():
    '''    public boolean canWriteObjectId()
    '''
def canWriteBinaryNatively():
    '''    public boolean canWriteBinaryNatively()
    '''
def canOmitFields():
    '''    public boolean canOmitFields()
    '''
def enable():
    '''    public JsonGenerator enable(final Feature f)
    '''
def disable():
    '''    public JsonGenerator disable(final Feature f)
    '''
def isEnabled():
    '''    public boolean isEnabled(final Feature f)
    '''
def getFeatureMask():
    '''    public int getFeatureMask()
    '''
def setFeatureMask():
    '''    public JsonGenerator setFeatureMask(final int mask)
    '''
def overrideStdFeatures():
    '''    public JsonGenerator overrideStdFeatures(final int values, final int mask)
    '''
def overrideFormatFeatures():
    '''    public JsonGenerator overrideFormatFeatures(final int values, final int mask)
    '''
def setPrettyPrinter():
    '''    public JsonGenerator setPrettyPrinter(final PrettyPrinter pp)
    '''
def getPrettyPrinter():
    '''    public PrettyPrinter getPrettyPrinter()
    '''
def useDefaultPrettyPrinter():
    '''    public JsonGenerator useDefaultPrettyPrinter()
    '''
def setHighestNonEscapedChar():
    '''    public JsonGenerator setHighestNonEscapedChar(final int charCode)
    '''
def getHighestEscapedChar():
    '''    public int getHighestEscapedChar()
    '''
def getCharacterEscapes():
    '''    public CharacterEscapes getCharacterEscapes()
    '''
def setCharacterEscapes():
    '''    public JsonGenerator setCharacterEscapes(final CharacterEscapes esc)
    '''
def setRootValueSeparator():
    '''    public JsonGenerator setRootValueSeparator(final SerializableString sep)
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
def writeFieldId():
    '''    public void writeFieldId(final long id)
    '''
def writeArray():
    '''    public void writeArray(final int[] array, final int offset, final int length)
    public void writeArray(final long[] array, final int offset, final int length)
    public void writeArray(final double[] array, final int offset, final int length)
    '''
def writeString():
    '''    public void writeString(final String text)
    public void writeString(final Reader reader, final int len)
    public void writeString(final char[] text, final int offset, final int len)
    public void writeString(final SerializableString text)
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
    public void writeRaw(final SerializableString raw)
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
    '''    public void writeBoolean(final boolean state)
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
def writeEmbeddedObject():
    '''    public void writeEmbeddedObject(final Object object)
    '''
def writeObject():
    '''    public void writeObject(final Object pojo)
    '''
def writeTree():
    '''    public void writeTree(final TreeNode tree)
    '''
def copyCurrentEvent():
    '''    public void copyCurrentEvent(final JsonParser p)
    '''
def copyCurrentStructure():
    '''    public void copyCurrentStructure(final JsonParser p)
    '''
def getOutputContext():
    '''    public JsonStreamContext getOutputContext()
    '''
def flush():
    '''    public void flush()
    '''
def close():
    '''    public void close()
    '''
def isClosed():
    '''    public boolean isClosed()
    '''
