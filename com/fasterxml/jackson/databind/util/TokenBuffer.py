TOKENS_PER_SEGMENT = "int  16"
def ():
    '''returns Segment\n\n
    (final ObjectCodec codec, final boolean hasNativeIds)\n
    (final JsonParser p)\n
    (final JsonParser p, final DeserializationContext ctxt)\n
    (final Segment firstSeg, final ObjectCodec codec, final boolean hasNativeTypeIds, final boolean hasNativeObjectIds)\n
    (final Segment firstSeg, final ObjectCodec codec, final boolean hasNativeTypeIds, final boolean hasNativeObjectIds, final JsonStreamContext parentContext)\n
    ()\n
    '''
def overrideParentContext():
    '''returns TokenBuffer\n\n
    overrideParentContext(final JsonStreamContext ctxt)\n
    '''
def forceUseOfBigDecimal():
    '''returns TokenBuffer\n\n
    forceUseOfBigDecimal(final boolean b)\n
    '''
def version():
    '''returns Version\n\n
    version()\n
    version()\n
    '''
def asParser():
    '''returns JsonParser\n\n
    asParser()\n
    asParser(final ObjectCodec codec)\n
    asParser(final JsonParser src)\n
    '''
def asParserOnFirstToken():
    '''returns JsonParser\n\n
    asParserOnFirstToken()\n
    '''
def firstToken():
    '''returns JsonToken\n\n
    firstToken()\n
    '''
def append():
    '''returns Segment\n\n
    append(final TokenBuffer other)\n
    append(final int index, final JsonToken tokenType)\n
    append(final int index, final JsonToken tokenType, final Object objectId, final Object typeId)\n
    append(final int index, final JsonToken tokenType, final Object value)\n
    append(final int index, final JsonToken tokenType, final Object value, final Object objectId, final Object typeId)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final JsonGenerator gen)\n
    '''
def deserialize():
    '''returns TokenBuffer\n\n
    deserialize(final JsonParser p, final DeserializationContext ctxt)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def enable():
    '''returns JsonGenerator\n\n
    enable(final JsonGenerator.Feature f)\n
    '''
def disable():
    '''returns JsonGenerator\n\n
    disable(final JsonGenerator.Feature f)\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled(final JsonGenerator.Feature f)\n
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
def canWriteBinaryNatively():
    '''returns boolean\n\n
    canWriteBinaryNatively()\n
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
def writeStartObject():
    '''returns None\n\n
    writeStartObject(final Object forValue)\n
    '''
def writeFieldName():
    '''returns None\n\n
    writeFieldName(final SerializableString name)\n
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
    writeRaw(final SerializableString text)\n
    writeRaw(final char[] text, final int offset, final int len)\n
    writeRaw(final char c)\n
    '''
def writeRawValue():
    '''returns None\n\n
    writeRawValue(final String text)\n
    writeRawValue(String text, final int offset, final int len)\n
    writeRawValue(final char[] text, final int offset, final int len)\n
    '''
def writeNumber():
    '''returns None\n\n
    writeNumber(final short i)\n
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
    writeTree(final TreeNode node)\n
    '''
def writeBinary():
    '''returns int\n\n
    writeBinary(final Base64Variant b64variant, final byte[] data, final int offset, final int len)\n
    writeBinary(final Base64Variant b64variant, final InputStream data, final int dataLength)\n
    '''
def canWriteTypeId():
    '''returns boolean\n\n
    canWriteTypeId()\n
    '''
def canWriteObjectId():
    '''returns boolean\n\n
    canWriteObjectId()\n
    '''
def writeTypeId():
    '''returns None\n\n
    writeTypeId(final Object id)\n
    '''
def writeObjectId():
    '''returns None\n\n
    writeObjectId(final Object id)\n
    '''
def writeEmbeddedObject():
    '''returns None\n\n
    writeEmbeddedObject(final Object object)\n
    '''
def copyCurrentEvent():
    '''returns None\n\n
    copyCurrentEvent(final JsonParser p)\n
    '''
def copyCurrentStructure():
    '''returns None\n\n
    copyCurrentStructure(final JsonParser p)\n
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
def nextFieldName():
    '''returns String\n\n
    nextFieldName()\n
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
def overrideCurrentName():
    '''returns None\n\n
    overrideCurrentName(final String name)\n
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
def isNaN():
    '''returns boolean\n\n
    isNaN()\n
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
def getEmbeddedObject():
    '''returns Object\n\n
    getEmbeddedObject()\n
    '''
def getBinaryValue():
    '''returns byte[]\n\n
    getBinaryValue(final Base64Variant b64variant)\n
    '''
def readBinaryValue():
    '''returns int\n\n
    readBinaryValue(final Base64Variant b64variant, final OutputStream out)\n
    '''
def canReadObjectId():
    '''returns boolean\n\n
    canReadObjectId()\n
    '''
def canReadTypeId():
    '''returns boolean\n\n
    canReadTypeId()\n
    '''
def getTypeId():
    '''returns Object\n\n
    getTypeId()\n
    '''
def getObjectId():
    '''returns Object\n\n
    getObjectId()\n
    '''
def type():
    '''returns JsonToken\n\n
    type(final int index)\n
    '''
def rawType():
    '''returns int\n\n
    rawType(final int index)\n
    '''
def get():
    '''returns Object\n\n
    get(final int index)\n
    '''
def next():
    '''returns Segment\n\n
    next()\n
    '''
def hasIds():
    '''returns boolean\n\n
    hasIds()\n
    '''
