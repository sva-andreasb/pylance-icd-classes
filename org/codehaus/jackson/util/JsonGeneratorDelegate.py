def ():
    '''returns JsonGeneratorDelegate\n\n
    (final JsonGenerator d)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def copyCurrentEvent():
    '''returns None\n\n
    copyCurrentEvent(final JsonParser jp)\n
    '''
def copyCurrentStructure():
    '''returns None\n\n
    copyCurrentStructure(final JsonParser jp)\n
    '''
def disable():
    '''returns JsonGenerator\n\n
    disable(final Feature f)\n
    '''
def enable():
    '''returns JsonGenerator\n\n
    enable(final Feature f)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def getCodec():
    '''returns ObjectCodec\n\n
    getCodec()\n
    '''
def getOutputContext():
    '''returns JsonStreamContext\n\n
    getOutputContext()\n
    '''
def setSchema():
    '''returns None\n\n
    setSchema(final FormatSchema schema)\n
    '''
def canUseSchema():
    '''returns boolean\n\n
    canUseSchema(final FormatSchema schema)\n
    '''
def version():
    '''returns Version\n\n
    version()\n
    '''
def getOutputTarget():
    '''returns Object\n\n
    getOutputTarget()\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled(final Feature f)\n
    '''
def setCodec():
    '''returns JsonGenerator\n\n
    setCodec(final ObjectCodec oc)\n
    '''
def useDefaultPrettyPrinter():
    '''returns JsonGenerator\n\n
    useDefaultPrettyPrinter()\n
    '''
def writeBinary():
    '''returns None\n\n
    writeBinary(final Base64Variant b64variant, final byte[] data, final int offset, final int len)\n
    '''
def writeBoolean():
    '''returns None\n\n
    writeBoolean(final boolean state)\n
    '''
def writeEndArray():
    '''returns None\n\n
    writeEndArray()\n
    '''
def writeEndObject():
    '''returns None\n\n
    writeEndObject()\n
    '''
def writeFieldName():
    '''returns None\n\n
    writeFieldName(final String name)\n
    writeFieldName(final SerializedString name)\n
    writeFieldName(final SerializableString name)\n
    '''
def writeNull():
    '''returns None\n\n
    writeNull()\n
    '''
def writeNumber():
    '''returns None\n\n
    writeNumber(final int v)\n
    writeNumber(final long v)\n
    writeNumber(final BigInteger v)\n
    writeNumber(final double v)\n
    writeNumber(final float v)\n
    writeNumber(final BigDecimal v)\n
    writeNumber(final String encodedValue)\n
    '''
def writeObject():
    '''returns None\n\n
    writeObject(final Object pojo)\n
    '''
def writeRaw():
    '''returns None\n\n
    writeRaw(final String text)\n
    writeRaw(final String text, final int offset, final int len)\n
    writeRaw(final char[] text, final int offset, final int len)\n
    writeRaw(final char c)\n
    '''
def writeRawValue():
    '''returns None\n\n
    writeRawValue(final String text)\n
    writeRawValue(final String text, final int offset, final int len)\n
    writeRawValue(final char[] text, final int offset, final int len)\n
    '''
def writeStartArray():
    '''returns None\n\n
    writeStartArray()\n
    '''
def writeStartObject():
    '''returns None\n\n
    writeStartObject()\n
    '''
def writeString():
    '''returns None\n\n
    writeString(final String text)\n
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
def writeTree():
    '''returns None\n\n
    writeTree(final JsonNode rootNode)\n
    '''
