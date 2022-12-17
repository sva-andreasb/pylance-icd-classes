def ():
    '''returns SessionInputBufferImpl\n\n
    (final HttpTransportMetricsImpl metrics, final int buffersize, final int minChunkLimit, final MessageConstraints constraints, final CharsetDecoder chardecoder)\n
    (final HttpTransportMetricsImpl metrics, final int buffersize)\n
    '''
def bind():
    '''returns None\n\n
    bind(final InputStream instream)\n
    '''
def isBound():
    '''returns boolean\n\n
    isBound()\n
    '''
def capacity():
    '''returns int\n\n
    capacity()\n
    '''
def length():
    '''returns int\n\n
    length()\n
    '''
def available():
    '''returns int\n\n
    available()\n
    '''
def fillBuffer():
    '''returns int\n\n
    fillBuffer()\n
    '''
def hasBufferedData():
    '''returns boolean\n\n
    hasBufferedData()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] b, final int off, final int len)\n
    read(final byte[] b)\n
    '''
def readLine():
    '''returns String\n\n
    readLine(final CharArrayBuffer charbuffer)\n
    readLine()\n
    '''
def isDataAvailable():
    '''returns boolean\n\n
    isDataAvailable(final int timeout)\n
    '''
def getMetrics():
    '''returns HttpTransportMetrics\n\n
    getMetrics()\n
    '''
