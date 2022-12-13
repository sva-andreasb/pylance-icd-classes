def of():
    '''    public static <K, V> Relation<K, V> of(final Map<K, Set<V>> map, final Class<?> setCreator)
    public static <K, V> Relation<K, V> of(final Map<K, Set<V>> map, final Class<?> setCreator, final Comparator<V> setComparator)
    '''
def Relation():
    '''    public Relation(final Map<K, Set<V>> map, final Class<?> setCreator)
    public Relation(final Map<K, Set<V>> map, final Class<?> setCreator, final Comparator<V> setComparator)
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
def equals():
    '''    public boolean equals(final Object o)
    '''
def getAll():
    '''    public Set<V> getAll(final Object key)
    '''
def get():
    '''    public Set<V> get(final Object key)
    '''
def hashCode():
    '''    public int hashCode()
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
    '''    public V putAll(final K key, final Collection<? extends V> values)
    public V putAll(final Collection<K> keys, final V value)
    public void putAll(final Map<? extends K, ? extends V> t)
    public void putAll(final Relation<? extends K, ? extends V> t)
    '''
def removeAll():
    '''    public Set<V> removeAll(final K key)
    public boolean removeAll(final Relation<K, V> toBeRemoved)
    public final Set<V> removeAll(final K... keys)
    public boolean removeAll(final K key, final Iterable<V> toBeRemoved)
    public Set<V> removeAll(final Collection<K> toBeRemoved)
    '''
def remove():
    '''    public boolean remove(final K key, final V value)
    '''
def size():
    '''    public int size()
    '''
def values():
    '''    public Set<V> values()
    public <C extends Collection<V>> C values(final C result)
    '''
def toString():
    '''    public String toString()
    '''
def addAllInverted():
    '''    public Relation<K, V> addAllInverted(final Relation<V, K> source)
    public Relation<K, V> addAllInverted(final Map<V, K> source)
    '''
def isFrozen():
    '''    public boolean isFrozen()
    '''
def freeze():
    '''    public Relation<K, V> freeze()
    '''
def cloneAsThawed():
    '''    public Relation<K, V> cloneAsThawed()
    '''
def SimpleEntry():
    '''    public SimpleEntry(final K key, final V value)
    public SimpleEntry(final Map.Entry<K, V> e)
    '''
def getKey():
    '''    public K getKey()
    '''
def getValue():
    '''    public V getValue()
    '''
def setValue():
    '''    public V setValue(final V value)
    '''
