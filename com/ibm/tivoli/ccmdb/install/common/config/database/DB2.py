JDBC_DRIVER = "String  \"com.ibm.db2.jcc.DB2Driver\""
DEF_FENCED_USER = "String  \"db2fenc1\""
NO_FENCE = "String  \"noFence\""
def ():
    '''returns DB2\n\n
    (final ReadWriteConfiguration configProperties)\n
    '''
def preCheck():
    '''returns List<TaskResult>\n\n
    preCheck()\n
    '''
def validate():
    '''returns List<TaskResult>\n\n
    validate()\n
    '''
def createInstance():
    '''returns TaskResult\n\n
    createInstance()\n
    '''
def dropInstance():
    '''returns TaskResult\n\n
    dropInstance()\n
    '''
def instanceExists():
    '''returns boolean\n\n
    instanceExists()\n
    '''
def createDatabase():
    '''returns TaskResult\n\n
    createDatabase()\n
    '''
def dropDatabase():
    '''returns TaskResult\n\n
    dropDatabase()\n
    '''
def databaseExists():
    '''returns boolean\n\n
    databaseExists()\n
    '''
def createTemporaryTablespace():
    '''returns TaskResult\n\n
    createTemporaryTablespace()\n
    '''
def dropTemporaryTablespace():
    '''returns TaskResult\n\n
    dropTemporaryTablespace()\n
    '''
def tempTablespaceExists():
    '''returns boolean\n\n
    tempTablespaceExists()\n
    '''
def dataTablespaceExists():
    '''returns boolean\n\n
    dataTablespaceExists()\n
    '''
def createDataTablespace():
    '''returns TaskResult\n\n
    createDataTablespace()\n
    '''
def dropDataTablespace():
    '''returns TaskResult\n\n
    dropDataTablespace()\n
    '''
def indexTablespaceExists():
    '''returns boolean\n\n
    indexTablespaceExists()\n
    '''
def createIndexTablespace():
    '''returns TaskResult\n\n
    createIndexTablespace()\n
    '''
def dropIndexTablespace():
    '''returns TaskResult\n\n
    dropIndexTablespace()\n
    '''
def createDatabaseUser():
    '''returns TaskResult\n\n
    createDatabaseUser()\n
    '''
def dropDatabaseUser():
    '''returns TaskResult\n\n
    dropDatabaseUser()\n
    '''
def userExists():
    '''returns boolean\n\n
    userExists(final String userName, final String userPassword)\n
    '''
def configureDatabaseUser():
    '''returns TaskResult\n\n
    configureDatabaseUser()\n
    '''
def setupPropertiesInDB():
    '''returns None\n\n
    setupPropertiesInDB()\n
    '''
def updateMaximoUserPolicy():
    '''returns TaskResult\n\n
    updateMaximoUserPolicy(final String userName)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def tablespaceExists():
    '''returns boolean\n\n
    tablespaceExists(final String tsName)\n
    '''
def getTaskTotalTime():
    '''returns int\n\n
    getTaskTotalTime(final Task task)\n
    '''
def getTaskWeightCompleted():
    '''returns int\n\n
    getTaskWeightCompleted()\n
    '''
def aboutThisTask():
    '''returns String\n\n
    aboutThisTask(final Task task)\n
    '''
def validDB2UnixOSUser():
    '''returns TaskResult\n\n
    validDB2UnixOSUser(final String user)\n
    '''
def isSibConfig():
    '''returns boolean\n\n
    isSibConfig()\n
    '''
def setSibConfig():
    '''returns None\n\n
    setSibConfig(final boolean sibConfig_)\n
    '''
