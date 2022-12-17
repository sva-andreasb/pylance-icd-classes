MONITOR_ENABLED = "String  \"monitorEnabled\""
MONITOR_INTERVAL = "String  \"monitorCollectionInterval\""
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getVersion():
    '''returns long\n\n
    getVersion()\n
    '''
def getSpecialRegisters():
    '''returns Properties\n\n
    getSpecialRegisters()\n
    '''
def ():
    '''returns Database\n\n
    (final String s, final long n, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5)\n
    (final String s, final long n, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final int pollingInterval_, final int statisticsCollectionInterval_, final int maxClientInfoToLogPerDataSource_)\n
    (final String s, final long n, final Properties properties, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5)\n
    (final String s, final long n, final Properties properties, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final int pollingInterval_, final int statisticsCollectionInterval_, final int maxClientInfoToLogPerDataSource_)\n
    (final String s, final long n, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final TransactionRule.Remapping remapping, final TransactionRule.PenaltyBox penaltyBox, final com.ibm.db2.cmx.Database database, final com.ibm.db2.cmx.Database database2, final com.ibm.db2.cmx.Database database3)\n
    (final String s, final long n, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final TransactionRule.Remapping[] transactionRemappingRules_, final TransactionRule.PenaltyBox[] transactionPenaltyBoxRules_, final com.ibm.db2.cmx.Database targetDatabase_, final com.ibm.db2.cmx.Database rerouteDatabase_, final com.ibm.db2.cmx.Database redirectDatabase_)\n
    (final String s, final long n, final Properties properties, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final TransactionRule.Remapping[] transactionRemappingRules_, final TransactionRule.PenaltyBox[] transactionPenaltyBoxRules_, final com.ibm.db2.cmx.Database targetDatabase_, final com.ibm.db2.cmx.Database rerouteDatabase_, final com.ibm.db2.cmx.Database redirectDatabase_)\n
    (final String s, final long n, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final TransactionRule.Remapping remapping, final TransactionRule.PenaltyBox penaltyBox)\n
    (final String s, final long n, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final TransactionRule.Remapping[] transactionRemappingRules_, final TransactionRule.PenaltyBox[] transactionPenaltyBoxRules_)\n
    (final String s, final long n, final Properties properties, final HashMap<String, String> hashMap, final HashMap<String, String> hashMap2, final HashMap<String, String> hashMap3, final HashMap<String, String> hashMap4, final HashMap<String, String> hashMap5, final TransactionRule.Remapping[] transactionRemappingRules_, final TransactionRule.PenaltyBox[] transactionPenaltyBoxRules_)\n
    '''
def updateToNewVersion():
    '''returns None\n\n
    updateToNewVersion(final Driver driver)\n
    updateToNewVersion(final DataSource dataSource)\n
    updateToNewVersion(final Database database)\n
    '''
def getPollingInterval():
    '''returns int\n\n
    getPollingInterval()\n
    '''
def getStatisticsCollectionInterval():
    '''returns int\n\n
    getStatisticsCollectionInterval()\n
    '''
def getMaxClientInfoToLogPerDataSource():
    '''returns int\n\n
    getMaxClientInfoToLogPerDataSource()\n
    '''
def getNumberOfTransactions():
    '''returns long\n\n
    getNumberOfTransactions()\n
    '''
def incrNumberOfTimesApplied():
    '''returns None\n\n
    incrNumberOfTimesApplied()\n
    '''
def resetNumberOfTimesApplied():
    '''returns None\n\n
    resetNumberOfTimesApplied()\n
    '''
