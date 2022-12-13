def multiValueMap():
    '''public static <K, V> MultiValueMap<K, V> multiValueMap(final Map<K, ? super Collection<V>> map)
    public static <K, V, C extends Collection<V>> MultiValueMap<K, V> multiValueMap(final Map<K, ? super C> map, final Class<C> collectionClass)
    public static <K, V, C extends Collection<V>> MultiValueMap<K, V> multiValueMap(final Map<K, ? super C> map, final Factory<C> collectionFactory)
    '''
def MultiValueMap():
    '''public MultiValueMap()
    '''
def clear():
    '''public void clear()
    public void clear()
    '''
def removeMapping():
    '''public boolean removeMapping(final Object key, final Object value)
    '''
def containsValue():
    '''public boolean containsValue(final Object value)
    public boolean containsValue(final Object key, final Object value)
    '''
def put():
    '''public Object put(final K key, final Object value)
    '''
def putAll():
    '''public void putAll(final Map<? extends K, ?> map)
    public boolean putAll(final K key, final Collection<V> values)
    '''
def values():
    '''public Collection<Object> values()
    '''
def getCollection():
    '''public Collection<V> getCollection(final Object key)
    '''
def size():
    '''public int size(final Object key)
    public int size()
    '''
def iterator():
    '''public Iterator<V> iterator(final Object key)
    public Iterator<V> iterator()
    '''
def getKey():
    '''public K getKey()
    '''
def getValue():
    '''public V getValue()
    '''
def setValue():
    '''public V setValue(final V value)
    '''
def totalSize():
    '''public int totalSize()
    '''
def ValuesIterator():
    '''public ValuesIterator(final Object key)
    '''
def remove():
    '''public void remove()
    '''
def hasNext():
    '''public boolean hasNext()
    '''
def next():
    '''public V next()
    '''
def ReflectionFactory():
    '''public ReflectionFactory(final Class<T> clazz)
    '''
def create():
    '''public T create()
    '''
