def BytesTrie():
    '''    public BytesTrie(final byte[] trieBytes, final int offset)
    public BytesTrie(final BytesTrie other)
    '''
def clone():
    '''    public BytesTrie clone()
    '''
def reset():
    '''    public BytesTrie reset()
    public Iterator reset()
    '''
def getState64():
    '''    public long getState64()
    '''
def resetToState64():
    '''    public BytesTrie resetToState64(final long state)
    '''
def saveState():
    '''    public BytesTrie saveState(final State state)
    '''
def resetToState():
    '''    public BytesTrie resetToState(final State state)
    '''
def current():
    '''    public Result current()
    '''
def first():
    '''    public Result first(int inByte)
    '''
def next():
    '''    public Result next(int inByte)
    public Result next(final byte[] s, int sIndex, final int sLimit)
    public Entry next()
    '''
def getValue():
    '''    public int getValue()
    '''
def getUniqueValue():
    '''    public long getUniqueValue()
    '''
def getNextBytes():
    '''    public int getNextBytes(final Appendable out)
    '''
def iterator():
    '''    public Iterator iterator()
    public Iterator iterator(final int maxStringLength)
    public static Iterator iterator(final byte[] trieBytes, final int offset, final int maxStringLength)
    '''
def matches():
    '''    public boolean matches()
    '''
def hasValue():
    '''    public boolean hasValue()
    '''
def hasNext():
    '''    public boolean hasNext()
    public boolean hasNext()
    '''
def bytesLength():
    '''    public int bytesLength()
    '''
def byteAt():
    '''    public byte byteAt(final int index)
    '''
def copyBytesTo():
    '''    public void copyBytesTo(final byte[] dest, final int destOffset)
    '''
def bytesAsByteBuffer():
    '''    public ByteBuffer bytesAsByteBuffer()
    '''
def remove():
    '''    public void remove()
    '''
