JDBC_DRIVER = "String  \"oracle.jdbc.OracleDriver\""
def dropInstance():
    '''returns TaskResult\n\n
    dropInstance()\n
    '''
def createInstance():
    '''returns TaskResult\n\n
    createInstance()\n
    '''
def createIndexTablespace():
    '''returns TaskResult\n\n
    createIndexTablespace()\n
    '''
def dropIndexTablespace():
    '''returns TaskResult\n\n
    dropIndexTablespace()\n
    '''
def createDataTablespace():
    '''returns TaskResult\n\n
    createDataTablespace()\n
    '''
def dropDataTablespace():
    '''returns TaskResult\n\n
    dropDataTablespace()\n
    '''
def createTemporaryTablespace():
    '''returns TaskResult\n\n
    createTemporaryTablespace()\n
    '''
def dropTemporaryTablespace():
    '''returns TaskResult\n\n
    dropTemporaryTablespace()\n
    '''
def userExists():
    '''returns boolean\n\n
    userExists(final String userName, final String userPass)\n
    '''
def createDatabaseUser():
    '''returns TaskResult\n\n
    createDatabaseUser()\n
    '''
def dropDatabaseUser():
    '''returns TaskResult\n\n
    dropDatabaseUser()\n
    '''
def configureDatabaseUser():
    '''returns TaskResult\n\n
    configureDatabaseUser()\n
    '''
def tempTablespaceExists():
    '''returns boolean\n\n
    tempTablespaceExists()\n
    '''
def dataTablespaceExists():
    '''returns boolean\n\n
    dataTablespaceExists()\n
    '''
def indexTablespaceExists():
    '''returns boolean\n\n
    indexTablespaceExists()\n
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
def instanceExists():
    '''returns boolean\n\n
    instanceExists()\n
    '''
def validate():
    '''returns ArrayList<TaskResult>\n\n
    validate()\n
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
def preCheck():
    '''returns List<TaskResult>\n\n
    preCheck()\n
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
