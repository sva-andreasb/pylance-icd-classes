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
def ():
    '''returns Config\n\n
    ()\n
    (final PoolableObjectFactory factory)\n
    (final PoolableObjectFactory factory, final Config config)\n
    (final PoolableObjectFactory factory, final int maxActive)\n
    (final PoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait)\n
    (final PoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait, final boolean testOnBorrow, final boolean testOnReturn)\n
    (final PoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait, final int maxIdle)\n
    (final PoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait, final int maxIdle, final boolean testOnBorrow, final boolean testOnReturn)\n
    (final PoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait, final int maxIdle, final boolean testOnBorrow, final boolean testOnReturn, final long timeBetweenEvictionRunsMillis, final int numTestsPerEvictionRun, final long minEvictableIdleTimeMillis, final boolean testWhileIdle)\n
    (final PoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait, final int maxIdle, final int minIdle, final boolean testOnBorrow, final boolean testOnReturn, final long timeBetweenEvictionRunsMillis, final int numTestsPerEvictionRun, final long minEvictableIdleTimeMillis, final boolean testWhileIdle)\n
    (final PoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait, final int maxIdle, final int minIdle, final boolean testOnBorrow, final boolean testOnReturn, final long timeBetweenEvictionRunsMillis, final int numTestsPerEvictionRun, final long minEvictableIdleTimeMillis, final boolean testWhileIdle, final long softMinEvictableIdleTimeMillis)\n
    (final PoolableObjectFactory factory, final int maxActive, final byte whenExhaustedAction, final long maxWait, final int maxIdle, final int minIdle, final boolean testOnBorrow, final boolean testOnReturn, final long timeBetweenEvictionRunsMillis, final int numTestsPerEvictionRun, final long minEvictableIdleTimeMillis, final boolean testWhileIdle, final long softMinEvictableIdleTimeMillis, final boolean lifo)\n
    ()\n
    '''
def getTestOnBorrow():
    '''returns boolean\n\n
    getTestOnBorrow()\n
    '''
def setTestOnBorrow():
    '''returns None\n\n
    setTestOnBorrow(final boolean testOnBorrow)\n
    '''
def getTestOnReturn():
    '''returns boolean\n\n
    getTestOnReturn()\n
    '''
def setTestOnReturn():
    '''returns None\n\n
    setTestOnReturn(final boolean testOnReturn)\n
    '''
def borrowObject():
    '''returns Object\n\n
    borrowObject()\n
    '''
def invalidateObject():
    '''returns None\n\n
    invalidateObject(final Object obj)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def returnObject():
    '''returns None\n\n
    returnObject(final Object obj)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def setFactory():
    '''returns None\n\n
    setFactory(final PoolableObjectFactory factory)\n
    '''
def evict():
    '''returns None\n\n
    evict()\n
    '''
def addObject():
    '''returns None\n\n
    addObject()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
