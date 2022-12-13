def TextBuffer():
    '''public TextBuffer(final BufferRecycler allocator)
    '''
def releaseBuffers():
    '''public void releaseBuffers()
    '''
def resetWithEmpty():
    '''public void resetWithEmpty()
    '''
def resetWith():
    '''public void resetWith(final char ch)
    '''
def resetWithShared():
    '''public void resetWithShared(final char[] buf, final int start, final int len)
    '''
def resetWithCopy():
    '''public void resetWithCopy(final char[] buf, final int start, final int len)
    public void resetWithCopy(final String text, final int start, final int len)
    '''
def resetWithString():
    '''public void resetWithString(final String value)
    '''
def getBufferWithoutReset():
    '''public char[] getBufferWithoutReset()
    '''
def size():
    '''public int size()
    '''
def getTextOffset():
    '''public int getTextOffset()
    '''
def hasTextAsCharacters():
    '''public boolean hasTextAsCharacters()
    '''
def getTextBuffer():
    '''public char[] getTextBuffer()
    '''
def contentsAsString():
    '''public String contentsAsString()
    '''
def contentsAsArray():
    '''public char[] contentsAsArray()
    '''
def contentsAsDecimal():
    '''public BigDecimal contentsAsDecimal()
    '''
def contentsAsDouble():
    '''public double contentsAsDouble()
    '''
def contentsAsInt():
    '''public int contentsAsInt(final boolean neg)
    '''
def contentsAsLong():
    '''public long contentsAsLong(final boolean neg)
    '''
def contentsToWriter():
    '''public int contentsToWriter(final Writer w)
    '''
def ensureNotShared():
    '''public void ensureNotShared()
    '''
def append():
    '''public void append(final char c)
    public void append(final char[] c, int start, int len)
    public void append(final String str, int offset, int len)
    '''
def getCurrentSegment():
    '''public char[] getCurrentSegment()
    '''
def emptyAndGetCurrentSegment():
    '''public char[] emptyAndGetCurrentSegment()
    '''
def getCurrentSegmentSize():
    '''public int getCurrentSegmentSize()
    '''
def setCurrentLength():
    '''public void setCurrentLength(final int len)
    '''
def setCurrentAndReturn():
    '''public String setCurrentAndReturn(final int len)
    '''
def finishCurrentSegment():
    '''public char[] finishCurrentSegment()
    '''
def expandCurrentSegment():
    '''public char[] expandCurrentSegment()
    public char[] expandCurrentSegment(final int minSize)
    '''
def toString():
    '''public String toString()
    '''
