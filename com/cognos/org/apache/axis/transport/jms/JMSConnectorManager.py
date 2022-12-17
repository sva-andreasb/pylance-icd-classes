def getVendorPool():
    '''returns ShareableObjectPool\n\n
    getVendorPool(final String vendorId)\n
    '''
def getConnector():
    '''returns JMSConnector\n\n
    getConnector(final HashMap connectorProperties, final HashMap connectionFactoryProperties, final String username, final String password, final JMSVendorAdapter vendorAdapter)\n
    '''
def addConnectorToPool():
    '''returns None\n\n
    addConnectorToPool(final JMSConnector conn)\n
    '''
def removeConnectorFromPool():
    '''returns None\n\n
    removeConnectorFromPool(final JMSConnector conn)\n
    '''
def reserve():
    '''returns None\n\n
    reserve(final JMSConnector connector)\n
    reserve(final Object obj)\n
    '''
def release():
    '''returns None\n\n
    release(final JMSConnector connector)\n
    release(final Object obj)\n
    '''
def ():
    '''returns ReferenceCountedObject\n\n
    ()\n
    (final Object obj)\n
    '''
def addObject():
    '''returns None\n\n
    addObject(final Object obj)\n
    '''
def removeObject():
    '''returns None\n\n
    removeObject(final Object obj, final long waitTime)\n
    removeObject(final Object obj)\n
    '''
