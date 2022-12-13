def PassiveExpiringMap():
'''public PassiveExpiringMap()
public PassiveExpiringMap(final ExpirationPolicy<K, V> expiringPolicy)
public PassiveExpiringMap(final ExpirationPolicy<K, V> expiringPolicy, final Map<K, V> map)
public PassiveExpiringMap(final long timeToLiveMillis)
public PassiveExpiringMap(final long timeToLiveMillis, final Map<K, V> map)
public PassiveExpiringMap(final long timeToLive, final TimeUnit timeUnit)
public PassiveExpiringMap(final long timeToLive, final TimeUnit timeUnit, final Map<K, V> map)
public PassiveExpiringMap(final Map<K, V> map)
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
def get():
'''public V get(final Object key)
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
'''public void putAll(final Map<? extends K, ? extends V> mapToCopy)
'''
pass
def remove():
'''public V remove(final Object key)
'''
pass
def size():
'''public int size()
'''
pass
def values():
'''public Collection<V> values()
'''
pass
def ConstantTimeToLiveExpirationPolicy():
'''public ConstantTimeToLiveExpirationPolicy()
public ConstantTimeToLiveExpirationPolicy(final long timeToLiveMillis)
public ConstantTimeToLiveExpirationPolicy(final long timeToLive, final TimeUnit timeUnit)
'''
pass
def expirationTime():
'''public long expirationTime(final K key, final V value)
'''
pass
