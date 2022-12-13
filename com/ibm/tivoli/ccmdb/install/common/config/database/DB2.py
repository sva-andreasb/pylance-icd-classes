JDBC_DRIVER = "String  \"com.ibm.db2.jcc.DB2Driver\""
DEF_FENCED_USER = "String  \"db2fenc1\""
NO_FENCE = "String  \"noFence\""
def getInstance():
    '''    public static DB2 getInstance(final ReadWriteConfiguration configProperties)
    '''
def DB2():
    '''    public DB2(final ReadWriteConfiguration configProperties)
    '''
def preCheck():
    '''    public List<TaskResult> preCheck()
    '''
def validate():
    '''    public List<TaskResult> validate()
    '''
def createInstance():
    '''    public TaskResult createInstance()
    '''
def dropInstance():
    '''    public TaskResult dropInstance()
    '''
def instanceExists():
    '''    public boolean instanceExists()
    '''
def createDatabase():
    '''    public TaskResult createDatabase()
    '''
def dropDatabase():
    '''    public TaskResult dropDatabase()
    '''
def databaseExists():
    '''    public boolean databaseExists()
    '''
def createTemporaryTablespace():
    '''    public TaskResult createTemporaryTablespace()
    '''
def dropTemporaryTablespace():
    '''    public TaskResult dropTemporaryTablespace()
    '''
def tempTablespaceExists():
    '''    public boolean tempTablespaceExists()
    '''
def dataTablespaceExists():
    '''    public boolean dataTablespaceExists()
    '''
def createDataTablespace():
    '''    public TaskResult createDataTablespace()
    '''
def dropDataTablespace():
    '''    public TaskResult dropDataTablespace()
    '''
def indexTablespaceExists():
    '''    public boolean indexTablespaceExists()
    '''
def createIndexTablespace():
    '''    public TaskResult createIndexTablespace()
    '''
def dropIndexTablespace():
    '''    public TaskResult dropIndexTablespace()
    '''
def createDatabaseUser():
    '''    public TaskResult createDatabaseUser()
    '''
def dropDatabaseUser():
    '''    public TaskResult dropDatabaseUser()
    '''
def userExists():
    '''    public boolean userExists(final String userName, final String userPassword)
    '''
def configureDatabaseUser():
    '''    public TaskResult configureDatabaseUser()
    '''
def setupPropertiesInDB():
    '''    public void setupPropertiesInDB()
    '''
def updateMaximoUserPolicy():
    '''    public TaskResult updateMaximoUserPolicy(final String userName)
    '''
def toString():
    '''    public String toString()
    '''
def tablespaceExists():
    '''    public boolean tablespaceExists(final String tsName)
    '''
def getTaskTotalTime():
    '''    public int getTaskTotalTime(final Task task)
    '''
def getTaskWeightCompleted():
    '''    public int getTaskWeightCompleted()
    '''
def formJDBCUrl():
    '''    public static String formJDBCUrl(final String host, final String port, final String dbName, final String home, final boolean enableSSL)
    '''
def aboutThisTask():
    '''    public String aboutThisTask(final Task task)
    '''
def main():
    '''    public static void main(final String[] args)
    '''
def validDB2UnixOSUser():
    '''    public TaskResult validDB2UnixOSUser(final String user)
    '''
def isSibConfig():
    '''    public boolean isSibConfig()
    '''
def setSibConfig():
    '''    public void setSibConfig(final boolean sibConfig_)
    '''
