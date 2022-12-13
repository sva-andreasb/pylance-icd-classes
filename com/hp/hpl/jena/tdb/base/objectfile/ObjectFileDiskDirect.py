compression = "boolean  false"
def ObjectFileDiskDirect():
    '''public ObjectFileDiskDirect(final String filename)
    '''
def write():
    '''public long write(final ByteBuffer bb)
    '''
def read():
    '''public ByteBuffer read(final long loc)
    '''
def length():
    '''public long length()
    '''
def all():
    '''public Iterator<Pair<Long, ByteBuffer>> all()
    '''
def close():
    '''public void close()
    '''
def sync():
    '''public void sync()
    public void sync(final boolean force)
    '''
def dump():
    '''public void dump()
    public void dump(final DumpHandler handler)
    '''
def handle():
    '''public void handle(final long fileIdx, final String str)
    '''
def ObjectIterator():
    '''public ObjectIterator(final long start, final long finish)
    '''
def hasNext():
    '''public boolean hasNext()
    '''
def next():
    '''public Pair<Long, ByteBuffer> next()
    '''
def remove():
    '''public void remove()
    '''
