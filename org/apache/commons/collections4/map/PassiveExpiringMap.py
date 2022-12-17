def ():
    '''returns ConstantTimeToLiveExpirationPolicy\n\n
    ()\n
    (final ExpirationPolicy<K, V> expiringPolicy)\n
    (final ExpirationPolicy<K, V> expiringPolicy, final Map<K, V> map)\n
    (final long timeToLiveMillis)\n
    (final long timeToLiveMillis, final Map<K, V> map)\n
    (final long timeToLive, final TimeUnit timeUnit)\n
    (final long timeToLive, final TimeUnit timeUnit, final Map<K, V> map)\n
    (final Map<K, V> map)\n
    ()\n
    (final long timeToLiveMillis)\n
    (final long timeToLive, final TimeUnit timeUnit)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def containsKey():
    '''returns boolean\n\n
    containsKey(final Object key)\n
    '''
def containsValue():
    '''returns boolean\n\n
    containsValue(final Object value)\n
    '''
def get():
    '''returns V\n\n
    get(final Object key)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def keySet():
    '''returns Set<K>\n\n
    keySet()\n
    '''
def put():
    '''returns V\n\n
    put(final K key, final V value)\n
    '''
def putAll():
    '''returns None\n\n
    putAll(final Map<? extends K, ? extends V> mapToCopy)\n
    '''
def remove():
    '''returns V\n\n
    remove(final Object key)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def values():
    '''returns Collection<V>\n\n
    values()\n
    '''
def expirationTime():
    '''returns long\n\n
    expirationTime(final K key, final V value)\n
    '''
