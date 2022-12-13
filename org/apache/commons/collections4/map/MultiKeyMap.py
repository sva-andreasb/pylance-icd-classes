def multiKeyMap():
    '''public static <K, V> MultiKeyMap<K, V> multiKeyMap(final AbstractHashedMap<MultiKey<? extends K>, V> map)
    '''
def MultiKeyMap():
    '''public MultiKeyMap()
    '''
def get():
    '''public V get(final Object key1, final Object key2)
    public V get(final Object key1, final Object key2, final Object key3)
    public V get(final Object key1, final Object key2, final Object key3, final Object key4)
    public V get(final Object key1, final Object key2, final Object key3, final Object key4, final Object key5)
    '''
def containsKey():
    '''public boolean containsKey(final Object key1, final Object key2)
    public boolean containsKey(final Object key1, final Object key2, final Object key3)
    public boolean containsKey(final Object key1, final Object key2, final Object key3, final Object key4)
    public boolean containsKey(final Object key1, final Object key2, final Object key3, final Object key4, final Object key5)
    '''
def put():
    '''public V put(final K key1, final K key2, final V value)
    public V put(final K key1, final K key2, final K key3, final V value)
    public V put(final K key1, final K key2, final K key3, final K key4, final V value)
    public V put(final K key1, final K key2, final K key3, final K key4, final K key5, final V value)
    public V put(final MultiKey<? extends K> key, final V value)
    '''
def removeMultiKey():
    '''public V removeMultiKey(final Object key1, final Object key2)
    public V removeMultiKey(final Object key1, final Object key2, final Object key3)
    public V removeMultiKey(final Object key1, final Object key2, final Object key3, final Object key4)
    public V removeMultiKey(final Object key1, final Object key2, final Object key3, final Object key4, final Object key5)
    '''
def removeAll():
    '''public boolean removeAll(final Object key1)
    public boolean removeAll(final Object key1, final Object key2)
    public boolean removeAll(final Object key1, final Object key2, final Object key3)
    public boolean removeAll(final Object key1, final Object key2, final Object key3, final Object key4)
    '''
def clone():
    '''public MultiKeyMap<K, V> clone()
    '''
def putAll():
    '''public void putAll(final Map<? extends MultiKey<? extends K>, ? extends V> mapToCopy)
    '''
