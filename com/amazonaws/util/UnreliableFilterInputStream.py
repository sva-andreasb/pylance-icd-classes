def UnreliableFilterInputStream():
    '''public UnreliableFilterInputStream(final InputStream in, final boolean isFakeIOException)
    '''
def read():
    '''public int read()
    public int read(final byte[] b, final int off, final int len)
    '''
def mark():
    '''public void mark(final int readlimit)
    '''
def reset():
    '''public void reset()
    '''
def getCurrNumErrors():
    '''public int getCurrNumErrors()
    '''
def getMaxNumErrors():
    '''public int getMaxNumErrors()
    '''
def withMaxNumErrors():
    '''public UnreliableFilterInputStream withMaxNumErrors(final int maxNumErrors)
    '''
def withBytesReadBeforeException():
    '''public UnreliableFilterInputStream withBytesReadBeforeException(final int bytesReadBeforeException)
    '''
def getBytesReadBeforeException():
    '''public int getBytesReadBeforeException()
    '''
def withResetIntervalBeforeException():
    '''public UnreliableFilterInputStream withResetIntervalBeforeException(final int resetIntervalBeforeException)
    '''
def getResetIntervalBeforeException():
    '''public int getResetIntervalBeforeException()
    '''
def getMarked():
    '''public int getMarked()
    '''
def getPosition():
    '''public int getPosition()
    '''
def isFakeIOException():
    '''public boolean isFakeIOException()
    '''
def getResetCount():
    '''public int getResetCount()
    '''
def toString():
    '''public String toString()
    '''
