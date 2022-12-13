MONITOR_ENABLED = "String  monitorEnabled""
MONITOR_INTERVAL = "String  monitorCollectionInterval""
def getName():
'''public String getName()
'''
pass
def getVersion():
'''public long getVersion()
'''
pass
def getSpecialRegisters():
'''public Properties getSpecialRegisters()
'''
pass
def getJccDirectives():
'''public HashMap<String, String> getJccDirectives()
'''
pass
def getCliDirectives():
'''public HashMap<String, String> getCliDirectives()
'''
pass
def getDotNetDirectives():
'''public HashMap<String, String> getDotNetDirectives()
'''
pass
def getWasDirectives():
'''public HashMap<String, String> getWasDirectives()
'''
pass
def getCmxDirectives():
'''public HashMap<String, String> getCmxDirectives()
'''
pass
def Driver():
'''public Driver(final String s, final long n, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5)
public Driver(final String s, final long n, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final int pollingInterval_, final int statisticsCollectionInterval_, final int maxClientInfoToLogPerDataSource_)
public Driver(final String s, final long n, final Properties properties, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5)
public Driver(final String s, final long n, final Properties properties, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final int pollingInterval_, final int statisticsCollectionInterval_, final int maxClientInfoToLogPerDataSource_)
'''
pass
def updateToNewVersion():
'''public void updateToNewVersion(final Driver driver)
public void updateToNewVersion(final DataSource dataSource)
public void updateToNewVersion(final Database database)
'''
pass
def getPollingInterval():
'''public int getPollingInterval()
'''
pass
def getStatisticsCollectionInterval():
'''public int getStatisticsCollectionInterval()
'''
pass
def getMaxClientInfoToLogPerDataSource():
'''public int getMaxClientInfoToLogPerDataSource()
'''
pass
def DataSource():
'''public DataSource(final String s, final long n, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final TransactionRule.Remapping remapping, final TransactionRule.PenaltyBox penaltyBox, final com.ibm.db2.cmx.Database database, final com.ibm.db2.cmx.Database database2, final com.ibm.db2.cmx.Database database3)
public DataSource(final String s, final long n, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final TransactionRule.Remapping[] transactionRemappingRules_, final TransactionRule.PenaltyBox[] transactionPenaltyBoxRules_, final com.ibm.db2.cmx.Database targetDatabase_, final com.ibm.db2.cmx.Database rerouteDatabase_, final com.ibm.db2.cmx.Database redirectDatabase_)
public DataSource(final String s, final long n, final Properties properties, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final TransactionRule.Remapping[] transactionRemappingRules_, final TransactionRule.PenaltyBox[] transactionPenaltyBoxRules_, final com.ibm.db2.cmx.Database targetDatabase_, final com.ibm.db2.cmx.Database rerouteDatabase_, final com.ibm.db2.cmx.Database redirectDatabase_)
'''
pass
def getNumberOfTransactions():
'''public long getNumberOfTransactions()
'''
pass
def incrNumberOfTimesApplied():
'''public void incrNumberOfTimesApplied()
'''
pass
def resetNumberOfTimesApplied():
'''public void resetNumberOfTimesApplied()
'''
pass
def Database():
'''public Database(final String s, final long n, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final TransactionRule.Remapping remapping, final TransactionRule.PenaltyBox penaltyBox)
public Database(final String s, final long n, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final TransactionRule.Remapping[] transactionRemappingRules_, final TransactionRule.PenaltyBox[] transactionPenaltyBoxRules_)
public Database(final String s, final long n, final Properties properties, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final TransactionRule.Remapping[] transactionRemappingRules_, final TransactionRule.PenaltyBox[] transactionPenaltyBoxRules_)
'''
pass
