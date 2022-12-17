def ():
    '''returns HttpControllerAgentImpl\n\n
    (final String s, final String s2)\n
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
def deregisterMonitorDataSource():
    '''returns None\n\n
    deregisterMonitorDataSource(final String s, final String s2, final int n, final String s3, final String s4, final int n2)\n
    '''
def registerMonitorDataSource():
    '''returns None\n\n
    registerMonitorDataSource(final String s, final String s2, final String[] array, final int n, final String s3, final String[] array2, final int i, final int n2, final int j, final int k, final boolean b, final int[] array3, final String[] array4, final String s4, final int n3, final int n4)\n
    '''
def run():
    '''returns Object\n\n
    run()\n
    '''
def registerDriverOverNetwork():
    '''returns None\n\n
    registerDriverOverNetwork(final Map<String, Object> map, final String str, final String str2, final long n)\n
    '''
def sendDeregisterDriver():
    '''returns None\n\n
    sendDeregisterDriver(final String str)\n
    '''
def sendDeregisterDataSource():
    '''returns None\n\n
    sendDeregisterDataSource(final String str)\n
    '''
def sendClearServerCache():
    '''returns boolean\n\n
    sendClearServerCache()\n
    '''
def sendAndReceiveChainedMessages():
    '''returns None\n\n
    sendAndReceiveChainedMessages(final ArrayList<ControlDriver.RequestInfo> list)\n
    '''
def logLookup():
    '''returns None\n\n
    logLookup(final String str, final String str2, final String str3, final String str4, final String str5, final String str6, final String[] array, final String[] array2, final String[] array3, final String[] array4, final String[] array5)\n
    '''
def logStatistics():
    '''returns None\n\n
    logStatistics(final String str, final String str2, final String str3, final String str4, final String[] a, final String[] array, final String[] array2, final Set<ClientInfo>[] array3, final HashMap<String, TransportPoolStatistics> hashMap, final long[][] array4, final Long[] array5, final Object[][] array6, final String[] array7, final String[] array8, final String[] array9, final String[] array10, final long[][] array11)\n
    '''
def logPushDownErrors():
    '''returns None\n\n
    logPushDownErrors(final String str, final String str2, final String str3, final MonitorInterface.ClientRuntime clientRuntime, final ArrayList<PushDownError> list)\n
    '''
def logApplicationException():
    '''returns None\n\n
    logApplicationException(final String str, final String str2, final String str3, final MonitorInterface.ClientRuntime clientRuntime, final SQLException ex)\n
    '''
def logPushDownApplication():
    '''returns None\n\n
    logPushDownApplication(final String str, final String str2, final Map<String, Object> map, final String str3, final String str4, final String str5, final String str6, final String[] a, final Map<String, Object>[] array, final String[] array2, final String[] array3, final String[] array4, final String[] array5, final HashMap<String, String>[] array6)\n
    '''
def getNegotiatedVersion():
    '''returns int\n\n
    getNegotiatedVersion()\n
    '''
def sendHttpEIPayloadWithReceive():
    '''returns None\n\n
    sendHttpEIPayloadWithReceive(final Message message)\n
    '''
