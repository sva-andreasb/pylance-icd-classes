def ():
    '''returns SessionOutputBufferImpl\n\n
    (final HttpTransportMetricsImpl metrics, final int buffersize, final int fragementSizeHint, final CharsetEncoder charencoder)\n
    (final HttpTransportMetricsImpl metrics, final int buffersize)\n
    '''
def bind():
    '''returns None\n\n
    bind(final OutputStream outstream)\n
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
def flush():
    '''returns None\n\n
    flush()\n
    '''
def write():
    '''returns None\n\n
    write(final byte[] b, final int off, final int len)\n
    write(final byte[] b)\n
    write(final int b)\n
    '''
def writeLine():
    '''returns None\n\n
    writeLine(final String s)\n
    writeLine(final CharArrayBuffer charbuffer)\n
    '''
def getMetrics():
    '''returns HttpTransportMetrics\n\n
    getMetrics()\n
    '''
