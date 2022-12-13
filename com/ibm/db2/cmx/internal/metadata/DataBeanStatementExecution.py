SQLHASH = "int  0"
MONITORID = "int  1"
STATIC = "int  2"
KEYLESS = "int  3"
STAT_PKG = "String  \"SYSSTAT\""
METADATA_PACKAGE = "int  0"
METADATA_CONTOKEN = "int  1"
METADATA_SECTION = "int  2"
def DataBeanStatementExecution():
    '''    public DataBeanStatementExecution(final MonitorAgent monitorAgent, final int maxBytesUsedforHash_)
    public DataBeanStatementExecution(final DataBeanStatementExecution dataBeanStatementExecution)
    '''
def setDriverData():
    '''    public void setDriverData(final Object[] a)
    '''
def getServerKeyType():
    '''    public int getServerKeyType()
    '''
def getServerKey():
    '''    public String getServerKey()
    '''
def statementTimerStarted():
    '''    public boolean statementTimerStarted()
    '''
def toJSON_DSM():
    '''    public JSONArray toJSON_DSM()
    '''
def toJSONv1():
    '''    public JSONArray toJSONv1()
    '''
def toJSONv2():
    '''    public JSONArray toJSONv2()
    '''
def toJSONv3():
    '''    public JSONArray toJSONv3()
    '''
def toJSONv7():
    '''    public JSONArray toJSONv7()
    '''
def toJSON():
    '''    public JSONArray toJSON(final int n)
    '''
def getKey():
    '''    public String getKey(final int n)
    '''
def getMetadataCorrelatorString():
    '''    public static String getMetadataCorrelatorString(final String str, final String str2, final String str3)
    '''
def setMetadataCorrelatorForLayerTransport():
    '''    public static void setMetadataCorrelatorForLayerTransport(final StatementDescriptorImpl value)
    '''
def setMetadataCorrelatorString():
    '''    public void setMetadataCorrelatorString(final String metadataCorrelator_)
    '''
def getMetadataCorrelator():
    '''    public String getMetadataCorrelator()
    '''
def prepareForAggregation():
    '''    public void prepareForAggregation()
    '''
def aggregate():
    '''    public void aggregate(final DataBeanStatementExecution dataBeanStatementExecution)
    '''
