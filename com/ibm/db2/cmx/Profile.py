MONITOR_ENABLED = "String  \"monitorEnabled\""
MONITOR_INTERVAL = "String  \"monitorCollectionInterval\""
def getName():
    '''    public String getName()
    '''
def getVersion():
    '''    public long getVersion()
    '''
def getSpecialRegisters():
    '''    public Properties getSpecialRegisters()
    '''
def getJccDirectives():
    '''    public HashMap<String, String> getJccDirectives()
    '''
def getCliDirectives():
    '''    public HashMap<String, String> getCliDirectives()
    '''
def getDotNetDirectives():
    '''    public HashMap<String, String> getDotNetDirectives()
    '''
def getWasDirectives():
    '''    public HashMap<String, String> getWasDirectives()
    '''
def getCmxDirectives():
    '''    public HashMap<String, String> getCmxDirectives()
    '''
def Driver():
    '''    public Driver(final String s, final long n, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5)
    public Driver(final String s, final long n, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final int pollingInterval_, final int statisticsCollectionInterval_, final int maxClientInfoToLogPerDataSource_)
    public Driver(final String s, final long n, final Properties properties, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5)
    public Driver(final String s, final long n, final Properties properties, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final int pollingInterval_, final int statisticsCollectionInterval_, final int maxClientInfoToLogPerDataSource_)
    '''
def updateToNewVersion():
    '''    public void updateToNewVersion(final Driver driver)
    public void updateToNewVersion(final DataSource dataSource)
    public void updateToNewVersion(final Database database)
    '''
def getPollingInterval():
    '''    public int getPollingInterval()
    '''
def getStatisticsCollectionInterval():
    '''    public int getStatisticsCollectionInterval()
    '''
def getMaxClientInfoToLogPerDataSource():
    '''    public int getMaxClientInfoToLogPerDataSource()
    '''
def DataSource():
    '''    public DataSource(final String s, final long n, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final TransactionRule.Remapping remapping, final TransactionRule.PenaltyBox penaltyBox, final com.ibm.db2.cmx.Database database, final com.ibm.db2.cmx.Database database2, final com.ibm.db2.cmx.Database database3)
    public DataSource(final String s, final long n, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final TransactionRule.Remapping[] transactionRemappingRules_, final TransactionRule.PenaltyBox[] transactionPenaltyBoxRules_, final com.ibm.db2.cmx.Database targetDatabase_, final com.ibm.db2.cmx.Database rerouteDatabase_, final com.ibm.db2.cmx.Database redirectDatabase_)
    public DataSource(final String s, final long n, final Properties properties, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final TransactionRule.Remapping[] transactionRemappingRules_, final TransactionRule.PenaltyBox[] transactionPenaltyBoxRules_, final com.ibm.db2.cmx.Database targetDatabase_, final com.ibm.db2.cmx.Database rerouteDatabase_, final com.ibm.db2.cmx.Database redirectDatabase_)
    '''
def getNumberOfTransactions():
    '''    public long getNumberOfTransactions()
    '''
def incrNumberOfTimesApplied():
    '''    public void incrNumberOfTimesApplied()
    '''
def resetNumberOfTimesApplied():
    '''    public void resetNumberOfTimesApplied()
    '''
def Database():
    '''    public Database(final String s, final long n, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final TransactionRule.Remapping remapping, final TransactionRule.PenaltyBox penaltyBox)
    public Database(final String s, final long n, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final TransactionRule.Remapping[] transactionRemappingRules_, final TransactionRule.PenaltyBox[] transactionPenaltyBoxRules_)
    public Database(final String s, final long n, final Properties properties, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final TransactionRule.Remapping[] transactionRemappingRules_, final TransactionRule.PenaltyBox[] transactionPenaltyBoxRules_)
    '''
