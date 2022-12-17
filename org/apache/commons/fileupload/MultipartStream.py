CR = "byte  13"
LF = "byte  10"
DASH = "byte  45"
HEADER_PART_SIZE_MAX = "int  10240"
def ():
    '''returns IllegalBoundaryException\n\n
    ()\n
    (final InputStream input, final byte[] boundary, final int bufSize)\n
    (final InputStream input, final byte[] boundary, final int bufSize, final ProgressNotifier pNotifier)\n
    (final InputStream input, final byte[] boundary)\n
    ()\n
    (final String message)\n
    ()\n
    (final String message)\n
    '''
def getHeaderEncoding():
    '''returns String\n\n
    getHeaderEncoding()\n
    '''
def setHeaderEncoding():
    '''returns None\n\n
    setHeaderEncoding(final String encoding)\n
    '''
def readByte():
    '''returns byte\n\n
    readByte()\n
    '''
def readBoundary():
    '''returns boolean\n\n
    readBoundary()\n
    '''
def setBoundary():
    '''returns None\n\n
    setBoundary(final byte[] boundary)\n
    '''
def readHeaders():
    '''returns String\n\n
    readHeaders()\n
    '''
def readBodyData():
    '''returns int\n\n
    readBodyData(final OutputStream output)\n
    '''
def discardBodyData():
    '''returns int\n\n
    discardBodyData()\n
    '''
def skipPreamble():
    '''returns boolean\n\n
    skipPreamble()\n
    '''
def getBytesRead():
    '''returns long\n\n
    getBytesRead()\n
    '''
def available():
    '''returns int\n\n
    available()\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] b, final int off, final int len)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    close(final boolean pCloseUnderlying)\n
    '''
def skip():
    '''returns long\n\n
    skip(final long bytes)\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
