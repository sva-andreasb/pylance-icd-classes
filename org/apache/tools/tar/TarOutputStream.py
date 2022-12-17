LONGFILE_ERROR = "int  0"
LONGFILE_TRUNCATE = "int  1"
LONGFILE_GNU = "int  2"
def ():
    '''returns TarOutputStream\n\n
    (final OutputStream os)\n
    (final OutputStream os, final int blockSize)\n
    (final OutputStream os, final int blockSize, final int recordSize)\n
    '''
def setLongFileMode():
    '''returns None\n\n
    setLongFileMode(final int longFileMode)\n
    '''
def setDebug():
    '''returns None\n\n
    setDebug(final boolean debugF)\n
    '''
def setBufferDebug():
    '''returns None\n\n
    setBufferDebug(final boolean debug)\n
    '''
def finish():
    '''returns None\n\n
    finish()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getRecordSize():
    '''returns int\n\n
    getRecordSize()\n
    '''
def putNextEntry():
    '''returns None\n\n
    putNextEntry(final TarEntry entry)\n
    '''
def closeEntry():
    '''returns None\n\n
    closeEntry()\n
    '''
def write():
    '''returns None\n\n
    write(final int b)\n
    write(final byte[] wBuf)\n
    write(final byte[] wBuf, int wOffset, int numToWrite)\n
    '''
