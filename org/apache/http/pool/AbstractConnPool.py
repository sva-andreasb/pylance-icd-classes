def AbstractConnPool():
    '''public AbstractConnPool(final ConnFactory<T, C> connFactory, final int defaultMaxPerRoute, final int maxTotal)
    '''
def isShutdown():
    '''public boolean isShutdown()
    '''
def shutdown():
    '''public void shutdown()
    '''
def lease():
    '''public Future<E> lease(final T route, final Object state, final FutureCallback<E> callback)
    public Future<E> lease(final T route, final Object state)
    '''
def getPoolEntry():
    '''public E getPoolEntry(final long timeout, final TimeUnit tunit)
    '''
def release():
    '''public void release(final E entry, final boolean reusable)
    '''
def setMaxTotal():
    '''public void setMaxTotal(final int max)
    '''
def getMaxTotal():
    '''public int getMaxTotal()
    '''
def setDefaultMaxPerRoute():
    '''public void setDefaultMaxPerRoute(final int max)
    '''
def getDefaultMaxPerRoute():
    '''public int getDefaultMaxPerRoute()
    '''
def setMaxPerRoute():
    '''public void setMaxPerRoute(final T route, final int max)
    '''
def getMaxPerRoute():
    '''public int getMaxPerRoute(final T route)
    '''
def getTotalStats():
    '''public PoolStats getTotalStats()
    '''
def getStats():
    '''public PoolStats getStats(final T route)
    '''
def getRoutes():
    '''public Set<T> getRoutes()
    '''
def closeIdle():
    '''public void closeIdle(final long idletime, final TimeUnit tunit)
    '''
def process():
    '''public void process(final PoolEntry<T, C> entry)
    public void process(final PoolEntry<T, C> entry)
    '''
def closeExpired():
    '''public void closeExpired()
    '''
def getValidateAfterInactivity():
    '''public int getValidateAfterInactivity()
    '''
def setValidateAfterInactivity():
    '''public void setValidateAfterInactivity(final int ms)
    '''
def toString():
    '''public String toString()
    '''
