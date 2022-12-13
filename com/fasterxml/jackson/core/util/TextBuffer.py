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
def resetWith():
'''public void resetWith(final char ch)
'''
pass
def resetWithShared():
'''public void resetWithShared(final char[] buf, final int start, final int len)
'''
pass
def resetWithCopy():
'''public void resetWithCopy(final char[] buf, final int start, final int len)
public void resetWithCopy(final String text, final int start, final int len)
'''
pass
def resetWithString():
'''public void resetWithString(final String value)
'''
pass
def getBufferWithoutReset():
'''public char[] getBufferWithoutReset()
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
def contentsAsInt():
'''public int contentsAsInt(final boolean neg)
'''
pass
def contentsAsLong():
'''public long contentsAsLong(final boolean neg)
'''
pass
def contentsToWriter():
'''public int contentsToWriter(final Writer w)
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
'''public char[] emptyAndGetCurrentSegment()
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
def setCurrentAndReturn():
'''public String setCurrentAndReturn(final int len)
'''
pass
def finishCurrentSegment():
'''public char[] finishCurrentSegment()
'''
pass
def expandCurrentSegment():
'''public char[] expandCurrentSegment()
public char[] expandCurrentSegment(final int minSize)
'''
pass
def toString():
'''public String toString()
'''
pass
