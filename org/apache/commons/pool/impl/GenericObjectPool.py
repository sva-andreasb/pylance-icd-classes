WHEN_EXHAUSTED_FAIL = "byte  0"
WHEN_EXHAUSTED_BLOCK = "byte  1"
WHEN_EXHAUSTED_GROW = "byte  2"
DEFAULT_MAX_IDLE = "int  8"
DEFAULT_MIN_IDLE = "int  0"
DEFAULT_MAX_ACTIVE = "int  8"
DEFAULT_WHEN_EXHAUSTED_ACTION = "byte  1"
DEFAULT_LIFO = "boolean  true"
DEFAULT_MAX_WAIT = "long  -1L"
DEFAULT_TEST_ON_BORROW = "boolean  false"
DEFAULT_TEST_ON_RETURN = "boolean  false"
DEFAULT_TEST_WHILE_IDLE = "boolean  false"
DEFAULT_TIME_BETWEEN_EVICTION_RUNS_MILLIS = "long  -1L"
DEFAULT_NUM_TESTS_PER_EVICTION_RUN = "int  3"
DEFAULT_MIN_EVICTABLE_IDLE_TIME_MILLIS = "long  1800000L"
DEFAULT_SOFT_MIN_EVICTABLE_IDLE_TIME_MILLIS = "long  -1L"
def GenericObjectPool():
'''public GenericObjectPool()
public GenericObjectPool(final PoolableObjectFactory factory)
public GenericObjectPool(final PoolableObjectFactory factory, final Config config)
public GenericObjectPool(final PoolableObjectFactory factory, final int maxActive)
public GenericObjectPool(final PoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait)
public GenericObjectPool(final PoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait, final boolean testOnBorrow, final boolean testOnReturn)
public GenericObjectPool(final PoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait, final int maxIdle)
public GenericObjectPool(final PoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait, final int maxIdle, final boolean testOnBorrow, final boolean testOnReturn)
public GenericObjectPool(final PoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait, final int maxIdle, final boolean testOnBorrow, final boolean testOnReturn, final long timeBetweenEvictionRunsMillis, final int numTestsPerEvictionRun, final long minEvictableIdleTimeMillis, final boolean testWhileIdle)
public GenericObjectPool(final PoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait, final int maxIdle, final int minIdle, final boolean testOnBorrow, final boolean testOnReturn, final long timeBetweenEvictionRunsMillis, final int numTestsPerEvictionRun, final long minEvictableIdleTimeMillis, final boolean testWhileIdle)
public GenericObjectPool(final PoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait, final int maxIdle, final int minIdle, final boolean testOnBorrow, final boolean testOnReturn, final long timeBetweenEvictionRunsMillis, final int numTestsPerEvictionRun, final long minEvictableIdleTimeMillis, final boolean testWhileIdle, final long softMinEvictableIdleTimeMillis)
public GenericObjectPool(final PoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait, final int maxIdle, final int minIdle, final boolean testOnBorrow, final boolean testOnReturn, final long timeBetweenEvictionRunsMillis, final int numTestsPerEvictionRun, final long minEvictableIdleTimeMillis, final boolean testWhileIdle, final long softMinEvictableIdleTimeMillis, final boolean lifo)
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
'''public synchronized void setMinIdle(final int minIdle)
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
def getSoftMinEvictableIdleTimeMillis():
'''public synchronized long getSoftMinEvictableIdleTimeMillis()
'''
pass
def setSoftMinEvictableIdleTimeMillis():
'''public synchronized void setSoftMinEvictableIdleTimeMillis(final long softMinEvictableIdleTimeMillis)
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
def getLifo():
'''public synchronized boolean getLifo()
'''
pass
def setLifo():
'''public synchronized void setLifo(final boolean lifo)
'''
pass
def setConfig():
'''public synchronized void setConfig(final Config conf)
'''
pass
def borrowObject():
'''public Object borrowObject()
'''
pass
def invalidateObject():
'''public void invalidateObject(final Object obj)
'''
pass
def clear():
'''public void clear()
'''
pass
def getNumActive():
'''public synchronized int getNumActive()
'''
pass
def getNumIdle():
'''public synchronized int getNumIdle()
'''
pass
def returnObject():
'''public void returnObject(final Object obj)
'''
pass
def close():
'''public void close()
'''
pass
def setFactory():
'''public void setFactory(final PoolableObjectFactory factory)
'''
pass
def evict():
'''public void evict()
'''
pass
def addObject():
'''public void addObject()
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
