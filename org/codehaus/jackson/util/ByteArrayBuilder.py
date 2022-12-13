def ByteArrayBuilder():
'''public ByteArrayBuilder()
public ByteArrayBuilder(final BufferRecycler br)
public ByteArrayBuilder(final int firstBlockSize)
public ByteArrayBuilder(final BufferRecycler br, final int firstBlockSize)
'''
pass
def reset():
'''public void reset()
'''
pass
def release():
'''public void release()
'''
pass
def append():
'''public void append(final int i)
'''
pass
def appendTwoBytes():
'''public void appendTwoBytes(final int b16)
'''
pass
def appendThreeBytes():
'''public void appendThreeBytes(final int b24)
'''
pass
def toByteArray():
'''public byte[] toByteArray()
'''
pass
def resetAndGetFirstSegment():
'''public byte[] resetAndGetFirstSegment()
'''
pass
def finishCurrentSegment():
'''public byte[] finishCurrentSegment()
'''
pass
def completeAndCoalesce():
'''public byte[] completeAndCoalesce(final int lastBlockLength)
'''
pass
def getCurrentSegment():
'''public byte[] getCurrentSegment()
'''
pass
def setCurrentSegmentLength():
'''public void setCurrentSegmentLength(final int len)
'''
pass
def getCurrentSegmentLength():
'''public int getCurrentSegmentLength()
'''
pass
def write():
'''public void write(final byte[] b)
public void write(final byte[] b, int off, int len)
public void write(final int b)
'''
pass
def close():
'''public void close()
'''
pass
def flush():
'''public void flush()
'''
pass
