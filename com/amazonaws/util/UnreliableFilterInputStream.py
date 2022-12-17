def ():
    '''returns UnreliableFilterInputStream\n\n
    (final InputStream in, final boolean isFakeIOException)\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] b, final int off, final int len)\n
    '''
def mark():
    '''returns None\n\n
    mark(final int readlimit)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def getCurrNumErrors():
    '''returns int\n\n
    getCurrNumErrors()\n
    '''
def getMaxNumErrors():
    '''returns int\n\n
    getMaxNumErrors()\n
    '''
def withMaxNumErrors():
    '''returns UnreliableFilterInputStream\n\n
    withMaxNumErrors(final int maxNumErrors)\n
    '''
def withBytesReadBeforeException():
    '''returns UnreliableFilterInputStream\n\n
    withBytesReadBeforeException(final int bytesReadBeforeException)\n
    '''
def getBytesReadBeforeException():
    '''returns int\n\n
    getBytesReadBeforeException()\n
    '''
def withResetIntervalBeforeException():
    '''returns UnreliableFilterInputStream\n\n
    withResetIntervalBeforeException(final int resetIntervalBeforeException)\n
    '''
def getResetIntervalBeforeException():
    '''returns int\n\n
    getResetIntervalBeforeException()\n
    '''
def getMarked():
    '''returns int\n\n
    getMarked()\n
    '''
def getPosition():
    '''returns int\n\n
    getPosition()\n
    '''
def isFakeIOException():
    '''returns boolean\n\n
    isFakeIOException()\n
    '''
def getResetCount():
    '''returns int\n\n
    getResetCount()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
