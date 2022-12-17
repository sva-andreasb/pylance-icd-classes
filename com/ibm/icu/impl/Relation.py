def ():
    '''returns SimpleEntry\n\n
    (final Map<K, Set<V>> map, final Class<?> setCreator)\n
    (final Map<K, Set<V>> map, final Class<?> setCreator, final Comparator<V> setComparator)\n
    (final K key, final V value)\n
    (final Map.Entry<K, V> e)\n
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
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def getAll():
    '''returns Set<V>\n\n
    getAll(final Object key)\n
    '''
def get():
    '''returns Set<V>\n\n
    get(final Object key)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
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
    putAll(final K key, final Collection<? extends V> values)\n
    putAll(final Collection<K> keys, final V value)\n
    putAll(final Map<? extends K, ? extends V> t)\n
    putAll(final Relation<? extends K, ? extends V> t)\n
    '''
def removeAll():
    '''returns Set<V>\n\n
    removeAll(final K key)\n
    removeAll(final Relation<K, V> toBeRemoved)\n
    removeAll(final K key, final Iterable<V> toBeRemoved)\n
    removeAll(final Collection<K> toBeRemoved)\n
    '''
def remove():
    '''returns boolean\n\n
    remove(final K key, final V value)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def values():
    '''returns Set<V>\n\n
    values()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def isFrozen():
    '''returns boolean\n\n
    isFrozen()\n
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
