SQLHASH = "int  0"
MONITORID = "int  1"
STATIC = "int  2"
KEYLESS = "int  3"
STAT_PKG = "String  \"SYSSTAT\""
METADATA_PACKAGE = "int  0"
METADATA_CONTOKEN = "int  1"
METADATA_SECTION = "int  2"
def ():
    '''returns DataBeanStatementExecution\n\n
    (final MonitorAgent monitorAgent, final int maxBytesUsedforHash_)\n
    (final DataBeanStatementExecution dataBeanStatementExecution)\n
    '''
def setDriverData():
    '''returns None\n\n
    setDriverData(final Object[] a)\n
    '''
def getServerKeyType():
    '''returns int\n\n
    getServerKeyType()\n
    '''
def getServerKey():
    '''returns String\n\n
    getServerKey()\n
    '''
def statementTimerStarted():
    '''returns boolean\n\n
    statementTimerStarted()\n
    '''
def toJSON_DSM():
    '''returns JSONArray\n\n
    toJSON_DSM()\n
    '''
def toJSONv1():
    '''returns JSONArray\n\n
    toJSONv1()\n
    '''
def toJSONv2():
    '''returns JSONArray\n\n
    toJSONv2()\n
    '''
def toJSONv3():
    '''returns JSONArray\n\n
    toJSONv3()\n
    '''
def toJSONv7():
    '''returns JSONArray\n\n
    toJSONv7()\n
    '''
def toJSON():
    '''returns JSONArray\n\n
    toJSON(final int n)\n
    '''
def getKey():
    '''returns String\n\n
    getKey(final int n)\n
    '''
def setMetadataCorrelatorString():
    '''returns None\n\n
    setMetadataCorrelatorString(final String metadataCorrelator_)\n
    '''
def getMetadataCorrelator():
    '''returns String\n\n
    getMetadataCorrelator()\n
    '''
def prepareForAggregation():
    '''returns None\n\n
    prepareForAggregation()\n
    '''
def aggregate():
    '''returns None\n\n
    aggregate(final DataBeanStatementExecution dataBeanStatementExecution)\n
    '''
