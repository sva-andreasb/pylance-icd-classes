MAGIC = "int  407708164"
LZ4_MAX_HEADER_LENGTH = "int  19"
LZ4_FRAME_INCOMPRESSIBLE_MASK = "int  Integer.MIN_VALUE"
CLOSED_STREAM = "String  \"The stream is already closed\""
BLOCKSIZE_64KB = "int  4"
BLOCKSIZE_256KB = "int  5"
BLOCKSIZE_1MB = "int  6"
BLOCKSIZE_4MB = "int  7"
def ():
    '''returns BD\n\n
    (final OutputStream out, final int blockSize, final boolean blockChecksum, final boolean useBrokenFlagDescriptorChecksum)\n
    (final OutputStream out, final int blockSize, final boolean blockChecksum)\n
    (final OutputStream out, final int blockSize)\n
    (final OutputStream out)\n
    (final OutputStream out, final boolean useBrokenHC)\n
    ()\n
    (final boolean blockChecksum)\n
    ()\n
    (final int blockSizeValue)\n
    '''
def useBrokenFlagDescriptorChecksum():
    '''returns boolean\n\n
    useBrokenFlagDescriptorChecksum()\n
    '''
def write():
    '''returns None\n\n
    write(final int b)\n
    write(final byte[] b, int off, int len)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def toByte():
    '''returns byte\n\n
    toByte()\n
    toByte()\n
    '''
def isContentChecksumSet():
    '''returns boolean\n\n
    isContentChecksumSet()\n
    '''
def isContentSizeSet():
    '''returns boolean\n\n
    isContentSizeSet()\n
    '''
def isBlockChecksumSet():
    '''returns boolean\n\n
    isBlockChecksumSet()\n
    '''
def isBlockIndependenceSet():
    '''returns boolean\n\n
    isBlockIndependenceSet()\n
    '''
def getVersion():
    '''returns int\n\n
    getVersion()\n
    '''
def getBlockMaximumSize():
    '''returns int\n\n
    getBlockMaximumSize()\n
    '''
