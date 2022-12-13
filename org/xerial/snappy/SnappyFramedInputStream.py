def SnappyFramedInputStream():
'''public SnappyFramedInputStream(final InputStream inputStream)
public SnappyFramedInputStream(final InputStream in, final boolean b)
public SnappyFramedInputStream(final ReadableByteChannel readableByteChannel)
public SnappyFramedInputStream(final ReadableByteChannel rbc, final boolean verifyChecksums)
'''
pass
def read():
'''public int read()
public int read(final byte[] array, final int i, final int n)
public int read(final ByteBuffer byteBuffer)
'''
pass
def available():
'''public int available()
'''
pass
def isOpen():
'''public boolean isOpen()
'''
pass
def transferTo():
'''public long transferTo(final OutputStream outputStream)
public long transferTo(final WritableByteChannel writableByteChannel)
'''
pass
def close():
'''public void close()
'''
pass
def FrameMetaData():
'''public FrameMetaData(final FrameAction frameAction, final int length)
'''
pass
def FrameData():
'''public FrameData(final int checkSum, final int offset)
'''
pass
