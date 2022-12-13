CR = "byte  13"
LF = "byte  10"
DASH = "byte  45"
HEADER_PART_SIZE_MAX = "int  10240"
def MultipartStream():
    '''public MultipartStream()
    public MultipartStream(final InputStream input, final byte[] boundary, final int bufSize)
    public MultipartStream(final InputStream input, final byte[] boundary, final int bufSize, final ProgressNotifier pNotifier)
    public MultipartStream(final InputStream input, final byte[] boundary)
    '''
def getHeaderEncoding():
    '''public String getHeaderEncoding()
    '''
def setHeaderEncoding():
    '''public void setHeaderEncoding(final String encoding)
    '''
def readByte():
    '''public byte readByte()
    '''
def readBoundary():
    '''public boolean readBoundary()
    '''
def setBoundary():
    '''public void setBoundary(final byte[] boundary)
    '''
def readHeaders():
    '''public String readHeaders()
    '''
def readBodyData():
    '''public int readBodyData(final OutputStream output)
    '''
def discardBodyData():
    '''public int discardBodyData()
    '''
def skipPreamble():
    '''public boolean skipPreamble()
    '''
def arrayequals():
    '''public static boolean arrayequals(final byte[] a, final byte[] b, final int count)
    '''
def MalformedStreamException():
    '''public MalformedStreamException()
    public MalformedStreamException(final String message)
    '''
def IllegalBoundaryException():
    '''public IllegalBoundaryException()
    public IllegalBoundaryException(final String message)
    '''
def getBytesRead():
    '''public long getBytesRead()
    '''
def available():
    '''public int available()
    '''
def read():
    '''public int read()
    public int read(final byte[] b, final int off, final int len)
    '''
def close():
    '''public void close()
    public void close(final boolean pCloseUnderlying)
    '''
def skip():
    '''public long skip(final long bytes)
    '''
def isClosed():
    '''public boolean isClosed()
    '''
