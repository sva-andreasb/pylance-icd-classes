def of():
'''public static <K, V> Relation<K, V> of(final Map<K, Set<V>> map, final Class<?> setCreator)
public static <K, V> Relation<K, V> of(final Map<K, Set<V>> map, final Class<?> setCreator, final Comparator<V> setComparator)
'''
pass
def Relation():
'''public Relation(final Map<K, Set<V>> map, final Class<?> setCreator)
public Relation(final Map<K, Set<V>> map, final Class<?> setCreator, final Comparator<V> setComparator)
'''
pass
def clear():
'''public void clear()
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
def equals():
'''public boolean equals(final Object o)
'''
pass
def getAll():
'''public Set<V> getAll(final Object key)
'''
pass
def get():
'''public Set<V> get(final Object key)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def isEmpty():
'''public boolean isEmpty()
'''
pass
def keySet():
'''public Set<K> keySet()
'''
pass
def put():
'''public V put(final K key, final V value)
'''
pass
def putAll():
'''public V putAll(final K key, final Collection<? extends V> values)
public V putAll(final Collection<K> keys, final V value)
public void putAll(final Map<? extends K, ? extends V> t)
public void putAll(final Relation<? extends K, ? extends V> t)
'''
pass
def removeAll():
'''public Set<V> removeAll(final K key)
public boolean removeAll(final Relation<K, V> toBeRemoved)
public final Set<V> removeAll(final K... keys)
public boolean removeAll(final K key, final Iterable<V> toBeRemoved)
public Set<V> removeAll(final Collection<K> toBeRemoved)
'''
pass
def remove():
'''public boolean remove(final K key, final V value)
'''
pass
def size():
'''public int size()
'''
pass
def values():
'''public Set<V> values()
public <C extends Collection<V>> C values(final C result)
'''
pass
def toString():
'''public String toString()
'''
pass
def addAllInverted():
'''public Relation<K, V> addAllInverted(final Relation<V, K> source)
public Relation<K, V> addAllInverted(final Map<V, K> source)
'''
pass
def isFrozen():
'''public boolean isFrozen()
'''
pass
def freeze():
'''public Relation<K, V> freeze()
'''
pass
def cloneAsThawed():
'''public Relation<K, V> cloneAsThawed()
'''
pass
def SimpleEntry():
'''public SimpleEntry(final K key, final V value)
public SimpleEntry(final Map.Entry<K, V> e)
'''
pass
def getKey():
'''public K getKey()
'''
pass
def getValue():
'''public V getValue()
'''
pass
def setValue():
'''public V setValue(final V value)
'''
pass
