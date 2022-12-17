def ():
    '''returns Field\n\n
    (final String name, final Reader reader, final IndexableFieldType type)\n
    (final String name, final TokenStream tokenStream, final IndexableFieldType type)\n
    (final String name, final byte[] value, final IndexableFieldType type)\n
    (final String name, final byte[] value, final int offset, final int length, final IndexableFieldType type)\n
    (final String name, final BytesRef bytes, final IndexableFieldType type)\n
    (final String name, final CharSequence value, final IndexableFieldType type)\n
    '''
def stringValue():
    '''returns String\n\n
    stringValue()\n
    '''
def getCharSequenceValue():
    '''returns CharSequence\n\n
    getCharSequenceValue()\n
    '''
def readerValue():
    '''returns Reader\n\n
    readerValue()\n
    '''
def tokenStreamValue():
    '''returns TokenStream\n\n
    tokenStreamValue()\n
    '''
def setStringValue():
    '''returns None\n\n
    setStringValue(final String value)\n
    '''
def setReaderValue():
    '''returns None\n\n
    setReaderValue(final Reader value)\n
    '''
def setBytesValue():
    '''returns None\n\n
    setBytesValue(final byte[] value)\n
    setBytesValue(final BytesRef value)\n
    '''
def setByteValue():
    '''returns None\n\n
    setByteValue(final byte value)\n
    '''
def setShortValue():
    '''returns None\n\n
    setShortValue(final short value)\n
    '''
def setIntValue():
    '''returns None\n\n
    setIntValue(final int value)\n
    '''
def setLongValue():
    '''returns None\n\n
    setLongValue(final long value)\n
    '''
def setFloatValue():
    '''returns None\n\n
    setFloatValue(final float value)\n
    '''
def setDoubleValue():
    '''returns None\n\n
    setDoubleValue(final double value)\n
    '''
def setTokenStream():
    '''returns None\n\n
    setTokenStream(final TokenStream tokenStream)\n
    '''
def name():
    '''returns String\n\n
    name()\n
    '''
def numericValue():
    '''returns Number\n\n
    numericValue()\n
    '''
def binaryValue():
    '''returns BytesRef\n\n
    binaryValue()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def fieldType():
    '''returns IndexableFieldType\n\n
    fieldType()\n
    '''
def tokenStream():
    '''returns TokenStream\n\n
    tokenStream(final Analyzer analyzer, TokenStream reuse)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final BytesRef value)\n
    '''
def incrementToken():
    '''returns boolean\n\n
    incrementToken()\n
    incrementToken()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    reset()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    close()\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
