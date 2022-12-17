def ():
    '''returns FrameData\n\n
    (final InputStream inputStream)\n
    (final InputStream in, final boolean b)\n
    (final ReadableByteChannel readableByteChannel)\n
    (final ReadableByteChannel rbc, final boolean verifyChecksums)\n
    (final FrameAction frameAction, final int length)\n
    (final int checkSum, final int offset)\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] array, final int i, final int n)\n
    read(final ByteBuffer byteBuffer)\n
    '''
def available():
    '''returns int\n\n
    available()\n
    '''
def isOpen():
    '''returns boolean\n\n
    isOpen()\n
    '''
def transferTo():
    '''returns long\n\n
    transferTo(final OutputStream outputStream)\n
    transferTo(final WritableByteChannel writableByteChannel)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
