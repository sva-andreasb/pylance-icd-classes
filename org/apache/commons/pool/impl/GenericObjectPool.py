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
def getMaxActive():
    '''public synchronized int getMaxActive()
    '''
def setMaxActive():
    '''public synchronized void setMaxActive(final int maxActive)
    '''
def getWhenExhaustedAction():
    '''public synchronized byte getWhenExhaustedAction()
    '''
def setWhenExhaustedAction():
    '''public synchronized void setWhenExhaustedAction(final byte whenExhaustedAction)
    '''
def getMaxWait():
    '''public synchronized long getMaxWait()
    '''
def setMaxWait():
    '''public synchronized void setMaxWait(final long maxWait)
    '''
def getMaxIdle():
    '''public synchronized int getMaxIdle()
    '''
def setMaxIdle():
    '''public synchronized void setMaxIdle(final int maxIdle)
    '''
def setMinIdle():
    '''public synchronized void setMinIdle(final int minIdle)
    '''
def getMinIdle():
    '''public synchronized int getMinIdle()
    '''
def getTestOnBorrow():
    '''public boolean getTestOnBorrow()
    '''
def setTestOnBorrow():
    '''public void setTestOnBorrow(final boolean testOnBorrow)
    '''
def getTestOnReturn():
    '''public boolean getTestOnReturn()
    '''
def setTestOnReturn():
    '''public void setTestOnReturn(final boolean testOnReturn)
    '''
def getTimeBetweenEvictionRunsMillis():
    '''public synchronized long getTimeBetweenEvictionRunsMillis()
    '''
def setTimeBetweenEvictionRunsMillis():
    '''public synchronized void setTimeBetweenEvictionRunsMillis(final long timeBetweenEvictionRunsMillis)
    '''
def getNumTestsPerEvictionRun():
    '''public synchronized int getNumTestsPerEvictionRun()
    '''
def setNumTestsPerEvictionRun():
    '''public synchronized void setNumTestsPerEvictionRun(final int numTestsPerEvictionRun)
    '''
def getMinEvictableIdleTimeMillis():
    '''public synchronized long getMinEvictableIdleTimeMillis()
    '''
def setMinEvictableIdleTimeMillis():
    '''public synchronized void setMinEvictableIdleTimeMillis(final long minEvictableIdleTimeMillis)
    '''
def getSoftMinEvictableIdleTimeMillis():
    '''public synchronized long getSoftMinEvictableIdleTimeMillis()
    '''
def setSoftMinEvictableIdleTimeMillis():
    '''public synchronized void setSoftMinEvictableIdleTimeMillis(final long softMinEvictableIdleTimeMillis)
    '''
def getTestWhileIdle():
    '''public synchronized boolean getTestWhileIdle()
    '''
def setTestWhileIdle():
    '''public synchronized void setTestWhileIdle(final boolean testWhileIdle)
    '''
def getLifo():
    '''public synchronized boolean getLifo()
    '''
def setLifo():
    '''public synchronized void setLifo(final boolean lifo)
    '''
def setConfig():
    '''public synchronized void setConfig(final Config conf)
    '''
def borrowObject():
    '''public Object borrowObject()
    '''
def invalidateObject():
    '''public void invalidateObject(final Object obj)
    '''
def clear():
    '''public void clear()
    '''
def getNumActive():
    '''public synchronized int getNumActive()
    '''
def getNumIdle():
    '''public synchronized int getNumIdle()
    '''
def returnObject():
    '''public void returnObject(final Object obj)
    '''
def close():
    '''public void close()
    '''
def setFactory():
    '''public void setFactory(final PoolableObjectFactory factory)
    '''
def evict():
    '''public void evict()
    '''
def addObject():
    '''public void addObject()
    '''
def run():
    '''public void run()
    '''
def Config():
    '''public Config()
    '''
