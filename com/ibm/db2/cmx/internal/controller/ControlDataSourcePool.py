def getInstance():
    '''    public static ControlDataSourcePool getInstance()
    '''
def getPool():
    '''    public Map<String, ControlDataSourceImpl> getPool()
    '''
def getPooledInstanceOrCreateCDS():
    '''    public ControlDataSourceImpl getPooledInstanceOrCreateCDS(final Service.ControllerType controllerType, final Map<String, Object> map, final int i, final String s, final String s2, final String s3, final String s4, final String s5, final ProxiedJdbcDataSource proxiedJdbcDataSource)
    '''
def removeCDSFromPool():
    '''    public void removeCDSFromPool(final int n)
    '''
def createKey():
    '''    public static String createKey(String str, String resolveToIPAddress, String str2, String s, String s2, final boolean b)
    public static String createKey(final String s, final String s2, final String s3, final String s4, final boolean b)
    public static String createKey(final String s)
    '''
def scheduleLookupTask():
    '''    public void scheduleLookupTask(final TimerTask task, final long n, final long n2)
    public void scheduleLookupTask(final TimerTask task, final long n)
    '''
