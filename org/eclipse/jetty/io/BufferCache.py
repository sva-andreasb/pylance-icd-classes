def BufferCache():
    '''public BufferCache()
    '''
def add():
    '''public CachedBuffer add(final String value, final int ordinal)
    '''
def get():
    '''public CachedBuffer get(final int ordinal)
    public CachedBuffer get(final Buffer buffer)
    public CachedBuffer get(final String value)
    '''
def lookup():
    '''public Buffer lookup(final Buffer buffer)
    public Buffer lookup(final String value)
    '''
def getBest():
    '''public CachedBuffer getBest(final byte[] value, final int offset, final int maxLength)
    '''
def toString():
    '''public String toString(final Buffer buffer)
    public String toString()
    '''
def getOrdinal():
    '''public int getOrdinal(final String value)
    public int getOrdinal(Buffer buffer)
    public int getOrdinal()
    '''
def CachedBuffer():
    '''public CachedBuffer(final String value, final int ordinal)
    '''
def getAssociate():
    '''public CachedBuffer getAssociate(final Object key)
    '''
def setAssociate():
    '''public void setAssociate(final Object key, final CachedBuffer associate)
    '''
