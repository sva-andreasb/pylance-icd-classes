def BOMInputStream():
    '''public BOMInputStream(final InputStream delegate)
    public BOMInputStream(final InputStream delegate, final boolean include)
    public BOMInputStream(final InputStream delegate, final ByteOrderMark... boms)
    public BOMInputStream(final InputStream delegate, final boolean include, final ByteOrderMark... boms)
    '''
def hasBOM():
    '''public boolean hasBOM()
    public boolean hasBOM(final ByteOrderMark bom)
    '''
def getBOM():
    '''public ByteOrderMark getBOM()
    '''
def getBOMCharsetName():
    '''public String getBOMCharsetName()
    '''
def read():
    '''public int read()
    public int read(final byte[] buf, int off, int len)
    public int read(final byte[] buf)
    '''
def mark():
    '''public synchronized void mark(final int readlimit)
    '''
def reset():
    '''public synchronized void reset()
    '''
def skip():
    '''public long skip(final long n)
    '''
def compare():
    '''public int compare(final ByteOrderMark bom1, final ByteOrderMark bom2)
    '''
