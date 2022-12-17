MAX_BLOCK_SIZE = "int  65536"
DEFAULT_BLOCK_SIZE = "int  65536"
DEFAULT_MIN_COMPRESSION_RATIO = "double  0.85"
def ():
    '''returns SnappyFramedOutputStream\n\n
    (final OutputStream outputStream)\n
    (final OutputStream out, final int n, final double n2)\n
    (final WritableByteChannel writableByteChannel)\n
    (final WritableByteChannel out, final int capacity, final double n)\n
    '''
def isOpen():
    '''returns boolean\n\n
    isOpen()\n
    '''
def write():
    '''returns int\n\n
    write(final int n)\n
    write(final byte[] src, int offset, int i)\n
    write(final ByteBuffer src)\n
    '''
def transferFrom():
    '''returns long\n\n
    transferFrom(final InputStream inputStream)\n
    transferFrom(final ReadableByteChannel readableByteChannel)\n
    '''
