def ():
    '''returns ByteBufferOutputStream\n\n
    (final ByteBuffer buffer)\n
    (final int initialCapacity)\n
    (final int initialCapacity, final boolean directBuffer)\n
    '''
def write():
    '''returns None\n\n
    write(final int b)\n
    write(final byte[] bytes, final int off, final int len)\n
    write(final ByteBuffer sourceBuffer)\n
    '''
def buffer():
    '''returns ByteBuffer\n\n
    buffer()\n
    '''
def position():
    '''returns None\n\n
    position()\n
    position(final int position)\n
    '''
def remaining():
    '''returns int\n\n
    remaining()\n
    '''
def limit():
    '''returns int\n\n
    limit()\n
    '''
def initialCapacity():
    '''returns int\n\n
    initialCapacity()\n
    '''
def ensureRemaining():
    '''returns None\n\n
    ensureRemaining(final int remainingBytesRequired)\n
    '''
