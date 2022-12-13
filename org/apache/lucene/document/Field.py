def Field():
'''public Field(final String name, final Reader reader, final IndexableFieldType type)
public Field(final String name, final TokenStream tokenStream, final IndexableFieldType type)
public Field(final String name, final byte[] value, final IndexableFieldType type)
public Field(final String name, final byte[] value, final int offset, final int length, final IndexableFieldType type)
public Field(final String name, final BytesRef bytes, final IndexableFieldType type)
public Field(final String name, final CharSequence value, final IndexableFieldType type)
'''
pass
def stringValue():
'''public String stringValue()
'''
pass
def getCharSequenceValue():
'''public CharSequence getCharSequenceValue()
'''
pass
def readerValue():
'''public Reader readerValue()
'''
pass
def tokenStreamValue():
'''public TokenStream tokenStreamValue()
'''
pass
def setStringValue():
'''public void setStringValue(final String value)
'''
pass
def setReaderValue():
'''public void setReaderValue(final Reader value)
'''
pass
def setBytesValue():
'''public void setBytesValue(final byte[] value)
public void setBytesValue(final BytesRef value)
'''
pass
def setByteValue():
'''public void setByteValue(final byte value)
'''
pass
def setShortValue():
'''public void setShortValue(final short value)
'''
pass
def setIntValue():
'''public void setIntValue(final int value)
'''
pass
def setLongValue():
'''public void setLongValue(final long value)
'''
pass
def setFloatValue():
'''public void setFloatValue(final float value)
'''
pass
def setDoubleValue():
'''public void setDoubleValue(final double value)
'''
pass
def setTokenStream():
'''public void setTokenStream(final TokenStream tokenStream)
'''
pass
def name():
'''public String name()
'''
pass
def numericValue():
'''public Number numericValue()
'''
pass
def binaryValue():
'''public BytesRef binaryValue()
'''
pass
def toString():
'''public String toString()
'''
pass
def fieldType():
'''public IndexableFieldType fieldType()
'''
pass
def tokenStream():
'''public TokenStream tokenStream(final Analyzer analyzer, TokenStream reuse)
'''
pass
def setValue():
'''public void setValue(final BytesRef value)
'''
pass
def incrementToken():
'''public boolean incrementToken()
public boolean incrementToken()
'''
pass
def reset():
'''public void reset()
public void reset()
'''
pass
def close():
'''public void close()
public void close()
'''
pass
def end():
'''public void end()
'''
pass
