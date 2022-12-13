def ByteArrayBuffer():
    '''public ByteArrayBuffer(final byte[] bytes)
    public ByteArrayBuffer(final byte[] bytes, final int index, final int length)
    public ByteArrayBuffer(final byte[] bytes, final int index, final int length, final int access)
    public ByteArrayBuffer(final byte[] bytes, final int index, final int length, final int access, final boolean isVolatile)
    public ByteArrayBuffer(final int size)
    public ByteArrayBuffer(final String value)
    public ByteArrayBuffer(final String value, final boolean immutable)
    public ByteArrayBuffer(final String value, final String encoding)
    '''
def array():
    '''public byte[] array()
    '''
def capacity():
    '''public int capacity()
    '''
def compact():
    '''public void compact()
    '''
def equals():
    '''public boolean equals(final Object obj)
    public boolean equals(final Object obj)
    '''
def equalsIgnoreCase():
    '''public boolean equalsIgnoreCase(final Buffer b)
    '''
def get():
    '''public byte get()
    '''
def hashCode():
    '''public int hashCode()
    '''
def peek():
    '''public byte peek(final int index)
    public int peek(final int index, final byte[] b, final int offset, final int length)
    '''
def poke():
    '''public void poke(final int index, final byte b)
    public int poke(int index, final Buffer src)
    public int poke(final int index, final byte[] b, final int offset, int length)
    '''
def writeTo():
    '''public void writeTo(final OutputStream out)
    '''
def readFrom():
    '''public int readFrom(final InputStream in, int max)
    '''
def space():
    '''public int space()
    '''
def CaseInsensitive():
    '''public CaseInsensitive(final String s)
    public CaseInsensitive(final byte[] b, final int o, final int l, final int rw)
    '''
