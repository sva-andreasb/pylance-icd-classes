FORWARDONLY = "int  4"
SCROLLINSENSITIVE = "int  5"
SCROLLSENSITIVE = "int  6"
SCROLLSENSITIVEONE = "int  7"
FASTFORWARD = "int  8"
def getLock():
'''public synchronized Lock getLock(final Object connectionKey)
'''
pass
def DBManager():
'''public DBManager()
'''
pass
def configure():
'''public void configure(final Properties properties)
'''
pass
def getSchemaOwner():
'''public String getSchemaOwner()
'''
pass
def getProperties():
'''public Properties getProperties()
'''
pass
def getName():
'''public String getName()
'''
pass
def getDatabaseProductName():
'''public String getDatabaseProductName()
'''
pass
def getDatabaseProductSimpleVersion():
'''public String getDatabaseProductSimpleVersion()
'''
pass
def getDatabaseProductVersion():
'''public String getDatabaseProductVersion()
'''
pass
def getSSDisableCursor():
'''public static boolean getSSDisableCursor()
'''
pass
def getSSFetchUse():
'''public static boolean getSSFetchUse()
'''
pass
def getSSFetchSize():
'''public static int getSSFetchSize()
'''
pass
def getSSCursorType():
'''public static int getSSCursorType()
'''
pass
def getDbSqlServerDriver():
'''public static int getDbSqlServerDriver()
'''
pass
def getDBPlatform():
'''public static int getDBPlatform()
'''
pass
def getDB2Version():
'''public static double getDB2Version()
'''
pass
def init():
'''public boolean init()
'''
pass
def destroy():
'''public synchronized void destroy()
'''
pass
def getConnection():
'''public Connection getConnection(final ConnectionKey conKey)
'''
pass
def printStackTraceNoMsg():
'''public static void printStackTraceNoMsg(final Throwable e)
'''
pass
def freeConnection():
'''public void freeConnection(final ConnectionKey conKey)
public void freeConnection(final ConnectionKeyLight conKey)
'''
pass
def getSystemConnectionKey():
'''public ConnectionKey getSystemConnectionKey()
'''
pass
def getSequenceConnection():
'''public synchronized Connection getSequenceConnection()
'''
pass
def getDBConnTotal():
'''public int getDBConnTotal()
'''
pass
def getDBConnUsed():
'''public int getDBConnUsed()
'''
pass
def getDBConnFree():
'''public int getDBConnFree()
'''
pass
def getDBAuthenticationType():
'''public int getDBAuthenticationType()
'''
pass
def getCredentialHandler():
'''public DBCredentialHandler getCredentialHandler()
'''
pass
def getSQLTimeLimit():
'''public static long getSQLTimeLimit()
'''
pass
def needToLogSQLOnTimeLimit():
'''public static boolean needToLogSQLOnTimeLimit()
'''
pass
def reloadSQLTimeLimit():
'''public static synchronized void reloadSQLTimeLimit()
'''
pass
def needToLogSQLPlan():
'''public static boolean needToLogSQLPlan()
'''
pass
def reloadLogSQLPlan():
'''public static synchronized void reloadLogSQLPlan()
'''
pass
def reloadSQLScanExclude():
'''public static synchronized void reloadSQLScanExclude()
'''
pass
def reloadDBRowCount():
'''public synchronized void reloadDBRowCount()
'''
pass
def reloadDBRefCount():
'''public synchronized void reloadDBRefCount()
'''
pass
def reloadProperties():
'''public void reloadProperties(final Properties props)
'''
pass
def readSQLTimeLimit():
'''public static void readSQLTimeLimit()
'''
pass
def sqlTableScanExclude():
'''public static Vector sqlTableScanExclude()
'''
pass
def logSQLPlan():
'''public static StringBuffer logSQLPlan(final Connection conn, final String sqlStatement)
'''
pass
def getSPID():
'''public static synchronized String getSPID(final Connection connection)
'''
pass
def flushFreeConnections():
'''public void flushFreeConnections()
'''
pass
def getTenantUsedConnCount():
'''public HashMap<Integer, Integer> getTenantUsedConnCount(final UserInfo ui, final List<Integer> allTenants)
'''
pass
def run():
'''public void run()
public void run()
public void run()
public void run()
public void run()
'''
pass
def finalization():
'''public void finalization()
public void finalization(final int timeMilli)
'''
pass
def cleanupStatementQueue():
'''public void cleanupStatementQueue()
'''
pass
def getReferenceQueue():
'''public ReferenceQueue getReferenceQueue()
'''
pass
def Lock():
'''public Lock()
'''
pass
def ConnectionPoolThread():
'''public ConnectionPoolThread()
'''
pass
def finishWork():
'''public void finishWork()
'''
pass
def getRetryConnection():
'''public ConRef getRetryConnection()
'''
pass
