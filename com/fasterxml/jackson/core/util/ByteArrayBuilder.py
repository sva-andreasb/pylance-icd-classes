def ByteArrayBuilder():
    '''public ByteArrayBuilder()
    public ByteArrayBuilder(final BufferRecycler br)
    public ByteArrayBuilder(final int firstBlockSize)
    public ByteArrayBuilder(final BufferRecycler br, final int firstBlockSize)
    '''
def reset():
    '''public void reset()
    '''
def size():
    '''public int size()
    '''
def release():
    '''public void release()
    '''
def append():
    '''public void append(final int i)
    '''
def appendTwoBytes():
    '''public void appendTwoBytes(final int b16)
    '''
def appendThreeBytes():
    '''public void appendThreeBytes(final int b24)
    '''
def appendFourBytes():
    '''public void appendFourBytes(final int b32)
    '''
def toByteArray():
    '''public byte[] toByteArray()
    '''
def resetAndGetFirstSegment():
    '''public byte[] resetAndGetFirstSegment()
    '''
def finishCurrentSegment():
    '''public byte[] finishCurrentSegment()
    '''
def completeAndCoalesce():
    '''public byte[] completeAndCoalesce(final int lastBlockLength)
    '''
def getCurrentSegment():
    '''public byte[] getCurrentSegment()
    '''
def setCurrentSegmentLength():
    '''public void setCurrentSegmentLength(final int len)
    '''
def getCurrentSegmentLength():
    '''public int getCurrentSegmentLength()
    '''
def write():
    '''public void write(final byte[] b)
    public void write(final byte[] b, int off, int len)
    public void write(final int b)
    '''
def close():
    '''public void close()
    '''
def flush():
    '''public void flush()
    '''
