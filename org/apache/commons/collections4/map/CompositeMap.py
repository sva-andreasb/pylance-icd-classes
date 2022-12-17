def ():
    '''returns CompositeMap\n\n
    ()\n
    (final Map<K, V> one, final Map<K, V> two)\n
    (final Map<K, V> one, final Map<K, V> two, final MapMutator<K, V> mutator)\n
    (final Map<K, V>... composite)\n
    (final Map<K, V>[] composite, final MapMutator<K, V> mutator)\n
    '''
def setMutator():
    '''returns None\n\n
    setMutator(final MapMutator<K, V> mutator)\n
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
    putAll(final Map<? extends K, ? extends V> map)\n
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
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
