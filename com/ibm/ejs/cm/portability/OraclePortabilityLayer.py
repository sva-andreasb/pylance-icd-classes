def checkCMPStoreOperation():
    '''returns boolean\n\n
    checkCMPStoreOperation(final String beanId, final Connection c, final boolean loadedForUpdate)\n
    '''
def setTransactionIsolation():
    '''returns None\n\n
    setTransactionIsolation(final Connection connection, int isolationLevel)\n
    '''
def configurePooledConnection():
    '''returns None\n\n
    configurePooledConnection(final PooledConnection pconn, final CMPropertiesImpl props)\n
    '''
def configureXAConnection():
    '''returns None\n\n
    configureXAConnection(final XAConnection xaconn, final CMPropertiesImpl props)\n
    '''
def getPreferredIsolationLevel():
    '''returns int\n\n
    getPreferredIsolationLevel()\n
    '''
def createConnectionProxy():
    '''returns ConnectionProxy\n\n
    createConnectionProxy(final ConnectO connection)\n
    '''
