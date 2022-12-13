def AbstractConnPool():
'''public AbstractConnPool(final ConnFactory<T, C> connFactory, final int defaultMaxPerRoute, final int maxTotal)
'''
pass
def isShutdown():
'''public boolean isShutdown()
'''
pass
def shutdown():
'''public void shutdown()
'''
pass
def lease():
'''public Future<E> lease(final T route, final Object state, final FutureCallback<E> callback)
public Future<E> lease(final T route, final Object state)
'''
pass
def getPoolEntry():
'''public E getPoolEntry(final long timeout, final TimeUnit tunit)
'''
pass
def release():
'''public void release(final E entry, final boolean reusable)
'''
pass
def setMaxTotal():
'''public void setMaxTotal(final int max)
'''
pass
def getMaxTotal():
'''public int getMaxTotal()
'''
pass
def setDefaultMaxPerRoute():
'''public void setDefaultMaxPerRoute(final int max)
'''
pass
def getDefaultMaxPerRoute():
'''public int getDefaultMaxPerRoute()
'''
pass
def setMaxPerRoute():
'''public void setMaxPerRoute(final T route, final int max)
'''
pass
def getMaxPerRoute():
'''public int getMaxPerRoute(final T route)
'''
pass
def getTotalStats():
'''public PoolStats getTotalStats()
'''
pass
def getStats():
'''public PoolStats getStats(final T route)
'''
pass
def getRoutes():
'''public Set<T> getRoutes()
'''
pass
def closeIdle():
'''public void closeIdle(final long idletime, final TimeUnit tunit)
'''
pass
def process():
'''public void process(final PoolEntry<T, C> entry)
public void process(final PoolEntry<T, C> entry)
'''
pass
def closeExpired():
'''public void closeExpired()
'''
pass
def getValidateAfterInactivity():
'''public int getValidateAfterInactivity()
'''
pass
def setValidateAfterInactivity():
'''public void setValidateAfterInactivity(final int ms)
'''
pass
def toString():
'''public String toString()
'''
pass
