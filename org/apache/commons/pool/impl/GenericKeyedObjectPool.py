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
    '''    public GenericKeyedObjectPool()
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
def getMaxActive():
    '''    public synchronized int getMaxActive()
    '''
def setMaxActive():
    '''    public synchronized void setMaxActive(final int maxActive)
    '''
def getMaxTotal():
    '''    public synchronized int getMaxTotal()
    '''
def setMaxTotal():
    '''    public synchronized void setMaxTotal(final int maxTotal)
    '''
def getWhenExhaustedAction():
    '''    public synchronized byte getWhenExhaustedAction()
    '''
def setWhenExhaustedAction():
    '''    public synchronized void setWhenExhaustedAction(final byte whenExhaustedAction)
    '''
def getMaxWait():
    '''    public synchronized long getMaxWait()
    '''
def setMaxWait():
    '''    public synchronized void setMaxWait(final long maxWait)
    '''
def getMaxIdle():
    '''    public synchronized int getMaxIdle()
    '''
def setMaxIdle():
    '''    public synchronized void setMaxIdle(final int maxIdle)
    '''
def setMinIdle():
    '''    public synchronized void setMinIdle(final int poolSize)
    '''
def getMinIdle():
    '''    public synchronized int getMinIdle()
    '''
def getTestOnBorrow():
    '''    public boolean getTestOnBorrow()
    '''
def setTestOnBorrow():
    '''    public void setTestOnBorrow(final boolean testOnBorrow)
    '''
def getTestOnReturn():
    '''    public boolean getTestOnReturn()
    '''
def setTestOnReturn():
    '''    public void setTestOnReturn(final boolean testOnReturn)
    '''
def getTimeBetweenEvictionRunsMillis():
    '''    public synchronized long getTimeBetweenEvictionRunsMillis()
    '''
def setTimeBetweenEvictionRunsMillis():
    '''    public synchronized void setTimeBetweenEvictionRunsMillis(final long timeBetweenEvictionRunsMillis)
    '''
def getNumTestsPerEvictionRun():
    '''    public synchronized int getNumTestsPerEvictionRun()
    '''
def setNumTestsPerEvictionRun():
    '''    public synchronized void setNumTestsPerEvictionRun(final int numTestsPerEvictionRun)
    '''
def getMinEvictableIdleTimeMillis():
    '''    public synchronized long getMinEvictableIdleTimeMillis()
    '''
def setMinEvictableIdleTimeMillis():
    '''    public synchronized void setMinEvictableIdleTimeMillis(final long minEvictableIdleTimeMillis)
    '''
def getTestWhileIdle():
    '''    public synchronized boolean getTestWhileIdle()
    '''
def setTestWhileIdle():
    '''    public synchronized void setTestWhileIdle(final boolean testWhileIdle)
    '''
def setConfig():
    '''    public synchronized void setConfig(final Config conf)
    '''
def getLifo():
    '''    public synchronized boolean getLifo()
    '''
def setLifo():
    '''    public synchronized void setLifo(final boolean lifo)
    '''
def borrowObject():
    '''    public Object borrowObject(final Object key)
    '''
def clear():
    '''    public void clear()
    public void clear(final Object key)
    '''
def clearOldest():
    '''    public void clearOldest()
    '''
def getNumActive():
    '''    public synchronized int getNumActive()
    public synchronized int getNumActive(final Object key)
    '''
def getNumIdle():
    '''    public synchronized int getNumIdle()
    public synchronized int getNumIdle(final Object key)
    '''
def returnObject():
    '''    public void returnObject(final Object key, final Object obj)
    '''
def invalidateObject():
    '''    public void invalidateObject(final Object key, final Object obj)
    '''
def addObject():
    '''    public void addObject(final Object key)
    '''
def preparePool():
    '''    public synchronized void preparePool(final Object key, final boolean populateImmediately)
    '''
def close():
    '''    public void close()
    '''
def setFactory():
    '''    public void setFactory(final KeyedPoolableObjectFactory factory)
    '''
def evict():
    '''    public void evict()
    '''
def toString():
    '''    public String toString()
    '''
def compareTo():
    '''    public int compareTo(final Object obj)
    public int compareTo(final ObjectTimestampPair other)
    '''
def run():
    '''    public void run()
    '''
def Config():
    '''    public Config()
    '''
