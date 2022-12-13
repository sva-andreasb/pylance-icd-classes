def Cache():
'''public Cache(final int maxSize, final long maxLifetime)
'''
pass
def put():
'''public synchronized V put(final K key, final V value)
'''
pass
def get():
'''public synchronized V get(final Object key)
'''
pass
def remove():
'''public synchronized V remove(final Object key)
public synchronized V remove(final Object key, final boolean internal)
public void remove()
public void remove()
public void remove()
'''
pass
def clear():
'''public synchronized void clear()
public void clear()
'''
pass
def size():
'''public synchronized int size()
public int size()
public int size()
'''
pass
def isEmpty():
'''public synchronized boolean isEmpty()
'''
pass
def values():
'''public synchronized Collection<V> values()
'''
pass
def iterator():
'''public Iterator<V> iterator()
public Iterator<Entry<K, V>> iterator()
'''
pass
def hasNext():
'''public boolean hasNext()
public boolean hasNext()
'''
pass
def next():
'''public V next()
public Entry<K, V> next()
'''
pass
def containsKey():
'''public synchronized boolean containsKey(final Object key)
'''
pass
def putAll():
'''public void putAll(final Map<? extends K, ? extends V> map)
'''
pass
def containsValue():
'''public synchronized boolean containsValue(final Object value)
'''
pass
def entrySet():
'''public synchronized Set<Entry<K, V>> entrySet()
'''
pass
def setValue():
'''public V setValue(final V value)
'''
pass
def keySet():
'''public synchronized Set<K> keySet()
'''
pass
def getCacheHits():
'''public long getCacheHits()
'''
pass
def getCacheMisses():
'''public long getCacheMisses()
'''
pass
def getMaxCacheSize():
'''public int getMaxCacheSize()
'''
pass
def setMaxCacheSize():
'''public synchronized void setMaxCacheSize(final int maxCacheSize)
'''
pass
def getMaxLifetime():
'''public long getMaxLifetime()
'''
pass
def setMaxLifetime():
'''public void setMaxLifetime(final long maxLifetime)
'''
pass
def CacheObject():
'''public CacheObject(final V object)
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def LinkedList():
'''public LinkedList()
'''
pass
def getFirst():
'''public LinkedListNode getFirst()
'''
pass
def getLast():
'''public LinkedListNode getLast()
'''
pass
def addFirst():
'''public LinkedListNode addFirst(final LinkedListNode node)
public LinkedListNode addFirst(final Object object)
'''
pass
def addLast():
'''public LinkedListNode addLast(final Object object)
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def LinkedListNode():
'''public LinkedListNode(final Object object, final LinkedListNode next, final LinkedListNode previous)
'''
pass
