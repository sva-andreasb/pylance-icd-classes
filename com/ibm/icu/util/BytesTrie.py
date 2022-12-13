def BytesTrie():
'''public BytesTrie(final byte[] trieBytes, final int offset)
public BytesTrie(final BytesTrie other)
'''
pass
def clone():
'''public BytesTrie clone()
'''
pass
def reset():
'''public BytesTrie reset()
public Iterator reset()
'''
pass
def getState64():
'''public long getState64()
'''
pass
def resetToState64():
'''public BytesTrie resetToState64(final long state)
'''
pass
def saveState():
'''public BytesTrie saveState(final State state)
'''
pass
def resetToState():
'''public BytesTrie resetToState(final State state)
'''
pass
def current():
'''public Result current()
'''
pass
def first():
'''public Result first(int inByte)
'''
pass
def next():
'''public Result next(int inByte)
public Result next(final byte[] s, int sIndex, final int sLimit)
public Entry next()
'''
pass
def getValue():
'''public int getValue()
'''
pass
def getUniqueValue():
'''public long getUniqueValue()
'''
pass
def getNextBytes():
'''public int getNextBytes(final Appendable out)
'''
pass
def iterator():
'''public Iterator iterator()
public Iterator iterator(final int maxStringLength)
public static Iterator iterator(final byte[] trieBytes, final int offset, final int maxStringLength)
'''
pass
def matches():
'''public boolean matches()
'''
pass
def hasValue():
'''public boolean hasValue()
'''
pass
def hasNext():
'''public boolean hasNext()
public boolean hasNext()
'''
pass
def bytesLength():
'''public int bytesLength()
'''
pass
def byteAt():
'''public byte byteAt(final int index)
'''
pass
def copyBytesTo():
'''public void copyBytesTo(final byte[] dest, final int destOffset)
'''
pass
def bytesAsByteBuffer():
'''public ByteBuffer bytesAsByteBuffer()
'''
pass
def remove():
'''public void remove()
'''
pass
