JDBC_DRIVER = "String  com.ibm.db2.jcc.DB2Driver""
DEF_FENCED_USER = "String  db2fenc1""
NO_FENCE = "String  noFence""
def getInstance():
'''public static DB2 getInstance(final ReadWriteConfiguration configProperties)
'''
pass
def DB2():
'''public DB2(final ReadWriteConfiguration configProperties)
'''
pass
def preCheck():
'''public List<TaskResult> preCheck()
'''
pass
def validate():
'''public List<TaskResult> validate()
'''
pass
def createInstance():
'''public TaskResult createInstance()
'''
pass
def dropInstance():
'''public TaskResult dropInstance()
'''
pass
def instanceExists():
'''public boolean instanceExists()
'''
pass
def createDatabase():
'''public TaskResult createDatabase()
'''
pass
def dropDatabase():
'''public TaskResult dropDatabase()
'''
pass
def databaseExists():
'''public boolean databaseExists()
'''
pass
def createTemporaryTablespace():
'''public TaskResult createTemporaryTablespace()
'''
pass
def dropTemporaryTablespace():
'''public TaskResult dropTemporaryTablespace()
'''
pass
def tempTablespaceExists():
'''public boolean tempTablespaceExists()
'''
pass
def dataTablespaceExists():
'''public boolean dataTablespaceExists()
'''
pass
def createDataTablespace():
'''public TaskResult createDataTablespace()
'''
pass
def dropDataTablespace():
'''public TaskResult dropDataTablespace()
'''
pass
def indexTablespaceExists():
'''public boolean indexTablespaceExists()
'''
pass
def createIndexTablespace():
'''public TaskResult createIndexTablespace()
'''
pass
def dropIndexTablespace():
'''public TaskResult dropIndexTablespace()
'''
pass
def createDatabaseUser():
'''public TaskResult createDatabaseUser()
'''
pass
def dropDatabaseUser():
'''public TaskResult dropDatabaseUser()
'''
pass
def userExists():
'''public boolean userExists(final String userName, final String userPassword)
'''
pass
def configureDatabaseUser():
'''public TaskResult configureDatabaseUser()
'''
pass
def setupPropertiesInDB():
'''public void setupPropertiesInDB()
'''
pass
def updateMaximoUserPolicy():
'''public TaskResult updateMaximoUserPolicy(final String userName)
'''
pass
def toString():
'''public String toString()
'''
pass
def tablespaceExists():
'''public boolean tablespaceExists(final String tsName)
'''
pass
def getTaskTotalTime():
'''public int getTaskTotalTime(final Task task)
'''
pass
def getTaskWeightCompleted():
'''public int getTaskWeightCompleted()
'''
pass
def formJDBCUrl():
'''public static String formJDBCUrl(final String host, final String port, final String dbName, final String home, final boolean enableSSL)
'''
pass
def aboutThisTask():
'''public String aboutThisTask(final Task task)
'''
pass
def main():
'''public static void main(final String[] args)
'''
pass
def validDB2UnixOSUser():
'''public TaskResult validDB2UnixOSUser(final String user)
'''
pass
def isSibConfig():
'''public boolean isSibConfig()
'''
pass
def setSibConfig():
'''public void setSibConfig(final boolean sibConfig_)
'''
pass
