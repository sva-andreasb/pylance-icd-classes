def ():
    '''returns SQLServerBlob\n\n
    (final SQLServerConnection connection, final byte[] data)\n
    '''
def free():
    '''returns None\n\n
    free()\n
    '''
def getBinaryStream():
    '''returns InputStream\n\n
    getBinaryStream()\n
    getBinaryStream(final long pos, final long length)\n
    '''
def getBytes():
    '''returns byte[]\n\n
    getBytes(long pos, int length)\n
    '''
def length():
    '''returns long\n\n
    length()\n
    '''
def position():
    '''returns long\n\n
    position(final Blob pattern, final long start)\n
    position(final byte[] bPattern, long start)\n
    '''
def truncate():
    '''returns None\n\n
    truncate(final long len)\n
    '''
def setBinaryStream():
    '''returns OutputStream\n\n
    setBinaryStream(final long pos)\n
    '''
def setBytes():
    '''returns int\n\n
    setBytes(final long pos, final byte[] bytes)\n
    setBytes(long pos, final byte[] bytes, final int offset, final int len)\n
    '''
