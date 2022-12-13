def TextBuffer():
'''public TextBuffer(final BufferRecycler allocator)
'''
pass
def releaseBuffers():
'''public void releaseBuffers()
'''
pass
def resetWithEmpty():
'''public void resetWithEmpty()
'''
pass
def resetWithShared():
'''public void resetWithShared(final char[] buf, final int start, final int len)
'''
pass
def resetWithCopy():
'''public void resetWithCopy(final char[] buf, final int start, final int len)
'''
pass
def resetWithString():
'''public void resetWithString(final String value)
'''
pass
def size():
'''public int size()
'''
pass
def getTextOffset():
'''public int getTextOffset()
'''
pass
def hasTextAsCharacters():
'''public boolean hasTextAsCharacters()
'''
pass
def getTextBuffer():
'''public char[] getTextBuffer()
'''
pass
def contentsAsString():
'''public String contentsAsString()
'''
pass
def contentsAsArray():
'''public char[] contentsAsArray()
'''
pass
def contentsAsDecimal():
'''public BigDecimal contentsAsDecimal()
'''
pass
def contentsAsDouble():
'''public double contentsAsDouble()
'''
pass
def ensureNotShared():
'''public void ensureNotShared()
'''
pass
def append():
'''public void append(final char c)
public void append(final char[] c, int start, int len)
public void append(final String str, int offset, int len)
'''
pass
def getCurrentSegment():
'''public char[] getCurrentSegment()
'''
pass
def emptyAndGetCurrentSegment():
'''public final char[] emptyAndGetCurrentSegment()
'''
pass
def getCurrentSegmentSize():
'''public int getCurrentSegmentSize()
'''
pass
def setCurrentLength():
'''public void setCurrentLength(final int len)
'''
pass
def finishCurrentSegment():
'''public char[] finishCurrentSegment()
'''
pass
def expandCurrentSegment():
'''public char[] expandCurrentSegment()
'''
pass
def toString():
'''public String toString()
'''
pass
