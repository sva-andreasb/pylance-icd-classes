def LRUMap():
    '''    public LRUMap()
    public LRUMap(final int maxSize)
    public LRUMap(final int maxSize, final int initialSize)
    public LRUMap(final int maxSize, final boolean scanUntilRemovable)
    public LRUMap(final int maxSize, final float loadFactor)
    public LRUMap(final int maxSize, final int initialSize, final float loadFactor)
    public LRUMap(final int maxSize, final float loadFactor, final boolean scanUntilRemovable)
    public LRUMap(final int maxSize, final int initialSize, final float loadFactor, final boolean scanUntilRemovable)
    public LRUMap(final Map<? extends K, ? extends V> map)
    public LRUMap(final Map<? extends K, ? extends V> map, final boolean scanUntilRemovable)
    '''
def get():
    '''    public V get(final Object key)
    public V get(final Object key, final boolean updateToMRU)
    '''
def isFull():
    '''    public boolean isFull()
    '''
def maxSize():
    '''    public int maxSize()
    '''
def isScanUntilRemovable():
    '''    public boolean isScanUntilRemovable()
    '''
def clone():
    '''    public LRUMap<K, V> clone()
    '''
