def AbstractBuffer():
'''public AbstractBuffer(final int access, final boolean isVolatile)
'''
pass
def asArray():
'''public byte[] asArray()
'''
pass
def duplicate():
'''public ByteArrayBuffer duplicate(final int access)
'''
pass
def asNonVolatileBuffer():
'''public Buffer asNonVolatileBuffer()
'''
pass
def asImmutableBuffer():
'''public Buffer asImmutableBuffer()
'''
pass
def asReadOnlyBuffer():
'''public Buffer asReadOnlyBuffer()
'''
pass
def asMutableBuffer():
'''public Buffer asMutableBuffer()
'''
pass
def buffer():
'''public Buffer buffer()
'''
pass
def clear():
'''public void clear()
'''
pass
def compact():
'''public void compact()
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
def equalsIgnoreCase():
'''public boolean equalsIgnoreCase(final Buffer b)
'''
pass
def get():
'''public byte get()
public int get(final byte[] b, final int offset, int length)
public Buffer get(final int length)
'''
pass
def getIndex():
'''public final int getIndex()
'''
pass
def hasContent():
'''public boolean hasContent()
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def isImmutable():
'''public boolean isImmutable()
'''
pass
def isReadOnly():
'''public boolean isReadOnly()
'''
pass
def isVolatile():
'''public boolean isVolatile()
'''
pass
def length():
'''public int length()
'''
pass
def mark():
'''public void mark()
public void mark(final int offset)
'''
pass
def markIndex():
'''public int markIndex()
'''
pass
def peek():
'''public byte peek()
public Buffer peek(final int index, final int length)
'''
pass
def poke():
'''public int poke(int index, final Buffer src)
public int poke(int index, final byte[] b, final int offset, int length)
'''
pass
def put():
'''public int put(final Buffer src)
public void put(final byte b)
public int put(final byte[] b, final int offset, final int length)
public int put(final byte[] b)
'''
pass
def putIndex():
'''public final int putIndex()
'''
pass
def reset():
'''public void reset()
'''
pass
def rewind():
'''public void rewind()
'''
pass
def setGetIndex():
'''public void setGetIndex(final int getIndex)
'''
pass
def setMarkIndex():
'''public void setMarkIndex(final int index)
'''
pass
def setPutIndex():
'''public void setPutIndex(final int putIndex)
'''
pass
def skip():
'''public int skip(int n)
'''
pass
def slice():
'''public Buffer slice()
'''
pass
def sliceFromMark():
'''public Buffer sliceFromMark()
public Buffer sliceFromMark(final int length)
'''
pass
def space():
'''public int space()
'''
pass
def toDetailString():
'''public String toDetailString()
'''
pass
def toString():
'''public String toString()
public String toString(final String charset)
'''
pass
def toDebugString():
'''public String toDebugString()
'''
pass
def writeTo():
'''public void writeTo(final OutputStream out)
'''
pass
def readFrom():
'''public int readFrom(final InputStream in, final int max)
'''
pass
