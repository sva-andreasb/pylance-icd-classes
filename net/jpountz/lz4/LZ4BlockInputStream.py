def ():
    '''returns LZ4BlockInputStream\n\n
    (final InputStream in, final LZ4FastDecompressor decompressor, final Checksum checksum, final boolean stopOnEmptyBlock)\n
    (final InputStream in, final LZ4FastDecompressor decompressor, final Checksum checksum)\n
    (final InputStream in, final LZ4FastDecompressor decompressor)\n
    (final InputStream in, final boolean stopOnEmptyBlock)\n
    (final InputStream in)\n
    '''
def available():
    '''returns int\n\n
    available()\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] b, final int off, int len)\n
    read(final byte[] b)\n
    '''
def skip():
    '''returns long\n\n
    skip(final long n)\n
    '''
def markSupported():
    '''returns boolean\n\n
    markSupported()\n
    '''
def mark():
    '''returns None\n\n
    mark(final int readlimit)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
