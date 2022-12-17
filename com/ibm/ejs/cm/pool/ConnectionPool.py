def ():
    '''returns ConnectionPool\n\n
    (final ConnectionFactory connectionFactory, final CMProperties attrs, final String password)\n
    (final ConnectionFactory connectionFactory, final CMProperties attributes, final String xaResourceFactoryName, final XAResourceInfo xaResourceInfo, final String password)\n
    '''
def freeConnection():
    '''returns None\n\n
    freeConnection(final ConnectO c)\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def getPortabilityLayer():
    '''returns PortabilityLayerExt\n\n
    getPortabilityLayer()\n
    '''
def getAttributes():
    '''returns CMProperties\n\n
    getAttributes()\n
    '''
def isWrapperFor():
    '''returns boolean\n\n
    isWrapperFor(final Class<?> iface)\n
    '''
def getConnection():
    '''returns Connection\n\n
    getConnection()\n
    getConnection(final String username, final String password)\n
    '''
def getLoginTimeout():
    '''returns int\n\n
    getLoginTimeout()\n
    '''
def getLogWriter():
    '''returns PrintWriter\n\n
    getLogWriter()\n
    '''
def setLogWriter():
    '''returns None\n\n
    setLogWriter(final PrintWriter out)\n
    '''
def connectionEnlisted():
    '''returns None\n\n
    connectionEnlisted(final ConnectO c, final Object coord)\n
    '''
def connectionDestroyed():
    '''returns None\n\n
    connectionDestroyed(final ConnectO c)\n
    '''
def connectionIdleTimeout():
    '''returns boolean\n\n
    connectionIdleTimeout(final ConnectO c)\n
    '''
def connectionAgedTimeout():
    '''returns boolean\n\n
    connectionAgedTimeout(final ConnectO c)\n
    '''
def commonDestroyForIdleAndAged():
    '''returns None\n\n
    commonDestroyForIdleAndAged(final ConnectO c)\n
    '''
def connectionTxComplete():
    '''returns None\n\n
    connectionTxComplete(final ConnectO c, final int status, final Object coord)\n
    '''
def connectionOrphaned():
    '''returns None\n\n
    connectionOrphaned(final ConnectO c)\n
    '''
def setDestroyed():
    '''returns None\n\n
    setDestroyed(final ConnectO c)\n
    '''
def getErrorMap():
    '''returns ErrorMap\n\n
    getErrorMap()\n
    '''
