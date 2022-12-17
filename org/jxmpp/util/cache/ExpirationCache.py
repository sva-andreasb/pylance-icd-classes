def ():
    '''returns ExpirationCache\n\n
    (final int maxSize, final long defaultExpirationTime)\n
    '''
def setDefaultExpirationTime():
    '''returns None\n\n
    setDefaultExpirationTime(final long defaultExpirationTime)\n
    '''
def put():
    '''returns V\n\n
    put(final K key, final V value)\n
    put(final K key, final V value, final long expirationTime)\n
    '''
def lookup():
    '''returns V\n\n
    lookup(final K key)\n
    '''
def get():
    '''returns V\n\n
    get(final Object key)\n
    '''
def remove():
    '''returns V\n\n
    remove(final Object key)\n
    '''
def getMaxCacheSize():
    '''returns int\n\n
    getMaxCacheSize()\n
    '''
def setMaxCacheSize():
    '''returns None\n\n
    setMaxCacheSize(final int maxCacheSize)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def containsKey():
    '''returns boolean\n\n
    containsKey(final Object key)\n
    '''
def containsValue():
    '''returns boolean\n\n
    containsValue(final Object value)\n
    '''
def putAll():
    '''returns None\n\n
    putAll(final Map<? extends K, ? extends V> m)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def keySet():
    '''returns Set<K>\n\n
    keySet()\n
    '''
def values():
    '''returns Collection<V>\n\n
    values()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def getKey():
    '''returns K\n\n
    getKey()\n
    '''
def getValue():
    '''returns V\n\n
    getValue()\n
    '''
def setValue():
    '''returns V\n\n
    setValue(final V value)\n
    '''
