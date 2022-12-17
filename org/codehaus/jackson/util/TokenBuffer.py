TOKENS_PER_SEGMENT = "int  16"
def ():
    '''returns Segment\n\n
    (final ObjectCodec codec)\n
    (final Segment firstSeg, final ObjectCodec codec)\n
    ()\n
    '''
def asParser():
    '''returns JsonParser\n\n
    asParser()\n
    asParser(final ObjectCodec codec)\n
    asParser(final JsonParser src)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final JsonGenerator jgen)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
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
def useDefaultPrettyPrinter():
    '''returns JsonGenerator\n\n
    useDefaultPrettyPrinter()\n
    '''
def setCodec():
    '''returns None\n\n
    setCodec(final ObjectCodec oc)\n
    setCodec(final ObjectCodec c)\n
    '''
def getCodec():
    '''returns ObjectCodec\n\n
    getCodec()\n
    getCodec()\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    close()\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    isClosed()\n
    '''
def writeFieldName():
    '''returns None\n\n
    writeFieldName(final SerializableString name)\n
    writeFieldName(final SerializedString name)\n
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
def writeNumber():
    '''returns None\n\n
    writeNumber(final int i)\n
    writeNumber(final long l)\n
    writeNumber(final double d)\n
    writeNumber(final float f)\n
    writeNumber(final BigDecimal dec)\n
    writeNumber(final BigInteger v)\n
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
def writeObject():
    '''returns None\n\n
    writeObject(final Object value)\n
    '''
def writeTree():
    '''returns None\n\n
    writeTree(final JsonNode rootNode)\n
    '''
def writeBinary():
    '''returns None\n\n
    writeBinary(final Base64Variant b64variant, final byte[] data, final int offset, final int len)\n
    '''
def copyCurrentEvent():
    '''returns None\n\n
    copyCurrentEvent(final JsonParser jp)\n
    '''
def copyCurrentStructure():
    '''returns None\n\n
    copyCurrentStructure(final JsonParser jp)\n
    '''
def setLocation():
    '''returns None\n\n
    setLocation(final JsonLocation l)\n
    '''
def peekNextToken():
    '''returns JsonToken\n\n
    peekNextToken()\n
    '''
def nextToken():
    '''returns JsonToken\n\n
    nextToken()\n
    '''
def getParsingContext():
    '''returns JsonStreamContext\n\n
    getParsingContext()\n
    '''
def getTokenLocation():
    '''returns JsonLocation\n\n
    getTokenLocation()\n
    '''
def getCurrentLocation():
    '''returns JsonLocation\n\n
    getCurrentLocation()\n
    '''
def getCurrentName():
    '''returns String\n\n
    getCurrentName()\n
    '''
def getText():
    '''returns String\n\n
    getText()\n
    '''
def getTextCharacters():
    '''returns char[]\n\n
    getTextCharacters()\n
    '''
def getTextLength():
    '''returns int\n\n
    getTextLength()\n
    '''
def getTextOffset():
    '''returns int\n\n
    getTextOffset()\n
    '''
def hasTextCharacters():
    '''returns boolean\n\n
    hasTextCharacters()\n
    '''
def getBigIntegerValue():
    '''returns BigInteger\n\n
    getBigIntegerValue()\n
    '''
def getDecimalValue():
    '''returns BigDecimal\n\n
    getDecimalValue()\n
    '''
def getDoubleValue():
    '''returns double\n\n
    getDoubleValue()\n
    '''
def getFloatValue():
    '''returns float\n\n
    getFloatValue()\n
    '''
def getIntValue():
    '''returns int\n\n
    getIntValue()\n
    '''
def getLongValue():
    '''returns long\n\n
    getLongValue()\n
    '''
def getNumberType():
    '''returns NumberType\n\n
    getNumberType()\n
    '''
def getEmbeddedObject():
    '''returns Object\n\n
    getEmbeddedObject()\n
    '''
def getBinaryValue():
    '''returns byte[]\n\n
    getBinaryValue(final Base64Variant b64variant)\n
    '''
def type():
    '''returns JsonToken\n\n
    type(final int index)\n
    '''
def get():
    '''returns Object\n\n
    get(final int index)\n
    '''
def next():
    '''returns Segment\n\n
    next()\n
    '''
def append():
    '''returns Segment\n\n
    append(final int index, final JsonToken tokenType)\n
    append(final int index, final JsonToken tokenType, final Object value)\n
    '''
def set():
    '''returns None\n\n
    set(final int index, final JsonToken tokenType)\n
    set(final int index, final JsonToken tokenType, final Object value)\n
    '''
