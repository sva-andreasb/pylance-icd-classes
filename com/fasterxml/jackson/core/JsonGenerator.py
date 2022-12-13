def configure():
    '''    public final JsonGenerator configure(final Feature f, final boolean state)
    '''
def overrideStdFeatures():
    '''    public JsonGenerator overrideStdFeatures(final int values, final int mask)
    '''
def getFormatFeatures():
    '''    public int getFormatFeatures()
    '''
def overrideFormatFeatures():
    '''    public JsonGenerator overrideFormatFeatures(final int values, final int mask)
    '''
def setSchema():
    '''    public void setSchema(final FormatSchema schema)
    '''
def getSchema():
    '''    public FormatSchema getSchema()
    '''
def setPrettyPrinter():
    '''    public JsonGenerator setPrettyPrinter(final PrettyPrinter pp)
    '''
def getPrettyPrinter():
    '''    public PrettyPrinter getPrettyPrinter()
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
def getOutputTarget():
    '''    public Object getOutputTarget()
    '''
def getOutputBuffered():
    '''    public int getOutputBuffered()
    '''
def getCurrentValue():
    '''    public Object getCurrentValue()
    '''
def setCurrentValue():
    '''    public void setCurrentValue(final Object v)
    '''
def canUseSchema():
    '''    public boolean canUseSchema(final FormatSchema schema)
    '''
def canWriteObjectId():
    '''    public boolean canWriteObjectId()
    '''
def canWriteTypeId():
    '''    public boolean canWriteTypeId()
    '''
def canWriteBinaryNatively():
    '''    public boolean canWriteBinaryNatively()
    '''
def canOmitFields():
    '''    public boolean canOmitFields()
    '''
def canWriteFormattedNumbers():
    '''    public boolean canWriteFormattedNumbers()
    '''
def writeStartArray():
    '''    public void writeStartArray(final int size)
    '''
def writeStartObject():
    '''    public void writeStartObject(final Object forValue)
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
    '''    public void writeString(final Reader reader, final int len)
    '''
def writeRaw():
    '''    public void writeRaw(final SerializableString raw)
    '''
def writeRawValue():
    '''    public void writeRawValue(final SerializableString raw)
    '''
def writeBinary():
    '''    public void writeBinary(final byte[] data, final int offset, final int len)
    public void writeBinary(final byte[] data)
    public int writeBinary(final InputStream data, final int dataLength)
    '''
def writeNumber():
    '''    public void writeNumber(final short v)
    '''
def writeEmbeddedObject():
    '''    public void writeEmbeddedObject(final Object object)
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
def writeTypePrefix():
    '''    public WritableTypeId writeTypePrefix(final WritableTypeId typeIdDef)
    '''
def writeTypeSuffix():
    '''    public WritableTypeId writeTypeSuffix(final WritableTypeId typeIdDef)
    '''
def writeStringField():
    '''    public void writeStringField(final String fieldName, final String value)
    '''
def writeBooleanField():
    '''    public final void writeBooleanField(final String fieldName, final boolean value)
    '''
def writeNullField():
    '''    public final void writeNullField(final String fieldName)
    '''
def writeNumberField():
    '''    public final void writeNumberField(final String fieldName, final int value)
    public final void writeNumberField(final String fieldName, final long value)
    public final void writeNumberField(final String fieldName, final double value)
    public final void writeNumberField(final String fieldName, final float value)
    public final void writeNumberField(final String fieldName, final BigDecimal value)
    '''
def writeBinaryField():
    '''    public final void writeBinaryField(final String fieldName, final byte[] data)
    '''
def writeArrayFieldStart():
    '''    public final void writeArrayFieldStart(final String fieldName)
    '''
def writeObjectFieldStart():
    '''    public final void writeObjectFieldStart(final String fieldName)
    '''
def writeObjectField():
    '''    public final void writeObjectField(final String fieldName, final Object pojo)
    '''
def writeOmittedField():
    '''    public void writeOmittedField(final String fieldName)
    '''
def copyCurrentEvent():
    '''    public void copyCurrentEvent(final JsonParser p)
    '''
def copyCurrentStructure():
    '''    public void copyCurrentStructure(final JsonParser p)
    '''
def collectDefaults():
    '''    public static int collectDefaults()
    '''
def enabledByDefault():
    '''    public boolean enabledByDefault()
    '''
def enabledIn():
    '''    public boolean enabledIn(final int flags)
    '''
def getMask():
    '''    public int getMask()
    '''
