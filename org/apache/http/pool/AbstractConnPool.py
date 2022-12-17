def ():
    '''returns AbstractConnPool\n\n
    (final ConnFactory<T, C> connFactory, final int defaultMaxPerRoute, final int maxTotal)\n
    '''
def isShutdown():
    '''returns boolean\n\n
    isShutdown()\n
    '''
def shutdown():
    '''returns None\n\n
    shutdown()\n
    '''
def lease():
    '''returns Future<E>\n\n
    lease(final T route, final Object state, final FutureCallback<E> callback)\n
    lease(final T route, final Object state)\n
    '''
def getPoolEntry():
    '''returns E\n\n
    getPoolEntry(final long timeout, final TimeUnit tunit)\n
    '''
def release():
    '''returns None\n\n
    release(final E entry, final boolean reusable)\n
    '''
def setMaxTotal():
    '''returns None\n\n
    setMaxTotal(final int max)\n
    '''
def getMaxTotal():
    '''returns int\n\n
    getMaxTotal()\n
    '''
def setDefaultMaxPerRoute():
    '''returns None\n\n
    setDefaultMaxPerRoute(final int max)\n
    '''
def getDefaultMaxPerRoute():
    '''returns int\n\n
    getDefaultMaxPerRoute()\n
    '''
def setMaxPerRoute():
    '''returns None\n\n
    setMaxPerRoute(final T route, final int max)\n
    '''
def getMaxPerRoute():
    '''returns int\n\n
    getMaxPerRoute(final T route)\n
    '''
def getTotalStats():
    '''returns PoolStats\n\n
    getTotalStats()\n
    '''
def getStats():
    '''returns PoolStats\n\n
    getStats(final T route)\n
    '''
def getRoutes():
    '''returns Set<T>\n\n
    getRoutes()\n
    '''
def closeIdle():
    '''returns None\n\n
    closeIdle(final long idletime, final TimeUnit tunit)\n
    '''
def process():
    '''returns None\n\n
    process(final PoolEntry<T, C> entry)\n
    process(final PoolEntry<T, C> entry)\n
    '''
def closeExpired():
    '''returns None\n\n
    closeExpired()\n
    '''
def getValidateAfterInactivity():
    '''returns int\n\n
    getValidateAfterInactivity()\n
    '''
def setValidateAfterInactivity():
    '''returns None\n\n
    setValidateAfterInactivity(final int ms)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
