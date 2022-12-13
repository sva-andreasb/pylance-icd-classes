HARD = "int  0"
SOFT = "int  1"
WEAK = "int  2"
def size():
'''public int size()
'''
pass
def isEmpty():
'''public boolean isEmpty()
'''
pass
def containsKey():
'''public boolean containsKey(final Object key)
'''
pass
def containsValue():
'''public boolean containsValue(final Object value)
'''
pass
def get():
'''public V get(final Object key)
'''
pass
def put():
'''public V put(final K key, final V value)
'''
pass
def remove():
'''public V remove(final Object key)
public void remove()
'''
pass
def clear():
'''public void clear()
'''
pass
def mapIterator():
'''public MapIterator<K, V> mapIterator()
'''
pass
def keySet():
'''public Set<K> keySet()
'''
pass
def values():
'''public Collection<V> values()
'''
pass
def createEntry():
'''public HashEntry<K, V> createEntry(final HashEntry<K, V> next, final int hashCode, final K key, final V value)
'''
pass
def toArray():
'''public Object[] toArray()
public <T> T[] toArray(final T[] arr)
public Object[] toArray()
public <T> T[] toArray(final T[] arr)
public Object[] toArray()
public <T> T[] toArray(final T[] arr)
'''
pass
def ReferenceEntry():
'''public ReferenceEntry(final AbstractReferenceMap<K, V> parent, final ReferenceEntry<K, V> next, final int hashCode, final K key, final V value)
'''
pass
def getKey():
'''public K getKey()
public K getKey()
'''
pass
def getValue():
'''public V getValue()
public V getValue()
'''
pass
def setValue():
'''public V setValue(final V obj)
public V setValue(final V value)
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
def hashCode():
'''public int hashCode()
public int hashCode()
public int hashCode()
'''
pass
def ReferenceIteratorBase():
'''public ReferenceIteratorBase(final AbstractReferenceMap<K, V> parent)
'''
pass
def hasNext():
'''public boolean hasNext()
'''
pass
def superNext():
'''public ReferenceEntry<K, V> superNext()
'''
pass
def ReferenceEntrySetIterator():
'''public ReferenceEntrySetIterator(final AbstractReferenceMap<K, V> abstractReferenceMap)
'''
pass
def next():
'''public ReferenceEntry<K, V> next()
public K next()
public V next()
public K next()
'''
pass
def SoftRef():
'''public SoftRef(final int hash, final T r, final ReferenceQueue q)
'''
pass
def WeakRef():
'''public WeakRef(final int hash, final T r, final ReferenceQueue q)
'''
pass
