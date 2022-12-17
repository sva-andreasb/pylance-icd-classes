def ():
    '''returns DirectNIOBuffer\n\n
    (final int size)\n
    (final ByteBuffer buffer, final boolean immutable)\n
    (final File file)\n
    '''
def isDirect():
    '''returns boolean\n\n
    isDirect()\n
    '''
def array():
    '''returns byte[]\n\n
    array()\n
    '''
def capacity():
    '''returns int\n\n
    capacity()\n
    '''
def peek():
    '''returns int\n\n
    peek(final int position)\n
    peek(final int index, final byte[] b, final int offset, final int length)\n
    '''
def poke():
    '''returns int\n\n
    poke(final int index, final byte b)\n
    poke(final int index, final Buffer src)\n
    poke(final int index, final byte[] b, final int offset, int length)\n
    '''
def getByteBuffer():
    '''returns ByteBuffer\n\n
    getByteBuffer()\n
    '''
def readFrom():
    '''returns int\n\n
    readFrom(final InputStream in, int max)\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final OutputStream out)\n
    '''
