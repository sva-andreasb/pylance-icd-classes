def CompositeMap():
    '''    public CompositeMap()
    public CompositeMap(final Map<K, V> one, final Map<K, V> two)
    public CompositeMap(final Map<K, V> one, final Map<K, V> two, final MapMutator<K, V> mutator)
    public CompositeMap(final Map<K, V>... composite)
    public CompositeMap(final Map<K, V>[] composite, final MapMutator<K, V> mutator)
    '''
def setMutator():
    '''    public void setMutator(final MapMutator<K, V> mutator)
    '''
def addComposited():
    '''    public synchronized void addComposited(final Map<K, V> map)
    '''
def removeComposited():
    '''    public synchronized Map<K, V> removeComposited(final Map<K, V> map)
    '''
def clear():
    '''    public void clear()
    '''
def containsKey():
    '''    public boolean containsKey(final Object key)
    '''
def containsValue():
    '''    public boolean containsValue(final Object value)
    '''
def get():
    '''    public V get(final Object key)
    '''
def isEmpty():
    '''    public boolean isEmpty()
    '''
def keySet():
    '''    public Set<K> keySet()
    '''
def put():
    '''    public V put(final K key, final V value)
    '''
def putAll():
    '''    public void putAll(final Map<? extends K, ? extends V> map)
    '''
def remove():
    '''    public V remove(final Object key)
    '''
def size():
    '''    public int size()
    '''
def values():
    '''    public Collection<V> values()
    '''
def equals():
    '''    public boolean equals(final Object obj)
    '''
def hashCode():
    '''    public int hashCode()
    '''
