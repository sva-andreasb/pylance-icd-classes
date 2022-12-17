def ():
    '''returns JsonGeneratorDelegate\n\n
    (final JsonGenerator d)\n
    (final JsonGenerator d, final boolean delegateCopyMethods)\n
    '''
def getCurrentValue():
    '''returns Object\n\n
    getCurrentValue()\n
    '''
def setCurrentValue():
    '''returns None\n\n
    setCurrentValue(final Object v)\n
    '''
def getDelegate():
    '''returns JsonGenerator\n\n
    getDelegate()\n
    '''
def getCodec():
    '''returns ObjectCodec\n\n
    getCodec()\n
    '''
def setCodec():
    '''returns JsonGenerator\n\n
    setCodec(final ObjectCodec oc)\n
    '''
def setSchema():
    '''returns None\n\n
    setSchema(final FormatSchema schema)\n
    '''
def getSchema():
    '''returns FormatSchema\n\n
    getSchema()\n
    '''
def version():
    '''returns Version\n\n
    version()\n
    '''
def getOutputTarget():
    '''returns Object\n\n
    getOutputTarget()\n
    '''
def getOutputBuffered():
    '''returns int\n\n
    getOutputBuffered()\n
    '''
def canUseSchema():
    '''returns boolean\n\n
    canUseSchema(final FormatSchema schema)\n
    '''
def canWriteTypeId():
    '''returns boolean\n\n
    canWriteTypeId()\n
    '''
def canWriteObjectId():
    '''returns boolean\n\n
    canWriteObjectId()\n
    '''
def canWriteBinaryNatively():
    '''returns boolean\n\n
    canWriteBinaryNatively()\n
    '''
def canOmitFields():
    '''returns boolean\n\n
    canOmitFields()\n
    '''
def enable():
    '''returns JsonGenerator\n\n
    enable(final Feature f)\n
    '''
def disable():
    '''returns JsonGenerator\n\n
    disable(final Feature f)\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled(final Feature f)\n
    '''
def getFeatureMask():
    '''returns int\n\n
    getFeatureMask()\n
    '''
def setFeatureMask():
    '''returns JsonGenerator\n\n
    setFeatureMask(final int mask)\n
    '''
def overrideStdFeatures():
    '''returns JsonGenerator\n\n
    overrideStdFeatures(final int values, final int mask)\n
    '''
def overrideFormatFeatures():
    '''returns JsonGenerator\n\n
    overrideFormatFeatures(final int values, final int mask)\n
    '''
def setPrettyPrinter():
    '''returns JsonGenerator\n\n
    setPrettyPrinter(final PrettyPrinter pp)\n
    '''
def getPrettyPrinter():
    '''returns PrettyPrinter\n\n
    getPrettyPrinter()\n
    '''
def useDefaultPrettyPrinter():
    '''returns JsonGenerator\n\n
    useDefaultPrettyPrinter()\n
    '''
def setHighestNonEscapedChar():
    '''returns JsonGenerator\n\n
    setHighestNonEscapedChar(final int charCode)\n
    '''
def getHighestEscapedChar():
    '''returns int\n\n
    getHighestEscapedChar()\n
    '''
def getCharacterEscapes():
    '''returns CharacterEscapes\n\n
    getCharacterEscapes()\n
    '''
def setCharacterEscapes():
    '''returns JsonGenerator\n\n
    setCharacterEscapes(final CharacterEscapes esc)\n
    '''
def setRootValueSeparator():
    '''returns JsonGenerator\n\n
    setRootValueSeparator(final SerializableString sep)\n
    '''
def writeStartArray():
    '''returns None\n\n
    writeStartArray()\n
    writeStartArray(final int size)\n
    '''
def writeEndArray():
    '''returns None\n\n
    writeEndArray()\n
    '''
def writeStartObject():
    '''returns None\n\n
    writeStartObject()\n
    writeStartObject(final Object forValue)\n
    '''
def writeEndObject():
    '''returns None\n\n
    writeEndObject()\n
    '''
def writeFieldName():
    '''returns None\n\n
    writeFieldName(final String name)\n
    writeFieldName(final SerializableString name)\n
    '''
def writeFieldId():
    '''returns None\n\n
    writeFieldId(final long id)\n
    '''
def writeArray():
    '''returns None\n\n
    writeArray(final int[] array, final int offset, final int length)\n
    writeArray(final long[] array, final int offset, final int length)\n
    writeArray(final double[] array, final int offset, final int length)\n
    '''
def writeString():
    '''returns None\n\n
    writeString(final String text)\n
    writeString(final Reader reader, final int len)\n
    writeString(final char[] text, final int offset, final int len)\n
    writeString(final SerializableString text)\n
    '''
def writeRawUTF8String():
    '''returns None\n\n
    writeRawUTF8String(final byte[] text, final int offset, final int length)\n
    '''
def writeUTF8String():
    '''returns None\n\n
    writeUTF8String(final byte[] text, final int offset, final int length)\n
    '''
def writeRaw():
    '''returns None\n\n
    writeRaw(final String text)\n
    writeRaw(final String text, final int offset, final int len)\n
    writeRaw(final SerializableString raw)\n
    writeRaw(final char[] text, final int offset, final int len)\n
    writeRaw(final char c)\n
    '''
def writeRawValue():
    '''returns None\n\n
    writeRawValue(final String text)\n
    writeRawValue(final String text, final int offset, final int len)\n
    writeRawValue(final char[] text, final int offset, final int len)\n
    '''
def writeBinary():
    '''returns int\n\n
    writeBinary(final Base64Variant b64variant, final byte[] data, final int offset, final int len)\n
    writeBinary(final Base64Variant b64variant, final InputStream data, final int dataLength)\n
    '''
def writeNumber():
    '''returns None\n\n
    writeNumber(final short v)\n
    writeNumber(final int v)\n
    writeNumber(final long v)\n
    writeNumber(final BigInteger v)\n
    writeNumber(final double v)\n
    writeNumber(final float v)\n
    writeNumber(final BigDecimal v)\n
    writeNumber(final String encodedValue)\n
    '''
def writeBoolean():
    '''returns None\n\n
    writeBoolean(final boolean state)\n
    '''
def writeNull():
    '''returns None\n\n
    writeNull()\n
    '''
def writeOmittedField():
    '''returns None\n\n
    writeOmittedField(final String fieldName)\n
    '''
def writeObjectId():
    '''returns None\n\n
    writeObjectId(final Object id)\n
    '''
def writeObjectRef():
    '''returns None\n\n
    writeObjectRef(final Object id)\n
    '''
def writeTypeId():
    '''returns None\n\n
    writeTypeId(final Object id)\n
    '''
def writeEmbeddedObject():
    '''returns None\n\n
    writeEmbeddedObject(final Object object)\n
    '''
def writeObject():
    '''returns None\n\n
    writeObject(final Object pojo)\n
    '''
def writeTree():
    '''returns None\n\n
    writeTree(final TreeNode tree)\n
    '''
def copyCurrentEvent():
    '''returns None\n\n
    copyCurrentEvent(final JsonParser p)\n
    '''
def copyCurrentStructure():
    '''returns None\n\n
    copyCurrentStructure(final JsonParser p)\n
    '''
def getOutputContext():
    '''returns JsonStreamContext\n\n
    getOutputContext()\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
