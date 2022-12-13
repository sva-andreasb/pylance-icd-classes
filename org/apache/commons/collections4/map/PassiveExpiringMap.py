def PassiveExpiringMap():
    '''public PassiveExpiringMap()
    public PassiveExpiringMap(final ExpirationPolicy<K, V> expiringPolicy)
    public PassiveExpiringMap(final ExpirationPolicy<K, V> expiringPolicy, final Map<K, V> map)
    public PassiveExpiringMap(final long timeToLiveMillis)
    public PassiveExpiringMap(final long timeToLiveMillis, final Map<K, V> map)
    public PassiveExpiringMap(final long timeToLive, final TimeUnit timeUnit)
    public PassiveExpiringMap(final long timeToLive, final TimeUnit timeUnit, final Map<K, V> map)
    public PassiveExpiringMap(final Map<K, V> map)
    '''
def clear():
    '''public void clear()
    '''
def containsKey():
    '''public boolean containsKey(final Object key)
    '''
def containsValue():
    '''public boolean containsValue(final Object value)
    '''
def get():
    '''public V get(final Object key)
    '''
def isEmpty():
    '''public boolean isEmpty()
    '''
def keySet():
    '''public Set<K> keySet()
    '''
def put():
    '''public V put(final K key, final V value)
    '''
def putAll():
    '''public void putAll(final Map<? extends K, ? extends V> mapToCopy)
    '''
def remove():
    '''public V remove(final Object key)
    '''
def size():
    '''public int size()
    '''
def values():
    '''public Collection<V> values()
    '''
def ConstantTimeToLiveExpirationPolicy():
    '''public ConstantTimeToLiveExpirationPolicy()
    public ConstantTimeToLiveExpirationPolicy(final long timeToLiveMillis)
    public ConstantTimeToLiveExpirationPolicy(final long timeToLive, final TimeUnit timeUnit)
    '''
def expirationTime():
    '''public long expirationTime(final K key, final V value)
    '''
