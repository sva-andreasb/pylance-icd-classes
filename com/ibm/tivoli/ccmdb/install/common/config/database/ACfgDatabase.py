def ACfgDatabase():
'''public ACfgDatabase()
'''
pass
def dropInstance():
'''public TaskResult dropInstance()
'''
pass
def dropDatabase():
'''public TaskResult dropDatabase()
'''
pass
def dropTemporaryTablespace():
'''public TaskResult dropTemporaryTablespace()
'''
pass
def dropDataTablespace():
'''public TaskResult dropDataTablespace()
'''
pass
def dropIndexTablespace():
'''public TaskResult dropIndexTablespace()
'''
pass
def dropDatabaseUser():
'''public TaskResult dropDatabaseUser()
'''
pass
def getConnection():
'''public Connection getConnection(final String userid, final String password, final String dbSchema)
public static Connection getConnection(final String jdbcUrl, final String userid, final String password, final String dbSchema)
'''
pass
def getDriverManagerConnection():
'''public static Connection getDriverManagerConnection(final String jdbcUrl, final String userid, final String password)
public static Connection getDriverManagerConnection(final String jdbcUrl, final String userid, final String password, final String dbSchema)
'''
pass
def registerDriver():
'''public static void registerDriver(final String driverName, final String[] driverJars)
'''
pass
def runConfigurationStep():
'''public TaskResult runConfigurationStep()
'''
pass
def undoConfiguration():
'''public TaskResult undoConfiguration()
'''
pass
def hasDatabaseSchemaBeenDeployed():
'''public TaskResult hasDatabaseSchemaBeenDeployed()
'''
pass
def verifyCompletion():
'''public TaskResult verifyCompletion()
'''
pass
def cronTaskExists():
'''public boolean cronTaskExists(final String userName)
'''
pass
def createCronTask():
'''public TaskResult createCronTask(final String userName)
'''
pass
def handleTextSearch():
'''public TaskResult handleTextSearch()
'''
pass
def getMaximoJDBCURL():
'''public static String getMaximoJDBCURL(final ReadConfiguration r)
public static String getMaximoJDBCURL(final Properties p)
public static String getMaximoJDBCURL(final HashMap<String, String> p)
'''
pass
def setMaximoJDBCURL():
'''public static String setMaximoJDBCURL(final ReadWriteConfiguration w, final String url)
'''
pass
def userSpecifiedJdbcUrl():
'''public static boolean userSpecifiedJdbcUrl(final ReadConfiguration r)
public static boolean userSpecifiedJdbcUrl()
'''
pass
def createJdbcUrl():
'''public static String createJdbcUrl(final String dbType, final String host, final String port, final String dbname, final String serviceName, final String userSpecifiedJdbcUrl)
'''
pass
def setRestrictivePasswordProperties():
'''public static boolean setRestrictivePasswordProperties(final ReadConfiguration configProperties)
'''
pass
def updateLightningProperties():
'''public void updateLightningProperties()
'''
pass
def main():
'''public static void main(final String[] args)
'''
pass
def handleInstallEvent():
'''public void handleInstallEvent(final ICmnInstallEvent requestEvent)
'''
pass
