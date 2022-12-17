def ():
    '''returns UTF8JsonGenerator\n\n
    (final IOContext ctxt, final int features, final ObjectCodec codec, final OutputStream out)\n
    (final IOContext ctxt, final int features, final ObjectCodec codec, final OutputStream out, final byte[] outputBuffer, final int outputOffset, final boolean bufferRecyclable)\n
    '''
def getOutputTarget():
    '''returns Object\n\n
    getOutputTarget()\n
    '''
def getOutputBuffered():
    '''returns int\n\n
    getOutputBuffered()\n
    '''
def writeFieldName():
    '''returns None\n\n
    writeFieldName(final String name)\n
    writeFieldName(final SerializableString name)\n
    '''
def writeStartObject():
    '''returns None\n\n
    writeStartObject(final Object forValue)\n
    '''
def writeString():
    '''returns None\n\n
    writeString(final String text)\n
    writeString(final Reader reader, final int len)\n
    writeString(final char[] text, final int offset, final int len)\n
    '''
def writeRawUTF8String():
    '''returns None\n\n
    writeRawUTF8String(final byte[] text, final int offset, final int length)\n
    '''
def writeUTF8String():
    '''returns None\n\n
    writeUTF8String(final byte[] text, final int offset, final int len)\n
    '''
def writeRaw():
    '''returns None\n\n
    writeRaw(final String text)\n
    writeRaw(final String text, int offset, int len)\n
    writeRaw(final SerializableString text)\n
    writeRaw(final char ch)\n
    '''
def writeRawValue():
    '''returns None\n\n
    writeRawValue(final SerializableString text)\n
    '''
def writeBinary():
    '''returns int\n\n
    writeBinary(final Base64Variant b64variant, final byte[] data, final int offset, final int len)\n
    writeBinary(final Base64Variant b64variant, final InputStream data, final int dataLength)\n
    '''
def writeNumber():
    '''returns None\n\n
    writeNumber(final short s)\n
    writeNumber(final int i)\n
    writeNumber(final long l)\n
    writeNumber(final BigInteger value)\n
    writeNumber(final double d)\n
    writeNumber(final float f)\n
    writeNumber(final BigDecimal value)\n
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
def flush():
    '''returns None\n\n
    flush()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
