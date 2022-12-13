def AbstractBuffer():
    '''    public AbstractBuffer(final int access, final boolean isVolatile)
    '''
def asArray():
    '''    public byte[] asArray()
    '''
def duplicate():
    '''    public ByteArrayBuffer duplicate(final int access)
    '''
def asNonVolatileBuffer():
    '''    public Buffer asNonVolatileBuffer()
    '''
def asImmutableBuffer():
    '''    public Buffer asImmutableBuffer()
    '''
def asReadOnlyBuffer():
    '''    public Buffer asReadOnlyBuffer()
    '''
def asMutableBuffer():
    '''    public Buffer asMutableBuffer()
    '''
def buffer():
    '''    public Buffer buffer()
    '''
def clear():
    '''    public void clear()
    '''
def compact():
    '''    public void compact()
    '''
def equals():
    '''    public boolean equals(final Object obj)
    '''
def equalsIgnoreCase():
    '''    public boolean equalsIgnoreCase(final Buffer b)
    '''
def get():
    '''    public byte get()
    public int get(final byte[] b, final int offset, int length)
    public Buffer get(final int length)
    '''
def getIndex():
    '''    public final int getIndex()
    '''
def hasContent():
    '''    public boolean hasContent()
    '''
def hashCode():
    '''    public int hashCode()
    '''
def isImmutable():
    '''    public boolean isImmutable()
    '''
def isReadOnly():
    '''    public boolean isReadOnly()
    '''
def isVolatile():
    '''    public boolean isVolatile()
    '''
def length():
    '''    public int length()
    '''
def mark():
    '''    public void mark()
    public void mark(final int offset)
    '''
def markIndex():
    '''    public int markIndex()
    '''
def peek():
    '''    public byte peek()
    public Buffer peek(final int index, final int length)
    '''
def poke():
    '''    public int poke(int index, final Buffer src)
    public int poke(int index, final byte[] b, final int offset, int length)
    '''
def put():
    '''    public int put(final Buffer src)
    public void put(final byte b)
    public int put(final byte[] b, final int offset, final int length)
    public int put(final byte[] b)
    '''
def putIndex():
    '''    public final int putIndex()
    '''
def reset():
    '''    public void reset()
    '''
def rewind():
    '''    public void rewind()
    '''
def setGetIndex():
    '''    public void setGetIndex(final int getIndex)
    '''
def setMarkIndex():
    '''    public void setMarkIndex(final int index)
    '''
def setPutIndex():
    '''    public void setPutIndex(final int putIndex)
    '''
def skip():
    '''    public int skip(int n)
    '''
def slice():
    '''    public Buffer slice()
    '''
def sliceFromMark():
    '''    public Buffer sliceFromMark()
    public Buffer sliceFromMark(final int length)
    '''
def space():
    '''    public int space()
    '''
def toDetailString():
    '''    public String toDetailString()
    '''
def toString():
    '''    public String toString()
    public String toString(final String charset)
    '''
def toDebugString():
    '''    public String toDebugString()
    '''
def writeTo():
    '''    public void writeTo(final OutputStream out)
    '''
def readFrom():
    '''    public int readFrom(final InputStream in, final int max)
    '''
