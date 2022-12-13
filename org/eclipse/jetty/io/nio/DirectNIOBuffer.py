def DirectNIOBuffer():
    '''    public DirectNIOBuffer(final int size)
    public DirectNIOBuffer(final ByteBuffer buffer, final boolean immutable)
    public DirectNIOBuffer(final File file)
    '''
def isDirect():
    '''    public boolean isDirect()
    '''
def array():
    '''    public byte[] array()
    '''
def capacity():
    '''    public int capacity()
    '''
def peek():
    '''    public byte peek(final int position)
    public int peek(final int index, final byte[] b, final int offset, final int length)
    '''
def poke():
    '''    public void poke(final int index, final byte b)
    public int poke(final int index, final Buffer src)
    public int poke(final int index, final byte[] b, final int offset, int length)
    '''
def getByteBuffer():
    '''    public ByteBuffer getByteBuffer()
    '''
def readFrom():
    '''    public int readFrom(final InputStream in, int max)
    '''
def writeTo():
    '''    public void writeTo(final OutputStream out)
    '''
