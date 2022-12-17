DEFAULT_RCDSIZE = "int  512"
DEFAULT_BLKSIZE = "int  10240"
def ():
    '''returns TarBuffer\n\n
    (final InputStream inStream)\n
    (final InputStream inStream, final int blockSize)\n
    (final InputStream inStream, final int blockSize, final int recordSize)\n
    (final OutputStream outStream)\n
    (final OutputStream outStream, final int blockSize)\n
    (final OutputStream outStream, final int blockSize, final int recordSize)\n
    '''
def getBlockSize():
    '''returns int\n\n
    getBlockSize()\n
    '''
def getRecordSize():
    '''returns int\n\n
    getRecordSize()\n
    '''
def setDebug():
    '''returns None\n\n
    setDebug(final boolean debug)\n
    '''
def isEOFRecord():
    '''returns boolean\n\n
    isEOFRecord(final byte[] record)\n
    '''
def skipRecord():
    '''returns None\n\n
    skipRecord()\n
    '''
def readRecord():
    '''returns byte[]\n\n
    readRecord()\n
    '''
def getCurrentBlockNum():
    '''returns int\n\n
    getCurrentBlockNum()\n
    '''
def getCurrentRecordNum():
    '''returns int\n\n
    getCurrentRecordNum()\n
    '''
def writeRecord():
    '''returns None\n\n
    writeRecord(final byte[] record)\n
    writeRecord(final byte[] buf, final int offset)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
