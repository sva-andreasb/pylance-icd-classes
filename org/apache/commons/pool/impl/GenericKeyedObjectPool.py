WHEN_EXHAUSTED_FAIL = "byte  0"
WHEN_EXHAUSTED_BLOCK = "byte  1"
WHEN_EXHAUSTED_GROW = "byte  2"
DEFAULT_MAX_IDLE = "int  8"
DEFAULT_MAX_ACTIVE = "int  8"
DEFAULT_MAX_TOTAL = "int  -1"
DEFAULT_WHEN_EXHAUSTED_ACTION = "byte  1"
DEFAULT_MAX_WAIT = "long  -1L"
DEFAULT_TEST_ON_BORROW = "boolean  false"
DEFAULT_TEST_ON_RETURN = "boolean  false"
DEFAULT_TEST_WHILE_IDLE = "boolean  false"
DEFAULT_TIME_BETWEEN_EVICTION_RUNS_MILLIS = "long  -1L"
DEFAULT_NUM_TESTS_PER_EVICTION_RUN = "int  3"
DEFAULT_MIN_EVICTABLE_IDLE_TIME_MILLIS = "long  1800000L"
DEFAULT_MIN_IDLE = "int  0"
DEFAULT_LIFO = "boolean  true"
def GenericKeyedObjectPool():
'''public GenericKeyedObjectPool()
public GenericKeyedObjectPool(final KeyedPoolableObjectFactory factory)
public GenericKeyedObjectPool(final KeyedPoolableObjectFactory factory, final Config config)
public GenericKeyedObjectPool(final KeyedPoolableObjectFactory factory, final int maxActive)
public GenericKeyedObjectPool(final KeyedPoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait)
public GenericKeyedObjectPool(final KeyedPoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait, final boolean testOnBorrow, final boolean testOnReturn)
public GenericKeyedObjectPool(final KeyedPoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait, final int maxIdle)
public GenericKeyedObjectPool(final KeyedPoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait, final int maxIdle, final boolean testOnBorrow, final boolean testOnReturn)
public GenericKeyedObjectPool(final KeyedPoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait, final int maxIdle, final boolean testOnBorrow, final boolean testOnReturn, final long timeBetweenEvictionRunsMillis, final int numTestsPerEvictionRun, final long minEvictableIdleTimeMillis, final boolean testWhileIdle)
public GenericKeyedObjectPool(final KeyedPoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait, final int maxIdle, final int maxTotal, final boolean testOnBorrow, final boolean testOnReturn, final long timeBetweenEvictionRunsMillis, final int numTestsPerEvictionRun, final long minEvictableIdleTimeMillis, final boolean testWhileIdle)
public GenericKeyedObjectPool(final KeyedPoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait, final int maxIdle, final int maxTotal, final int minIdle, final boolean testOnBorrow, final boolean testOnReturn, final long timeBetweenEvictionRunsMillis, final int numTestsPerEvictionRun, final long minEvictableIdleTimeMillis, final boolean testWhileIdle)
public GenericKeyedObjectPool(final KeyedPoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait, final int maxIdle, final int maxTotal, final int minIdle, final boolean testOnBorrow, final boolean testOnReturn, final long timeBetweenEvictionRunsMillis, final int numTestsPerEvictionRun, final long minEvictableIdleTimeMillis, final boolean testWhileIdle, final boolean lifo)
'''
pass
def getMaxActive():
'''public synchronized int getMaxActive()
'''
pass
def setMaxActive():
'''public synchronized void setMaxActive(final int maxActive)
'''
pass
def getMaxTotal():
'''public synchronized int getMaxTotal()
'''
pass
def setMaxTotal():
'''public synchronized void setMaxTotal(final int maxTotal)
'''
pass
def getWhenExhaustedAction():
'''public synchronized byte getWhenExhaustedAction()
'''
pass
def setWhenExhaustedAction():
'''public synchronized void setWhenExhaustedAction(final byte whenExhaustedAction)
'''
pass
def getMaxWait():
'''public synchronized long getMaxWait()
'''
pass
def setMaxWait():
'''public synchronized void setMaxWait(final long maxWait)
'''
pass
def getMaxIdle():
'''public synchronized int getMaxIdle()
'''
pass
def setMaxIdle():
'''public synchronized void setMaxIdle(final int maxIdle)
'''
pass
def setMinIdle():
'''public synchronized void setMinIdle(final int poolSize)
'''
pass
def getMinIdle():
'''public synchronized int getMinIdle()
'''
pass
def getTestOnBorrow():
'''public boolean getTestOnBorrow()
'''
pass
def setTestOnBorrow():
'''public void setTestOnBorrow(final boolean testOnBorrow)
'''
pass
def getTestOnReturn():
'''public boolean getTestOnReturn()
'''
pass
def setTestOnReturn():
'''public void setTestOnReturn(final boolean testOnReturn)
'''
pass
def getTimeBetweenEvictionRunsMillis():
'''public synchronized long getTimeBetweenEvictionRunsMillis()
'''
pass
def setTimeBetweenEvictionRunsMillis():
'''public synchronized void setTimeBetweenEvictionRunsMillis(final long timeBetweenEvictionRunsMillis)
'''
pass
def getNumTestsPerEvictionRun():
'''public synchronized int getNumTestsPerEvictionRun()
'''
pass
def setNumTestsPerEvictionRun():
'''public synchronized void setNumTestsPerEvictionRun(final int numTestsPerEvictionRun)
'''
pass
def getMinEvictableIdleTimeMillis():
'''public synchronized long getMinEvictableIdleTimeMillis()
'''
pass
def setMinEvictableIdleTimeMillis():
'''public synchronized void setMinEvictableIdleTimeMillis(final long minEvictableIdleTimeMillis)
'''
pass
def getTestWhileIdle():
'''public synchronized boolean getTestWhileIdle()
'''
pass
def setTestWhileIdle():
'''public synchronized void setTestWhileIdle(final boolean testWhileIdle)
'''
pass
def setConfig():
'''public synchronized void setConfig(final Config conf)
'''
pass
def getLifo():
'''public synchronized boolean getLifo()
'''
pass
def setLifo():
'''public synchronized void setLifo(final boolean lifo)
'''
pass
def borrowObject():
'''public Object borrowObject(final Object key)
'''
pass
def clear():
'''public void clear()
public void clear(final Object key)
'''
pass
def clearOldest():
'''public void clearOldest()
'''
pass
def getNumActive():
'''public synchronized int getNumActive()
public synchronized int getNumActive(final Object key)
'''
pass
def getNumIdle():
'''public synchronized int getNumIdle()
public synchronized int getNumIdle(final Object key)
'''
pass
def returnObject():
'''public void returnObject(final Object key, final Object obj)
'''
pass
def invalidateObject():
'''public void invalidateObject(final Object key, final Object obj)
'''
pass
def addObject():
'''public void addObject(final Object key)
'''
pass
def preparePool():
'''public synchronized void preparePool(final Object key, final boolean populateImmediately)
'''
pass
def close():
'''public void close()
'''
pass
def setFactory():
'''public void setFactory(final KeyedPoolableObjectFactory factory)
'''
pass
def evict():
'''public void evict()
'''
pass
def toString():
'''public String toString()
'''
pass
def compareTo():
'''public int compareTo(final Object obj)
public int compareTo(final ObjectTimestampPair other)
'''
pass
def run():
'''public void run()
'''
pass
def Config():
'''public Config()
'''
pass
