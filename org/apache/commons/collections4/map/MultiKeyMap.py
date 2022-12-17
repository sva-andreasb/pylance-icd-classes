def ():
    '''returns MultiKeyMap\n\n
    ()\n
    '''
def get():
    '''returns V\n\n
    get(final Object key1, final Object key2)\n
    get(final Object key1, final Object key2, final Object key3)\n
    get(final Object key1, final Object key2, final Object key3, final Object key4)\n
    get(final Object key1, final Object key2, final Object key3, final Object key4, final Object key5)\n
    '''
def containsKey():
    '''returns boolean\n\n
    containsKey(final Object key1, final Object key2)\n
    containsKey(final Object key1, final Object key2, final Object key3)\n
    containsKey(final Object key1, final Object key2, final Object key3, final Object key4)\n
    containsKey(final Object key1, final Object key2, final Object key3, final Object key4, final Object key5)\n
    '''
def put():
    '''returns V\n\n
    put(final K key1, final K key2, final V value)\n
    put(final K key1, final K key2, final K key3, final V value)\n
    put(final K key1, final K key2, final K key3, final K key4, final V value)\n
    put(final K key1, final K key2, final K key3, final K key4, final K key5, final V value)\n
    put(final MultiKey<? extends K> key, final V value)\n
    '''
def removeMultiKey():
    '''returns V\n\n
    removeMultiKey(final Object key1, final Object key2)\n
    removeMultiKey(final Object key1, final Object key2, final Object key3)\n
    removeMultiKey(final Object key1, final Object key2, final Object key3, final Object key4)\n
    removeMultiKey(final Object key1, final Object key2, final Object key3, final Object key4, final Object key5)\n
    '''
def removeAll():
    '''returns boolean\n\n
    removeAll(final Object key1)\n
    removeAll(final Object key1, final Object key2)\n
    removeAll(final Object key1, final Object key2, final Object key3)\n
    removeAll(final Object key1, final Object key2, final Object key3, final Object key4)\n
    '''
def putAll():
    '''returns None\n\n
    putAll(final Map<? extends MultiKey<? extends K>, ? extends V> mapToCopy)\n
    '''
