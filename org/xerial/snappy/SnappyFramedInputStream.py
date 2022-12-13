def SnappyFramedInputStream():
    '''    public SnappyFramedInputStream(final InputStream inputStream)
    public SnappyFramedInputStream(final InputStream in, final boolean b)
    public SnappyFramedInputStream(final ReadableByteChannel readableByteChannel)
    public SnappyFramedInputStream(final ReadableByteChannel rbc, final boolean verifyChecksums)
    '''
def read():
    '''    public int read()
    public int read(final byte[] array, final int i, final int n)
    public int read(final ByteBuffer byteBuffer)
    '''
def available():
    '''    public int available()
    '''
def isOpen():
    '''    public boolean isOpen()
    '''
def transferTo():
    '''    public long transferTo(final OutputStream outputStream)
    public long transferTo(final WritableByteChannel writableByteChannel)
    '''
def close():
    '''    public void close()
    '''
def FrameMetaData():
    '''    public FrameMetaData(final FrameAction frameAction, final int length)
    '''
def FrameData():
    '''    public FrameData(final int checkSum, final int offset)
    '''
