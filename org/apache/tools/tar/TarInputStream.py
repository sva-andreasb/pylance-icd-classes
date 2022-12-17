def ():
    '''returns TarInputStream\n\n
    (final InputStream is)\n
    (final InputStream is, final int blockSize)\n
    (final InputStream is, final int blockSize, final int recordSize)\n
    '''
def setDebug():
    '''returns None\n\n
    setDebug(final boolean debug)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getRecordSize():
    '''returns int\n\n
    getRecordSize()\n
    '''
def available():
    '''returns int\n\n
    available()\n
    '''
def skip():
    '''returns long\n\n
    skip(final long numToSkip)\n
    '''
def markSupported():
    '''returns boolean\n\n
    markSupported()\n
    '''
def mark():
    '''returns None\n\n
    mark(final int markLimit)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def getNextEntry():
    '''returns TarEntry\n\n
    getNextEntry()\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] buf, int offset, int numToRead)\n
    '''
def copyEntryContents():
    '''returns None\n\n
    copyEntryContents(final OutputStream out)\n
    '''
