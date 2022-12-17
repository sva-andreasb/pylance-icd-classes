def ():
    '''returns LazyConnectionInvocationHandler\n\n
    ()\n
    (final DataSource targetDataSource)\n
    ()\n
    (final LazyConnectionDataSourceProxy lazyConnectionDataSourceProxy, final String username, final String password)\n
    '''
def setDefaultAutoCommit():
    '''returns None\n\n
    setDefaultAutoCommit(final boolean defaultAutoCommit)\n
    '''
def setDefaultTransactionIsolation():
    '''returns None\n\n
    setDefaultTransactionIsolation(final int defaultTransactionIsolation)\n
    '''
def afterPropertiesSet():
    '''returns None\n\n
    afterPropertiesSet()\n
    '''
def getConnection():
    '''returns Connection\n\n
    getConnection()\n
    getConnection(final String username, final String password)\n
    '''
def invoke():
    '''returns Object\n\n
    invoke(final Object proxy, final Method method, final Object[] args)\n
    '''
