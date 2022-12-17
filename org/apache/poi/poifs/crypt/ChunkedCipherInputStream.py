def ():
    '''returns ChunkedCipherInputStream\n\n
    (final InputStream stream, final long size, final int chunkSize)\n
    (final InputStream stream, final long size, final int chunkSize, final int initialPos)\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] b, final int off, final int len)\n
    '''
def skip():
    '''returns long\n\n
    skip(final long n)\n
    '''
def available():
    '''returns int\n\n
    available()\n
    '''
def markSupported():
    '''returns boolean\n\n
    markSupported()\n
    '''
def readPlain():
    '''returns None\n\n
    readPlain(final byte[] b, final int off, final int len)\n
    '''
def setNextRecordSize():
    '''returns None\n\n
    setNextRecordSize(final int recordSize)\n
    '''
def getPos():
    '''returns long\n\n
    getPos()\n
    '''
