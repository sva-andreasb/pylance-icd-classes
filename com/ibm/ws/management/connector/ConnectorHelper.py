def ():
    '''returns ConnectorInfo\n\n
    (final String configRoot, final String cellName, final String nodeName, final String serverName, final String uuid, final String defaultHostName, final String managedNodeName, final boolean isInternal, final String username, final String password)\n
    (final ConfigService configService, final VariableMap variableMap, final String uuid, final String defaultHostName, final String managedNodeName, final boolean isInternal, final String username, final String password)\n
    ()\n
    '''
def createConnector():
    '''returns AdminClient\n\n
    createConnector(final boolean tryAll)\n
    createConnector(final List list, final boolean tryAll)\n
    '''
def getLocalAdminProtocol():
    '''returns String\n\n
    getLocalAdminProtocol()\n
    '''
def getRemoteAdminProtocol():
    '''returns String\n\n
    getRemoteAdminProtocol()\n
    '''
def getPreferredConnector():
    '''returns String\n\n
    getPreferredConnector()\n
    '''
def getOpenConnectorPorts():
    '''returns List\n\n
    getOpenConnectorPorts(final boolean tryAll)\n
    '''
def debug():
    '''returns None\n\n
    debug()\n
    '''
