def ():
    '''returns FileBackedDataSource\n\n
    (final File file)\n
    (final File file, final boolean readOnly)\n
    (final RandomAccessFile srcFile, final boolean readOnly)\n
    (final FileChannel channel, final boolean readOnly)\n
    '''
def isWriteable():
    '''returns boolean\n\n
    isWriteable()\n
    '''
def getChannel():
    '''returns FileChannel\n\n
    getChannel()\n
    '''
def read():
    '''returns ByteBuffer\n\n
    read(final int length, final long position)\n
    '''
def write():
    '''returns None\n\n
    write(final ByteBuffer src, final long position)\n
    '''
def copyTo():
    '''returns None\n\n
    copyTo(final OutputStream stream)\n
    '''
def size():
    '''returns long\n\n
    size()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def run():
    '''returns Void\n\n
    run()\n
    '''
