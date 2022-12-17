def overrideStdFeatures():
    '''returns JsonGenerator\n\n
    overrideStdFeatures(final int values, final int mask)\n
    '''
def getFormatFeatures():
    '''returns int\n\n
    getFormatFeatures()\n
    '''
def overrideFormatFeatures():
    '''returns JsonGenerator\n\n
    overrideFormatFeatures(final int values, final int mask)\n
    '''
def setSchema():
    '''returns None\n\n
    setSchema(final FormatSchema schema)\n
    '''
def getSchema():
    '''returns FormatSchema\n\n
    getSchema()\n
    '''
def setPrettyPrinter():
    '''returns JsonGenerator\n\n
    setPrettyPrinter(final PrettyPrinter pp)\n
    '''
def getPrettyPrinter():
    '''returns PrettyPrinter\n\n
    getPrettyPrinter()\n
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
def getOutputTarget():
    '''returns Object\n\n
    getOutputTarget()\n
    '''
def getOutputBuffered():
    '''returns int\n\n
    getOutputBuffered()\n
    '''
def getCurrentValue():
    '''returns Object\n\n
    getCurrentValue()\n
    '''
def setCurrentValue():
    '''returns None\n\n
    setCurrentValue(final Object v)\n
    '''
def canUseSchema():
    '''returns boolean\n\n
    canUseSchema(final FormatSchema schema)\n
    '''
def canWriteObjectId():
    '''returns boolean\n\n
    canWriteObjectId()\n
    '''
def canWriteTypeId():
    '''returns boolean\n\n
    canWriteTypeId()\n
    '''
def canWriteBinaryNatively():
    '''returns boolean\n\n
    canWriteBinaryNatively()\n
    '''
def canOmitFields():
    '''returns boolean\n\n
    canOmitFields()\n
    '''
def canWriteFormattedNumbers():
    '''returns boolean\n\n
    canWriteFormattedNumbers()\n
    '''
def writeStartArray():
    '''returns None\n\n
    writeStartArray(final int size)\n
    '''
def writeStartObject():
    '''returns None\n\n
    writeStartObject(final Object forValue)\n
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
    writeString(final Reader reader, final int len)\n
    '''
def writeRaw():
    '''returns None\n\n
    writeRaw(final SerializableString raw)\n
    '''
def writeRawValue():
    '''returns None\n\n
    writeRawValue(final SerializableString raw)\n
    '''
def writeBinary():
    '''returns int\n\n
    writeBinary(final byte[] data, final int offset, final int len)\n
    writeBinary(final byte[] data)\n
    writeBinary(final InputStream data, final int dataLength)\n
    '''
def writeNumber():
    '''returns None\n\n
    writeNumber(final short v)\n
    '''
def writeEmbeddedObject():
    '''returns None\n\n
    writeEmbeddedObject(final Object object)\n
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
def writeTypePrefix():
    '''returns WritableTypeId\n\n
    writeTypePrefix(final WritableTypeId typeIdDef)\n
    '''
def writeTypeSuffix():
    '''returns WritableTypeId\n\n
    writeTypeSuffix(final WritableTypeId typeIdDef)\n
    '''
def writeStringField():
    '''returns None\n\n
    writeStringField(final String fieldName, final String value)\n
    '''
def writeOmittedField():
    '''returns None\n\n
    writeOmittedField(final String fieldName)\n
    '''
def copyCurrentEvent():
    '''returns None\n\n
    copyCurrentEvent(final JsonParser p)\n
    '''
def copyCurrentStructure():
    '''returns None\n\n
    copyCurrentStructure(final JsonParser p)\n
    '''
def enabledByDefault():
    '''returns boolean\n\n
    enabledByDefault()\n
    '''
def enabledIn():
    '''returns boolean\n\n
    enabledIn(final int flags)\n
    '''
def getMask():
    '''returns int\n\n
    getMask()\n
    '''
