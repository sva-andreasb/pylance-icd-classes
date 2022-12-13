def SessionInputBufferImpl():
    '''    public SessionInputBufferImpl(final HttpTransportMetricsImpl metrics, final int buffersize, final int minChunkLimit, final MessageConstraints constraints, final CharsetDecoder chardecoder)
    public SessionInputBufferImpl(final HttpTransportMetricsImpl metrics, final int buffersize)
    '''
def bind():
    '''    public void bind(final InputStream instream)
    '''
def isBound():
    '''    public boolean isBound()
    '''
def capacity():
    '''    public int capacity()
    '''
def length():
    '''    public int length()
    '''
def available():
    '''    public int available()
    '''
def fillBuffer():
    '''    public int fillBuffer()
    '''
def hasBufferedData():
    '''    public boolean hasBufferedData()
    '''
def clear():
    '''    public void clear()
    '''
def read():
    '''    public int read()
    public int read(final byte[] b, final int off, final int len)
    public int read(final byte[] b)
    '''
def readLine():
    '''    public int readLine(final CharArrayBuffer charbuffer)
    public String readLine()
    '''
def isDataAvailable():
    '''    public boolean isDataAvailable(final int timeout)
    '''
def getMetrics():
    '''    public HttpTransportMetrics getMetrics()
    '''
