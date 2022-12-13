def ACfgDatabase():
    '''    public ACfgDatabase()
    '''
def dropInstance():
    '''    public TaskResult dropInstance()
    '''
def dropDatabase():
    '''    public TaskResult dropDatabase()
    '''
def dropTemporaryTablespace():
    '''    public TaskResult dropTemporaryTablespace()
    '''
def dropDataTablespace():
    '''    public TaskResult dropDataTablespace()
    '''
def dropIndexTablespace():
    '''    public TaskResult dropIndexTablespace()
    '''
def dropDatabaseUser():
    '''    public TaskResult dropDatabaseUser()
    '''
def getConnection():
    '''    public Connection getConnection(final String userid, final String password, final String dbSchema)
    public static Connection getConnection(final String jdbcUrl, final String userid, final String password, final String dbSchema)
    '''
def getDriverManagerConnection():
    '''    public static Connection getDriverManagerConnection(final String jdbcUrl, final String userid, final String password)
    public static Connection getDriverManagerConnection(final String jdbcUrl, final String userid, final String password, final String dbSchema)
    '''
def registerDriver():
    '''    public static void registerDriver(final String driverName, final String[] driverJars)
    '''
def runConfigurationStep():
    '''    public TaskResult runConfigurationStep()
    '''
def undoConfiguration():
    '''    public TaskResult undoConfiguration()
    '''
def hasDatabaseSchemaBeenDeployed():
    '''    public TaskResult hasDatabaseSchemaBeenDeployed()
    '''
def verifyCompletion():
    '''    public TaskResult verifyCompletion()
    '''
def cronTaskExists():
    '''    public boolean cronTaskExists(final String userName)
    '''
def createCronTask():
    '''    public TaskResult createCronTask(final String userName)
    '''
def handleTextSearch():
    '''    public TaskResult handleTextSearch()
    '''
def getMaximoJDBCURL():
    '''    public static String getMaximoJDBCURL(final ReadConfiguration r)
    public static String getMaximoJDBCURL(final Properties p)
    public static String getMaximoJDBCURL(final HashMap<String, String> p)
    '''
def setMaximoJDBCURL():
    '''    public static String setMaximoJDBCURL(final ReadWriteConfiguration w, final String url)
    '''
def userSpecifiedJdbcUrl():
    '''    public static boolean userSpecifiedJdbcUrl(final ReadConfiguration r)
    public static boolean userSpecifiedJdbcUrl()
    '''
def createJdbcUrl():
    '''    public static String createJdbcUrl(final String dbType, final String host, final String port, final String dbname, final String serviceName, final String userSpecifiedJdbcUrl)
    '''
def setRestrictivePasswordProperties():
    '''    public static boolean setRestrictivePasswordProperties(final ReadConfiguration configProperties)
    '''
def updateLightningProperties():
    '''    public void updateLightningProperties()
    '''
def main():
    '''    public static void main(final String[] args)
    '''
def handleInstallEvent():
    '''    public void handleInstallEvent(final ICmnInstallEvent requestEvent)
    '''
