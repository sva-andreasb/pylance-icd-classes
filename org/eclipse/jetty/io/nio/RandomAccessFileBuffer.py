def ():
    '''returns RandomAccessFileBuffer\n\n
    (final File file)\n
    (final File file, final int capacity)\n
    (final File file, final int capacity, final int access)\n
    '''
def array():
    '''returns byte[]\n\n
    array()\n
    '''
def capacity():
    '''returns int\n\n
    capacity()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def peek():
    '''returns int\n\n
    peek()\n
    peek(final int index)\n
    peek(final int index, final byte[] b, final int offset, final int length)\n
    '''
def poke():
    '''returns int\n\n
    poke(final int index, final byte b)\n
    poke(final int index, final byte[] b, final int offset, final int length)\n
    '''
def writeTo():
    '''returns int\n\n
    writeTo(final WritableByteChannel channel, final int index, final int length)\n
    '''
