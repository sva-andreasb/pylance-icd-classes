def ():
    '''returns NPXControllerAgentImpl\n\n
    ()\n
    '''
def writeToLogStream():
    '''returns None\n\n
    writeToLogStream(final JSONArray jsonArray, final int i, final int n)\n
    '''
def fetchConfigNPX():
    '''returns String\n\n
    fetchConfigNPX(final String s, final int i, final int j)\n
    '''
def lookupOverNetwork():
    '''returns None\n\n
    lookupOverNetwork(final ControlDataSourceImpl controlDataSourceImpl)\n
    '''
def registerDriverOverNetwork():
    '''returns None\n\n
    registerDriverOverNetwork(final Map<String, Object> map, final String s, final String s2, final long n)\n
    '''
def getControllerInfo():
    '''returns None\n\n
    getControllerInfo(final StringBuilder sb)\n
    '''
def isConnected():
    '''returns boolean\n\n
    isConnected()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def registerMonitorDataSource():
    '''returns None\n\n
    registerMonitorDataSource(final String s, final String s2, final String[] array, final int n, final String s3, final String[] array2, final int n2, final int n3, final int n4, final int n5, final boolean b, final int[] array3, final String[] array4, final String s4, final int n6, final int n7)\n
    '''
def deregisterMonitorDataSource():
    '''returns None\n\n
    deregisterMonitorDataSource(final String s, final String s2, final int n, final String s3, final String s4, final int n2)\n
    '''
def sendDeregisterDriver():
    '''returns None\n\n
    sendDeregisterDriver(final String s)\n
    '''
def sendDeregisterDataSource():
    '''returns None\n\n
    sendDeregisterDataSource(final String s)\n
    '''
def sendAndReceiveChainedMessages():
    '''returns None\n\n
    sendAndReceiveChainedMessages(final ArrayList<ControlDriver.RequestInfo> list)\n
    '''
def logLookup():
    '''returns None\n\n
    logLookup(final String s, final String s2, final String s3, final String s4, final String s5, final String s6, final String[] array, final String[] array2, final String[] array3, final String[] array4, final String[] array5)\n
    '''
def logStatistics():
    '''returns None\n\n
    logStatistics(final String s, final String s2, final String s3, final String s4, final String[] array, final String[] array2, final String[] array3, final Set<ClientInfo>[] array4, final HashMap<String, TransportPoolStatistics> hashMap, final long[][] array5, final Long[] array6, final Object[][] array7, final String[] array8, final String[] array9, final String[] array10, final String[] array11, final long[][] array12)\n
    '''
def logPushDownErrors():
    '''returns None\n\n
    logPushDownErrors(final String s, final String s2, final String s3, final MonitorInterface.ClientRuntime clientRuntime, final ArrayList<PushDownError> list)\n
    '''
def logApplicationException():
    '''returns None\n\n
    logApplicationException(final String s, final String s2, final String s3, final MonitorInterface.ClientRuntime clientRuntime, final SQLException ex)\n
    '''
def logPushDownApplication():
    '''returns None\n\n
    logPushDownApplication(final String s, final String s2, final Map<String, Object> map, final String s3, final String s4, final String s5, final String s6, final String[] array, final Map<String, Object>[] array2, final String[] array3, final String[] array4, final String[] array5, final String[] array6, final HashMap<String, String>[] array7)\n
    '''
def getNegotiatedVersion():
    '''returns int\n\n
    getNegotiatedVersion()\n
    '''
def setConnectionMap():
    '''returns None\n\n
    setConnectionMap(final Map<Integer, Connection> monconnectionMap)\n
    '''
