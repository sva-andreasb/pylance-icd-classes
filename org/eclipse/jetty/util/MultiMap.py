def MultiMap():
    '''public MultiMap()
    public MultiMap(final Map<K, Object> map)
    public MultiMap(final MultiMap<K> map)
    public MultiMap(final int capacity)
    public MultiMap(final boolean concurrent)
    '''
def getValues():
    '''public List<Object> getValues(final Object name)
    '''
def getValue():
    '''public Object getValue(final Object name, final int i)
    '''
def getString():
    '''public String getString(final Object name)
    '''
def get():
    '''public Object get(final Object name)
    '''
def put():
    '''public Object put(final K name, final Object value)
    '''
def putValues():
    '''public Object putValues(final K name, final List<?> values)
    public Object putValues(final K name, final String... values)
    '''
def add():
    '''public void add(final K name, final Object value)
    '''
def addValues():
    '''public void addValues(final K name, final List<?> values)
    public void addValues(final K name, final String[] values)
    '''
def removeValue():
    '''public boolean removeValue(final K name, final Object value)
    '''
def putAll():
    '''public void putAll(final Map<? extends K, ?> m)
    '''
def toStringArrayMap():
    '''public Map<K, String[]> toStringArrayMap()
    '''
def toString():
    '''public String toString()
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
def equals():
    '''public boolean equals(final Object o)
    '''
def hashCode():
    '''public int hashCode()
    '''
def isEmpty():
    '''public boolean isEmpty()
    '''
def keySet():
    '''public Set<K> keySet()
    '''
def remove():
    '''public Object remove(final Object key)
    public boolean remove(final Object key, final Object value)
    '''
def size():
    '''public int size()
    '''
def values():
    '''public Collection<Object> values()
    '''
def putIfAbsent():
    '''public Object putIfAbsent(final K key, final Object value)
    '''
def replace():
    '''public boolean replace(final K key, final Object oldValue, final Object newValue)
    public Object replace(final K key, final Object value)
    '''
