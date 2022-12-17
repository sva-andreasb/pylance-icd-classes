def ():
    '''returns FilteringGeneratorDelegate\n\n
    (final JsonGenerator d, final TokenFilter f, final boolean includePath, final boolean allowMultipleMatches)\n
    '''
def getFilter():
    '''returns TokenFilter\n\n
    getFilter()\n
    '''
def getFilterContext():
    '''returns JsonStreamContext\n\n
    getFilterContext()\n
    '''
def getMatchCount():
    '''returns int\n\n
    getMatchCount()\n
    '''
def getOutputContext():
    '''returns JsonStreamContext\n\n
    getOutputContext()\n
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
def writeString():
    '''returns None\n\n
    writeString(final String value)\n
    writeString(final char[] text, final int offset, final int len)\n
    writeString(final SerializableString value)\n
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
    writeRaw(final SerializableString text)\n
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
    writeBoolean(final boolean v)\n
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
