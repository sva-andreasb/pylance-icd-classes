def configure():
'''public final JsonGenerator configure(final Feature f, final boolean state)
'''
pass
def overrideStdFeatures():
'''public JsonGenerator overrideStdFeatures(final int values, final int mask)
'''
pass
def getFormatFeatures():
'''public int getFormatFeatures()
'''
pass
def overrideFormatFeatures():
'''public JsonGenerator overrideFormatFeatures(final int values, final int mask)
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
def setPrettyPrinter():
'''public JsonGenerator setPrettyPrinter(final PrettyPrinter pp)
'''
pass
def getPrettyPrinter():
'''public PrettyPrinter getPrettyPrinter()
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
def getOutputTarget():
'''public Object getOutputTarget()
'''
pass
def getOutputBuffered():
'''public int getOutputBuffered()
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
def canUseSchema():
'''public boolean canUseSchema(final FormatSchema schema)
'''
pass
def canWriteObjectId():
'''public boolean canWriteObjectId()
'''
pass
def canWriteTypeId():
'''public boolean canWriteTypeId()
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
def canWriteFormattedNumbers():
'''public boolean canWriteFormattedNumbers()
'''
pass
def writeStartArray():
'''public void writeStartArray(final int size)
'''
pass
def writeStartObject():
'''public void writeStartObject(final Object forValue)
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
'''public void writeString(final Reader reader, final int len)
'''
pass
def writeRaw():
'''public void writeRaw(final SerializableString raw)
'''
pass
def writeRawValue():
'''public void writeRawValue(final SerializableString raw)
'''
pass
def writeBinary():
'''public void writeBinary(final byte[] data, final int offset, final int len)
public void writeBinary(final byte[] data)
public int writeBinary(final InputStream data, final int dataLength)
'''
pass
def writeNumber():
'''public void writeNumber(final short v)
'''
pass
def writeEmbeddedObject():
'''public void writeEmbeddedObject(final Object object)
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
def writeTypePrefix():
'''public WritableTypeId writeTypePrefix(final WritableTypeId typeIdDef)
'''
pass
def writeTypeSuffix():
'''public WritableTypeId writeTypeSuffix(final WritableTypeId typeIdDef)
'''
pass
def writeStringField():
'''public void writeStringField(final String fieldName, final String value)
'''
pass
def writeBooleanField():
'''public final void writeBooleanField(final String fieldName, final boolean value)
'''
pass
def writeNullField():
'''public final void writeNullField(final String fieldName)
'''
pass
def writeNumberField():
'''public final void writeNumberField(final String fieldName, final int value)
public final void writeNumberField(final String fieldName, final long value)
public final void writeNumberField(final String fieldName, final double value)
public final void writeNumberField(final String fieldName, final float value)
public final void writeNumberField(final String fieldName, final BigDecimal value)
'''
pass
def writeBinaryField():
'''public final void writeBinaryField(final String fieldName, final byte[] data)
'''
pass
def writeArrayFieldStart():
'''public final void writeArrayFieldStart(final String fieldName)
'''
pass
def writeObjectFieldStart():
'''public final void writeObjectFieldStart(final String fieldName)
'''
pass
def writeObjectField():
'''public final void writeObjectField(final String fieldName, final Object pojo)
'''
pass
def writeOmittedField():
'''public void writeOmittedField(final String fieldName)
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
def collectDefaults():
'''public static int collectDefaults()
'''
pass
def enabledByDefault():
'''public boolean enabledByDefault()
'''
pass
def enabledIn():
'''public boolean enabledIn(final int flags)
'''
pass
def getMask():
'''public int getMask()
'''
pass
