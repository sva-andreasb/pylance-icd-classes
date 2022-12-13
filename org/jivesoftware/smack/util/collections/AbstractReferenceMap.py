HARD = "int  0"
SOFT = "int  1"
WEAK = "int  2"
def size():
    '''    public int size()
    '''
def isEmpty():
    '''    public boolean isEmpty()
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
def put():
    '''    public V put(final K key, final V value)
    '''
def remove():
    '''    public V remove(final Object key)
    public void remove()
    '''
def clear():
    '''    public void clear()
    '''
def mapIterator():
    '''    public MapIterator<K, V> mapIterator()
    '''
def keySet():
    '''    public Set<K> keySet()
    '''
def values():
    '''    public Collection<V> values()
    '''
def createEntry():
    '''    public HashEntry<K, V> createEntry(final HashEntry<K, V> next, final int hashCode, final K key, final V value)
    '''
def toArray():
    '''    public Object[] toArray()
    public <T> T[] toArray(final T[] arr)
    public Object[] toArray()
    public <T> T[] toArray(final T[] arr)
    public Object[] toArray()
    public <T> T[] toArray(final T[] arr)
    '''
def ReferenceEntry():
    '''    public ReferenceEntry(final AbstractReferenceMap<K, V> parent, final ReferenceEntry<K, V> next, final int hashCode, final K key, final V value)
    '''
def getKey():
    '''    public K getKey()
    public K getKey()
    '''
def getValue():
    '''    public V getValue()
    public V getValue()
    '''
def setValue():
    '''    public V setValue(final V obj)
    public V setValue(final V value)
    '''
def equals():
    '''    public boolean equals(final Object obj)
    '''
def hashCode():
    '''    public int hashCode()
    public int hashCode()
    public int hashCode()
    '''
def ReferenceIteratorBase():
    '''    public ReferenceIteratorBase(final AbstractReferenceMap<K, V> parent)
    '''
def hasNext():
    '''    public boolean hasNext()
    '''
def superNext():
    '''    public ReferenceEntry<K, V> superNext()
    '''
def ReferenceEntrySetIterator():
    '''    public ReferenceEntrySetIterator(final AbstractReferenceMap<K, V> abstractReferenceMap)
    '''
def next():
    '''    public ReferenceEntry<K, V> next()
    public K next()
    public V next()
    public K next()
    '''
def SoftRef():
    '''    public SoftRef(final int hash, final T r, final ReferenceQueue q)
    '''
def WeakRef():
    '''    public WeakRef(final int hash, final T r, final ReferenceQueue q)
    '''
