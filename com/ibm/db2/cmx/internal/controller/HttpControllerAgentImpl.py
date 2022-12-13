def HttpControllerAgentImpl():
    '''    public HttpControllerAgentImpl(final String s, final String s2)
    '''
def getInstance():
    '''    public static HttpControllerAgentImpl getInstance(final String s, final String s2, final boolean b)
    '''
def getControllerInfo():
    '''    public void getControllerInfo(final StringBuilder sb)
    '''
def lookupOverNetwork():
    '''    public synchronized void lookupOverNetwork(final ControlDataSourceImpl controlDataSourceImpl)
    '''
def isConnected():
    '''    public boolean isConnected()
    '''
def close():
    '''    public void close()
    '''
def deregisterMonitorDataSource():
    '''    public void deregisterMonitorDataSource(final String s, final String s2, final int n, final String s3, final String s4, final int n2)
    '''
def registerMonitorDataSource():
    '''    public void registerMonitorDataSource(final String s, final String s2, final String[] array, final int n, final String s3, final String[] array2, final int i, final int n2, final int j, final int k, final boolean b, final int[] array3, final String[] array4, final String s4, final int n3, final int n4)
    '''
def run():
    '''    public Object run()
    '''
def registerDriverOverNetwork():
    '''    public void registerDriverOverNetwork(final Map<String, Object> map, final String str, final String str2, final long n)
    '''
def sendDeregisterDriver():
    '''    public void sendDeregisterDriver(final String str)
    '''
def sendDeregisterDataSource():
    '''    public void sendDeregisterDataSource(final String str)
    '''
def sendClearServerCache():
    '''    public boolean sendClearServerCache()
    '''
def sendAndReceiveChainedMessages():
    '''    public void sendAndReceiveChainedMessages(final ArrayList<ControlDriver.RequestInfo> list)
    '''
def logLookup():
    '''    public void logLookup(final String str, final String str2, final String str3, final String str4, final String str5, final String str6, final String[] array, final String[] array2, final String[] array3, final String[] array4, final String[] array5)
    '''
def logStatistics():
    '''    public void logStatistics(final String str, final String str2, final String str3, final String str4, final String[] a, final String[] array, final String[] array2, final Set<ClientInfo>[] array3, final HashMap<String, TransportPoolStatistics> hashMap, final long[][] array4, final Long[] array5, final Object[][] array6, final String[] array7, final String[] array8, final String[] array9, final String[] array10, final long[][] array11)
    '''
def logPushDownErrors():
    '''    public void logPushDownErrors(final String str, final String str2, final String str3, final MonitorInterface.ClientRuntime clientRuntime, final ArrayList<PushDownError> list)
    '''
def logApplicationException():
    '''    public void logApplicationException(final String str, final String str2, final String str3, final MonitorInterface.ClientRuntime clientRuntime, final SQLException ex)
    '''
def logPushDownApplication():
    '''    public void logPushDownApplication(final String str, final String str2, final Map<String, Object> map, final String str3, final String str4, final String str5, final String str6, final String[] a, final Map<String, Object>[] array, final String[] array2, final String[] array3, final String[] array4, final String[] array5, final HashMap<String, String>[] array6)
    '''
def getNegotiatedVersion():
    '''    public int getNegotiatedVersion()
    '''
def sendHttpEIPayloadWithReceive():
    '''    public void sendHttpEIPayloadWithReceive(final Message message)
    '''
