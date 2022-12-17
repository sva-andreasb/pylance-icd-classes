def ():
    '''returns LRUMap\n\n
    ()\n
    (final int maxSize)\n
    (final int maxSize, final int initialSize)\n
    (final int maxSize, final boolean scanUntilRemovable)\n
    (final int maxSize, final float loadFactor)\n
    (final int maxSize, final int initialSize, final float loadFactor)\n
    (final int maxSize, final float loadFactor, final boolean scanUntilRemovable)\n
    (final int maxSize, final int initialSize, final float loadFactor, final boolean scanUntilRemovable)\n
    (final Map<? extends K, ? extends V> map)\n
    (final Map<? extends K, ? extends V> map, final boolean scanUntilRemovable)\n
    '''
def get():
    '''returns V\n\n
    get(final Object key)\n
    get(final Object key, final boolean updateToMRU)\n
    '''
def isFull():
    '''returns boolean\n\n
    isFull()\n
    '''
def maxSize():
    '''returns int\n\n
    maxSize()\n
    '''
def isScanUntilRemovable():
    '''returns boolean\n\n
    isScanUntilRemovable()\n
    '''
