def ():
    '''returns WriterBasedGenerator\n\n
    (final IOContext ctxt, final int features, final ObjectCodec codec, final Writer w)\n
    '''
def setHighestNonEscapedChar():
    '''returns JsonGenerator\n\n
    setHighestNonEscapedChar(final int charCode)\n
    '''
def getHighestEscapedChar():
    '''returns int\n\n
    getHighestEscapedChar()\n
    '''
def setCharacterEscapes():
    '''returns JsonGenerator\n\n
    setCharacterEscapes(final CharacterEscapes esc)\n
    '''
def getCharacterEscapes():
    '''returns CharacterEscapes\n\n
    getCharacterEscapes()\n
    '''
def getOutputTarget():
    '''returns Object\n\n
    getOutputTarget()\n
    '''
def _writeFieldName():
    '''returns None\n\n
    _writeFieldName(final SerializableString name, final boolean commaBefore)\n
    '''
def writeString():
    '''returns None\n\n
    writeString(final String text)\n
    writeString(final char[] text, final int offset, final int len)\n
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
    writeRaw(final String text, final int start, final int len)\n
    writeRaw(final char[] text, final int offset, final int len)\n
    writeRaw(final char c)\n
    '''
def writeBinary():
    '''returns None\n\n
    writeBinary(final Base64Variant b64variant, final byte[] data, final int offset, final int len)\n
    '''
def writeNumber():
    '''returns None\n\n
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
def close():
    '''returns None\n\n
    close()\n
    '''
