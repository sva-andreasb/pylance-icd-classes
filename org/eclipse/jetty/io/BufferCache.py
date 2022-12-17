def ():
    '''returns CachedBuffer\n\n
    ()\n
    (final String value, final int ordinal)\n
    '''
def add():
    '''returns CachedBuffer\n\n
    add(final String value, final int ordinal)\n
    '''
def get():
    '''returns CachedBuffer\n\n
    get(final int ordinal)\n
    get(final Buffer buffer)\n
    get(final String value)\n
    '''
def lookup():
    '''returns Buffer\n\n
    lookup(final Buffer buffer)\n
    lookup(final String value)\n
    '''
def getBest():
    '''returns CachedBuffer\n\n
    getBest(final byte[] value, final int offset, final int maxLength)\n
    '''
def toString():
    '''returns String\n\n
    toString(final Buffer buffer)\n
    toString()\n
    '''
def getOrdinal():
    '''returns int\n\n
    getOrdinal(final String value)\n
    getOrdinal(Buffer buffer)\n
    getOrdinal()\n
    '''
def getAssociate():
    '''returns CachedBuffer\n\n
    getAssociate(final Object key)\n
    '''
def setAssociate():
    '''returns None\n\n
    setAssociate(final Object key, final CachedBuffer associate)\n
    '''
