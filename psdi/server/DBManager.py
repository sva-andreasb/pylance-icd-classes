FORWARDONLY = "int  4"
SCROLLINSENSITIVE = "int  5"
SCROLLSENSITIVE = "int  6"
SCROLLSENSITIVEONE = "int  7"
FASTFORWARD = "int  8"
def getLock():
    '''    public synchronized Lock getLock(final Object connectionKey)
    '''
def DBManager():
    '''    public DBManager()
    '''
def configure():
    '''    public void configure(final Properties properties)
    '''
def getSchemaOwner():
    '''    public String getSchemaOwner()
    '''
def getProperties():
    '''    public Properties getProperties()
    '''
def getName():
    '''    public String getName()
    '''
def getDatabaseProductName():
    '''    public String getDatabaseProductName()
    '''
def getDatabaseProductSimpleVersion():
    '''    public String getDatabaseProductSimpleVersion()
    '''
def getDatabaseProductVersion():
    '''    public String getDatabaseProductVersion()
    '''
def getSSDisableCursor():
    '''    public static boolean getSSDisableCursor()
    '''
def getSSFetchUse():
    '''    public static boolean getSSFetchUse()
    '''
def getSSFetchSize():
    '''    public static int getSSFetchSize()
    '''
def getSSCursorType():
    '''    public static int getSSCursorType()
    '''
def getDbSqlServerDriver():
    '''    public static int getDbSqlServerDriver()
    '''
def getDBPlatform():
    '''    public static int getDBPlatform()
    '''
def getDB2Version():
    '''    public static double getDB2Version()
    '''
def init():
    '''    public boolean init()
    '''
def destroy():
    '''    public synchronized void destroy()
    '''
def getConnection():
    '''    public Connection getConnection(final ConnectionKey conKey)
    '''
def printStackTraceNoMsg():
    '''    public static void printStackTraceNoMsg(final Throwable e)
    '''
def freeConnection():
    '''    public void freeConnection(final ConnectionKey conKey)
    public void freeConnection(final ConnectionKeyLight conKey)
    '''
def getSystemConnectionKey():
    '''    public ConnectionKey getSystemConnectionKey()
    '''
def getSequenceConnection():
    '''    public synchronized Connection getSequenceConnection()
    '''
def getDBConnTotal():
    '''    public int getDBConnTotal()
    '''
def getDBConnUsed():
    '''    public int getDBConnUsed()
    '''
def getDBConnFree():
    '''    public int getDBConnFree()
    '''
def getDBAuthenticationType():
    '''    public int getDBAuthenticationType()
    '''
def getCredentialHandler():
    '''    public DBCredentialHandler getCredentialHandler()
    '''
def getSQLTimeLimit():
    '''    public static long getSQLTimeLimit()
    '''
def needToLogSQLOnTimeLimit():
    '''    public static boolean needToLogSQLOnTimeLimit()
    '''
def reloadSQLTimeLimit():
    '''    public static synchronized void reloadSQLTimeLimit()
    '''
def needToLogSQLPlan():
    '''    public static boolean needToLogSQLPlan()
    '''
def reloadLogSQLPlan():
    '''    public static synchronized void reloadLogSQLPlan()
    '''
def reloadSQLScanExclude():
    '''    public static synchronized void reloadSQLScanExclude()
    '''
def reloadDBRowCount():
    '''    public synchronized void reloadDBRowCount()
    '''
def reloadDBRefCount():
    '''    public synchronized void reloadDBRefCount()
    '''
def reloadProperties():
    '''    public void reloadProperties(final Properties props)
    '''
def readSQLTimeLimit():
    '''    public static void readSQLTimeLimit()
    '''
def sqlTableScanExclude():
    '''    public static Vector sqlTableScanExclude()
    '''
def logSQLPlan():
    '''    public static StringBuffer logSQLPlan(final Connection conn, final String sqlStatement)
    '''
def getSPID():
    '''    public static synchronized String getSPID(final Connection connection)
    '''
def flushFreeConnections():
    '''    public void flushFreeConnections()
    '''
def getTenantUsedConnCount():
    '''    public HashMap<Integer, Integer> getTenantUsedConnCount(final UserInfo ui, final List<Integer> allTenants)
    '''
def run():
    '''    public void run()
    public void run()
    public void run()
    public void run()
    public void run()
    '''
def finalization():
    '''    public void finalization()
    public void finalization(final int timeMilli)
    '''
def cleanupStatementQueue():
    '''    public void cleanupStatementQueue()
    '''
def getReferenceQueue():
    '''    public ReferenceQueue getReferenceQueue()
    '''
def Lock():
    '''    public Lock()
    '''
def ConnectionPoolThread():
    '''    public ConnectionPoolThread()
    '''
def finishWork():
    '''    public void finishWork()
    '''
def getRetryConnection():
    '''    public ConRef getRetryConnection()
    '''
